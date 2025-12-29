import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'Quran Muaalem',
  description: 'Docs for the Quran Muaalem model and the quran-transcript toolkit',
  base: '/quran-muaalem/',
  themeConfig: {
    nav: [
      { text: 'Getting Started', link: '/getting-started' },
      { text: 'Quran Muaalem', link: '/muaalem/' },
      { text: 'Quran Transcript', link: '/quran-transcript/' },
      { text: 'Model', link: '/model/' },
      { text: 'Developer', link: '/dev/' },
    ],
    sidebar: [
      {
        text: 'Getting Started',
        link: '/getting-started',
      },
      {
        text: 'Quran Muaalem',
        items: [
          { text: 'Overview', link: '/muaalem/' },
          { text: 'Gradio UI', link: '/muaalem/gradio-ui' },
          { text: 'Python API', link: '/muaalem/python-api' },
          { text: 'Outputs', link: '/muaalem/output' },
        ],
      },
      {
        text: 'Model and Architecture',
        items: [
          { text: 'Overview', link: '/model/' },
          { text: 'Architecture', link: '/model/architecture' },
          { text: 'Weights and Dtype', link: '/model/weights' },
        ],
      },
      {
        text: 'Phonetic Pipeline',
        items: [
          { text: 'Overview', link: '/pipeline/' },
          { text: 'Moshaf Attributes', link: '/pipeline/moshaf-attributes' },
        ],
      },
      {
        text: 'Quran Transcript',
        items: [
          { text: 'Overview', link: '/quran-transcript/' },
          { text: 'Installation', link: '/quran-transcript/installation' },
          { text: 'Usage', link: '/quran-transcript/usage' },
          { text: 'Phonetics', link: '/quran-transcript/phonetics' },
          { text: 'Tools', link: '/quran-transcript/tools' },
        ],
      },
      {
        text: 'Training and Data',
        items: [
          { text: 'Overview', link: '/training/' },
          { text: 'Data Sources', link: '/training/data-sources' },
          { text: 'Pipeline Steps', link: '/training/pipeline' },
        ],
      },
      {
        text: 'Developer',
        items: [
          { text: 'Overview', link: '/dev/' },
          { text: 'Tests', link: '/dev/tests' },
          { text: 'Contributing', link: '/dev/contributing' },
        ],
      },
      {
        text: 'Appendix',
        items: [
          { text: 'Paper', link: '/appendix/paper' },
          { text: 'License', link: '/appendix/license' },
          { text: 'FAQ', link: '/appendix/faq' },
        ],
      },
    ],
    socialLinks: [
      { icon: 'github', link: 'https://github.com/obadx/quran-muaalem' },
    ],
  },
})
