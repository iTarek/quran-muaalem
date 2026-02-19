import litserve as ls

from quran_muaalem.engine.serve import QuranMuaalemAPI

if __name__ == "__main__":
    api = QuranMuaalemAPI(
        max_batch_size=128,
        batch_timeout=0.5,
    )
    server = ls.LitServer(api, accelerator="cuda", devices=1, workers_per_device=1)
    server.run(port=8000)
