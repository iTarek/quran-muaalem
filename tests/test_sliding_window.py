from time import perf_counter
from dataclasses import dataclass


from quran_transcript import Aya, quran_phonetizer, MoshafAttributes
import numpy as np
import torch
from librosa.core import load
from transformers import AutoFeatureExtractor

from quran_muaalem.modeling.multi_level_tokenizer import MultiLevelTokenizer
from quran_muaalem.modeling.modeling_multi_level_ctc import Wav2Vec2BertForMultilevelCTC
from quran_muaalem.decode import ctc_decode


def count_frames(samples: int, window=400, hop_size=160, stride=2):
    return (samples - window) / (stride * hop_size)


def count_sampels_from_frames(
    num_frames: int, window=400, hop_size=160, stride=2
) -> int:
    return int(num_frames * stride * hop_size + window)


def fix_chunk_length(chunk_ms: float, sampling_rate=16000) -> float:
    """fix chunk length so the input of each frame to the model
    is complete not padded with zeros by the preprossor
    """
    num_frames = count_frames(int(chunk_ms * sampling_rate / 1000))
    fixed_sampels = count_sampels_from_frames(np.ceil(num_frames))
    return fixed_sampels / sampling_rate * 1000


def diff_lists(old_list, new_list):
    """
    Show differences between two lists of integers in GitHub-like format.

    Args:
        old_list: Original list of integers
        new_list: New list of integers

    Returns:
        String with formatted diff output
    """
    # Create dictionaries to track positions
    old_dict = {}
    for i, num in enumerate(old_list):
        old_dict.setdefault(num, []).append(i)

    new_dict = {}
    for i, num in enumerate(new_list):
        new_dict.setdefault(num, []).append(i)

    # Initialize result
    result_lines = []
    i, j = 0, 0

    while i < len(old_list) or j < len(new_list):
        if i < len(old_list) and j < len(new_list) and old_list[i] == new_list[j]:
            # Unchanged line
            result_lines.append(f"  {old_list[i]}")
            i += 1
            j += 1
        else:
            # Try to find if current old element appears later in new list
            moved_to_future = False
            if i < len(old_list):
                for k in range(j + 1, len(new_list)):
                    if new_list[k] == old_list[i] and not any(
                        x["old_idx"] == i for x in result_lines if "old_idx" in x
                    ):
                        # This element moved forward
                        for pos in range(j, k):
                            if pos < len(new_list):
                                result_lines.append(
                                    {
                                        "type": "+",
                                        "value": new_list[pos],
                                        "old_idx": None,
                                        "new_idx": pos,
                                    }
                                )
                        result_lines.append(f"  {old_list[i]}")
                        j = k + 1
                        i += 1
                        moved_to_future = True
                        break

            if not moved_to_future:
                # Check if current new element appeared earlier in old list
                moved_from_past = False
                if j < len(new_list):
                    for k in range(i + 1, len(old_list)):
                        if old_list[k] == new_list[j] and not any(
                            x["new_idx"] == j for x in result_lines if "new_idx" in x
                        ):
                            # This element was moved from later in old list
                            for pos in range(i, k):
                                if pos < len(old_list):
                                    result_lines.append(
                                        {
                                            "type": "-",
                                            "value": old_list[pos],
                                            "old_idx": pos,
                                            "new_idx": None,
                                        }
                                    )
                            result_lines.append(f"  {new_list[j]}")
                            i = k + 1
                            j += 1
                            moved_from_past = True
                            break

                if not moved_from_past:
                    # Simple addition or deletion
                    if j >= len(new_list) or (
                        i < len(old_list)
                        and old_list[i] not in new_dict.get(new_list[j], [])
                    ):
                        # Deletion
                        result_lines.append(
                            {
                                "type": "-",
                                "value": old_list[i],
                                "old_idx": i,
                                "new_idx": None,
                            }
                        )
                        i += 1
                    else:
                        # Addition
                        result_lines.append(
                            {
                                "type": "+",
                                "value": new_list[j],
                                "old_idx": None,
                                "new_idx": j,
                            }
                        )
                        j += 1

    # Format the output
    formatted_lines = []
    for line in result_lines:
        if isinstance(line, str):
            formatted_lines.append(line)
        else:
            formatted_lines.append(f"{line['type']} {line['value']}")

    return "\n".join(formatted_lines)


def show_list_diff(old_list, new_list, context_lines=3):
    """
    Display list diff with GitHub-like formatting including context.

    Args:
        old_list: Original list
        new_list: New list
        context_lines: Number of unchanged lines to show around changes
    """
    # Get the basic diff
    diff_output = diff_lists(old_list, new_list).split("\n")

    # Add line numbers and formatting
    old_line_num = 1
    new_line_num = 1
    output = []
    in_change_block = False

    print("Diff between lists:")
    print(f"--- Original list")
    print(f"+++ New list")
    print()

    for line in diff_output:
        if line.startswith("  "):
            # Unchanged line - show with context
            num = line[2:]
            if not in_change_block:
                output.append(f" {old_line_num:3} {new_line_num:3}   {num}")
            else:
                output.append(f" {old_line_num:3} {new_line_num:3}   {num}")
                in_change_block = False
            old_line_num += 1
            new_line_num += 1
        elif line.startswith("-"):
            # Deleted line
            num = line[2:]
            output.append(f"\033[91m-{old_line_num:3}      {num}\033[0m")
            old_line_num += 1
            in_change_block = True
        elif line.startswith("+"):
            # Added line
            num = line[2:]
            output.append(f"\033[92m+     {new_line_num:3} {num}\033[0m")
            new_line_num += 1
            in_change_block = True

    # Print with context
    if context_lines > 0:
        # Find change indices
        change_indices = [i for i, line in enumerate(output) if "\033[" in line]

        if change_indices:
            # Expand context around changes
            show_indices = set()
            for idx in change_indices:
                for i in range(
                    max(0, idx - context_lines),
                    min(len(output), idx + context_lines + 1),
                ):
                    show_indices.add(i)

            # Print with context
            for i in show_indices:
                print(output[i])
        else:
            # No changes, show all
            for line in output:
                print(line)
    else:
        # Show all lines
        for line in output:
            print(line)

    # Show summary
    changes = sum(
        1 for line in diff_output if line.startswith("-") or line.startswith("+")
    )
    if changes > 0:
        print(f"\nTotal changes: {changes}")
    else:
        print("\nNo changes detected.")


# Alternative simple version for basic diff
def simple_list_diff(old_list, new_list):
    """
    Simple diff showing - for removed items and + for added items.
    """
    result = []

    # Find removed items
    for item in old_list:
        if item not in new_list:
            result.append(f"- {item}")
        else:
            result.append(f"  {item}")

    # Find added items
    for item in new_list:
        if item not in old_list:
            result.append(f"+ {item}")

    return "\n".join(result)


@torch.no_grad()
def run_muaalem(
    wave,
    model: Wav2Vec2BertForMultilevelCTC,
    processor: AutoFeatureExtractor,
    device: str | torch.device,
    dtype: str | torch.dtype,
    sampling_rate=16000,
):
    features = processor(wave, return_tensors="pt", sampling_rate=sampling_rate)
    features = {k: v.to(device, dtype=dtype) for k, v in features.items()}
    level_to_logits = model(**features)[0]
    level_to_probs = {
        k: torch.softmax(v, dim=-1).to("cpu")[:, :, 0]
        for k, v in level_to_logits.items()
    }
    level_to_ids = {k: v.argmax(dim=-1).to("cpu") for k, v in level_to_logits.items()}
    return level_to_ids, level_to_probs


@dataclass
class MergeMatch:
    longest_match: int | None = None
    start_a_idx: int | None = None
    start_b_idx: int | None = None

    def update(self, match: "MergeMatch"):
        self.longest_match = match.longest_match
        self.start_a_idx = match.start_a_idx
        self.start_b_idx = match.start_b_idx


def merge_lists_with_overlap(A, B, num_ignore=2, max_B_offset=2):
    """
    Merge two lists by finding the maximum overlap between the end of A and beginning of B.

    * If there is not common sub sequence:
        delete last num_ignore of A and concatenate B

    Args:
        A: First list
        B: Second list
        max_B_offset: the starting point of comarison is shifted to the left by `max_B_offset`
        EX: A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], B = [5, 6, 7, 8]

        if max_B_offset = 0 then start point:
        A: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        B:                   [5, 6, 7, 8]

        if max_B_offset = 1 then start point:
        A: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        B:                [5, 6, 7, 8]

        if max_B_offset = 2 then start point:
        A: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        B:             [5, 6, 7, 8]

        Then shifting B to the right step by step unitl we find a match


    Returns:
        Merged list with overlap handled optimally
    """

    a_orig_offset = max(len(A) - len(B) - max_B_offset, 0)
    b_span = min(len(A), len(B))
    print(f"A({len(A)}):\n{A}\nB({len(B)}):\n{B}")
    curr_match = MergeMatch()
    best_match = MergeMatch()
    for a_offset in range(a_orig_offset, len(A)):
        for ptr in range(b_span):
            a_idx = a_offset + ptr
            b_idx = ptr

            if A[a_idx] == B[b_idx]:
                if curr_match.longest_match is None:
                    curr_match.longest_match = 1
                    curr_match.start_a_idx = a_idx
                    curr_match.start_b_idx = b_idx
                else:
                    curr_match.longest_match += 1
            elif curr_match.longest_match is not None:
                if best_match.longest_match is None:
                    best_match.update(curr_match)
                    curr_match.longest_match = None
                elif curr_match.longest_match > best_match.longest_match:
                    best_match.update(curr_match)
                    curr_match.longest_match = None

        # Last check
        if curr_match.longest_match is not None:
            if best_match.longest_match is None:
                best_match.update(curr_match)
            elif curr_match.longest_match > best_match.longest_match:
                best_match.update(curr_match)

        # Reset step
        curr_match.longest_match = None
        if (a_offset + len(B)) >= len(A):
            b_span -= 1

    if best_match.longest_match is None:
        return A + B
    else:
        # Making B overwriting A
        # TODO: make this desicions with a margin min_distance
        assert best_match.start_a_idx is not None and best_match.start_b_idx is not None
        print(
            f"Start of A: {best_match.start_a_idx}, Start of B IDX: {best_match.start_b_idx}, Longest Match: {best_match.longest_match}"
        )
        print("\n\n")
        return A[: best_match.start_a_idx] + B[best_match.start_b_idx :]


def sliding_window_inference(
    wave,
    model: Wav2Vec2BertForMultilevelCTC,
    processor: AutoFeatureExtractor,
    device: str | torch.device,
    dtype: str | torch.dtype,
    window_ms: int,
    chunk_ms: int,
    sampling_rate: int = 16000,
):
    window_samples = int(window_ms / 1000 * sampling_rate)
    chunk_samples = int(chunk_ms / 1000 * sampling_rate)
    overlap_samples = window_samples - chunk_samples

    merged_ph_ids: list = []
    for start in range(0, len(wave) - window_samples, chunk_samples):
        end = start + window_samples
        print(
            f"Start MS: {start / sampling_rate * 1000}, End MS: {end / sampling_rate * 1000}"
        )
        # Golden Seqence
        level_to_ids, level_to_probs = run_muaalem(
            wave=wave[start:end],
            model=model,
            processor=processor,
            device=device,
            dtype=dtype,
        )
        curr_ph_ids = level_to_ids["phonemes"]
        curr_ph_probs = level_to_probs["phonemes"]
        curr_ph_ids = ctc_decode(curr_ph_ids, curr_ph_probs)[0].ids.tolist()
        if curr_ph_ids:
            if curr_ph_ids[-1] == 0:
                curr_ph_ids = curr_ph_ids[:-1]
        # print(curr_ph_ids)
        # merging ids
        if merged_ph_ids:
            merged_ph_ids = merge_lists_with_overlap(merged_ph_ids, curr_ph_ids)
        else:
            merged_ph_ids = curr_ph_ids
        # print(merged_ph_ids)

    return merged_ph_ids


def decode_phonemes(ids: list, vocab):
    id_to_ph = {v: k for k, v in vocab["phonemes"].items()}
    out_str = ""
    for idx in ids:
        out_str += id_to_ph[idx]
    return out_str


if __name__ == "__main__":
    window_ms = 3000
    chunk_ms = 300
    window_ms = int(fix_chunk_length(window_ms))
    chunk_ms = int(fix_chunk_length(chunk_ms))
    sampling_rate = 16000
    # audio_path = "./assets/test.wav"
    audio_path = "./assets/fatiha_long_track.wav"
    device = "cuda"
    model_id = "obadx/muaalem-model-v3_2"
    dtype = torch.bfloat16

    print(f"Window(ms): `{window_ms}`. Chunk(ms): `{chunk_ms}`")

    mulit_level_tokenizer = MultiLevelTokenizer(model_id)

    model = Wav2Vec2BertForMultilevelCTC.from_pretrained(model_id)
    model.to(device, dtype=dtype)
    processor = AutoFeatureExtractor.from_pretrained(
        model_id, sampling_rate=sampling_rate
    )

    uthmani_ref = Aya(8, 75).get_by_imlaey_words(17, 9).uthmani
    moshaf = MoshafAttributes(
        rewaya="hafs",
        madd_monfasel_len=2,
        madd_mottasel_len=4,
        madd_mottasel_waqf=4,
        madd_aared_len=2,
    )
    phonetizer_out = quran_phonetizer(uthmani_ref, moshaf, remove_spaces=True)

    wave, _ = load(audio_path, sr=sampling_rate, mono=True)

    # Golden Seqence
    golden_level_to_ids, golden_level_to_probs = run_muaalem(
        wave=wave,
        model=model,
        processor=processor,
        device=device,
        dtype=dtype,
    )
    golden_phonemes_ids = ctc_decode(
        batch_ids=golden_level_to_ids["phonemes"],
        batch_probs=golden_level_to_probs["phonemes"],
    )[0].ids.tolist()

    # Sliding window Algorithm
    sw_ph_ids = sliding_window_inference(
        wave=wave,
        model=model,
        processor=processor,
        dtype=dtype,
        device=device,
        window_ms=window_ms,
        chunk_ms=chunk_ms,
        sampling_rate=sampling_rate,
    )
    print(golden_phonemes_ids)
    print(sw_ph_ids)
    print(f"len sw: {len(sw_ph_ids)}, len of golden: {len(golden_phonemes_ids)}")
    print(golden_phonemes_ids == sw_ph_ids)

    decode_phonemes([1], mulit_level_tokenizer.vocab)
