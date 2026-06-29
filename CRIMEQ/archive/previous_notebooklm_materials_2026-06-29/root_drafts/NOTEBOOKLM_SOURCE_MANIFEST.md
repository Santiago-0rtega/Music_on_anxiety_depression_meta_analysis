# NotebookLM Source Manifest for CRIME-Q Live Test

Use this manifest to map uploaded PDF filenames to the study-level IDs used in the
CRIME-Q gold standard and scoring script. The PDF filenames in `References/` are
UUID-style names, so NotebookLM should identify the target paper by both
`Study_ID` and title before scoring.

| Study_ID | PDF file in `References/` | Title |
|---|---|---|
| Camargo_2013_PSYN | `5021c4a6-0672-3f03-1433-a176a012e9f8.pdf` | Adjuvant effects of classical music on simvastatin induced reduction of anxiety but not object recognition memory in rats |
| Chen_2019_BIOMEDRI | `1799f359-e95b-5fe1-7cee-d82b4bf43920.pdf` | Regular Music Exposure in Juvenile Rats Facilitates Conditioned Fear Extinction and Reduces Anxiety after Foot Shock in Adulthood |
| Cheng_2024_HLYN | `0538fc51-e1d3-2acb-5bc5-d17b55e3ffb4.pdf` | Light and classical music therapies attenuate chronic unpredictable mild stress-induced depression via BDNF signaling pathway in mice |
| Chikahisa_2007_BBR | `377b1971-3f63-5427-579a-b6bcb1d65da4.pdf` | Anxiolytic effect of music depends on ovarian steroid in female mice |
| Escribano_2014_APPANBSC | `44dfd16d-85f8-5aed-06b8-2f723e166254.pdf` | Role of noise and music as anxiety modulators: Relationship with ovarian hormones in the rat |
| Flores_2018_NP | `255a62bd-d9bb-4169-7d56-dd6e97940c98.pdf` | Exposure to Patterned Auditory Stimuli during Acute Stress Prevents Despair-Like Behavior in Adult Mice That Were Previously Housed in an Enriched Environment in Combination with Auditory Stimuli |
| Freitas_2020_ECNE | `179d969e-5038-b21d-0507-1fa72703a44c.pdf` | Classical Music and Environmental Enrichment Enhanced Spatial Memory and Learning and Increased Mouse Innate Tendency to Avoid Open Spaces |
| Fu_2023_TRANSPSY | `16dcc961-504d-748f-2f29-731777f65ffc.pdf` | Music prevents stress-induced depression and anxiety-like behavior in mice |
| Fu_2025_TRANSPSY | `18575e71-93b7-943f-000b-fa61ebb65b4c.pdf` | Music therapy as a preventive intervention for postpartum depression: modulation of synaptic plasticity, oxidative stress, and inflammation in a mouse model |
| Krishnamurthy_2025_INDIANJTRADITKNOW | `58e803ba-3e31-0227-35d5-a827ca566704.pdf` | Indian classical Mohana Raga (instrumental music) overcomes anxiety, depression and memory impairment in chronic unpredictable mild stress rat model - A behavioural study |
| Li_2010_BR | `0862b837-2d02-63cf-49c9-4c9ad8e30bf4.pdf` | Anxiolytic effect of music exposure on BDNFMet/Met transgenic mice |
| Milbratz_2017_ALN | `46eb6eb1-1b6b-4e4d-3320-8b3476341850.pdf` | Cocoa and classical music: effect on anxiety and antioxidant activity in Wistar rats |
| Niehues_2011_BCNEURO | `230f6915-3bc9-fd95-48ee-66b72afaed90.pdf` | The Power of Classic Music to Reduce Anxiety in Rats Treated with Simvastatin |
| Pangemanan_2024_PHJ | `20f170d7-297b-69b9-46f1-27c3c78443ac.pdf` | Mozart K488 Addition Can Improve Depressive-Like Behavior in Rats: In Search of Better Management |
| Papadakakis_2019_BBR | `08d1f3da-a098-1ba5-1af0-d144db066128.pdf` | Music exposure attenuates anxiety- and depression-like behaviors and increases hippocampal spine density in male rats |
| Ren_2024_ASEAN | `0225aea1-a873-5483-5b5d-cc380a442c3c.pdf` | Heavy metal Music, Hip-hop Music and Construction Noise Induces Depressive Symptoms in mice |
| Rizzolo_2021_CC | `1c675768-2422-78e7-5041-7f0985732940.pdf` | Long-Term Music Exposure Prevents Age-Related Cognitive Deficits in Rats Independently of Hippocampal Neurogenesis |
| Saghari_2021_BIOINTERFACE | `4db54856-a790-9c6f-5e46-ebcd043664ac.pdf` | Music Alleviates Learning and Memory Impairments in an Animal Model of Post-Traumatic Stress Disorder |
| Sampaio_2017_PSYNEURO | `03c53367-5d52-b22b-6bd3-588f4ec65c78.pdf` | Effect of Music Therapy on the Developing Central Nervous System of Rats |
| Terzioglu_2020_CMJ | `6fdec913-1997-d465-279c-38c2a5c341dc.pdf` | Effects of music on stress induced hormones and oxidative stress levels |

Live-test rule: for a per-study query, use only the target paper named here plus
`CRIME-Q_Detailed_Codebook_v3.md`. Do not borrow evidence from any other study
PDF in the notebook.
