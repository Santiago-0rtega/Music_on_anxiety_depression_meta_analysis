# Supplementary Table: Music-exposure unit and pseudoreplication risk across included studies

This table is not derived from the extraction database — no field in `data/db251124.csv` records the physical unit (individual animal, cage, or room) that actually received an independently assignable music exposure. It was compiled by reading the full text of all 20 included primary papers (`CRIMEQ/independent_screening/pdf_text/*.json`) and classifying, for each study, the smallest unit that received the music exposure as reported by the authors themselves. Full supporting quotes, page numbers, and confidence ratings for every classification are in `CRIMEQ/independent_screening/reviewer_audit_exposure_unit.csv`.

**Across the 20 included studies, no study was classified as delivering music to individually housed/individually exposed animals as the exposure unit**: 11 studies delivered music at the room level, 4 at the cage level, and 5 could not be classified with confidence from the reported methods (`unclear`). Combining this with housing-structure evidence (e.g., explicit animals-per-cage counts even when the exact delivery mechanism was ambiguous), **18 of 20 studies (90%) show at least a plausible cage- or room-level pseudoreplication concern** — i.e., multiple animals sharing one acoustic environment while the original statistical analysis treated individual animals as fully independent replicates, with no cage/room/litter term in the model.

| # | Authors | Year | Title | Journal | Music-exposure unit | Pseudoreplication flag |
|---|---|---|---|---|---|---|
| 1 | Camargo et al. | 2013 | Adjuvant effects of classical music on simvastatin induced reduction of anxiety but not object recognition memory in rats | Psychology & Neuroscience | Room | Potential room-level |
| 2 | Chen et al. | 2019 | Regular music exposure in juvenile rats facilitates conditioned fear extinction and reduces anxiety after foot shock in adulthood | BioMed Research International | Room | Potential room-level |
| 3 | Cheng et al. | 2024 | Light and classical music therapies attenuate chronic unpredictable mild stress-induced depression via BDNF signaling pathway in mice | Heliyon | Unclear | Potential cage-level |
| 4 | Chikahisa et al. | 2007 | Anxiolytic effect of music depends on ovarian steroid in female mice | Behavioural Brain Research | Unclear | Potential cage-level |
| 5 | Escribano et al. | 2014 | Role of noise and music as anxiety modulators: relationship with ovarian hormones in the rat | Applied Animal Behaviour Science | Unclear | Potential cage-level |
| 6 | Flores-Gutiérrez et al. | 2018 | Exposure to patterned auditory stimuli during acute stress prevents despair-like behavior in adult mice previously housed in an enriched environment in combination with auditory stimuli | Neural Plasticity | Cage | Potential cage-level |
| 7 | Freitas Oliveira et al. | 2020 | Classical music and environmental enrichment enhanced spatial memory and learning and increased mouse innate tendency to avoid open spaces | EC Neurology | Cage | Potential cage-level |
| 8 | Fu et al. | 2023 | Music prevents stress-induced depression and anxiety-like behavior in mice | Translational Psychiatry | Room | Potential room-level (attenuated by individual housing) |
| 9 | Fu et al. | 2025 | Music therapy as a preventive intervention for postpartum depression: modulation of synaptic plasticity, oxidative stress, and inflammation in a mouse model | Translational Psychiatry | Room | Potential room-level |
| 10 | Krishnamurthy & Rao | 2025 | Indian classical Mohana Raga (instrumental music) overcomes anxiety, depression and memory impairment in chronic unpredictable mild stress rat model — a behavioural study | Indian Journal of Traditional Knowledge | Room | Potential room-level |
| 11 | Li et al. | 2010 | Anxiolytic effect of music exposure on BDNF^Met/Met transgenic mice | Brain Research | Cage | Potential cage-level |
| 12 | Milbratz de Camargo et al. | 2017 | Cocoa and classical music: effect on anxiety and antioxidant activity in Wistar rats | Archivos Latinoamericanos de Nutrición | Room | Potential room-level |
| 13 | Niehues da Cruz et al. | 2011 | The power of classic music to reduce anxiety in rats treated with simvastatin | Basic and Clinical Neuroscience | Room | Potential room-level |
| 14 | Pangemanan et al. | 2024 | Mozart K488 addition can improve depressive-like behavior in rats: in search of better management | Pharmacognosy Journal | Room | Potential cage- and room-level |
| 15 | Papadakakis et al. | 2019 | Music exposure attenuates anxiety- and depression-like behaviors and increases hippocampal spine density in male rats | Behavioural Brain Research | Room | Potential cage- and litter-level |
| 16 | Ren & Lu | 2024 | Heavy metal music, hip-hop music and construction noise induces depressive symptoms in mice | ASEAN Journal of Psychiatry | Unclear | Unclear (insufficient reporting) |
| 17 | Rizzolo et al. | 2021 | Long-term music exposure prevents age-related cognitive deficits in rats independently of hippocampal neurogenesis | Cerebral Cortex | Room | Potential cage- and room-level |
| 18 | Saghari et al. | 2021 | Music alleviates learning and memory impairments in an animal model of post-traumatic stress disorder | Biointerface Research in Applied Chemistry | Unclear | Unclear (insufficient reporting) |
| 19 | Sampaio et al. | 2017 | Effect of music therapy on the developing central nervous system of rats | Psychology & Neuroscience | Room | Potential room-level |
| 20 | Terzioğlu-Usak et al. | 2020 | Effects of music on stress induced hormones and oxidative stress levels | Cukurova Medical Journal | Cage | Potential cage-level (severe — single shared cage per condition) |

**Summary counts (music-exposure unit):** Room = 11 studies; Cage = 4 studies; Unclear = 5 studies; Individual = 0 studies.

**Notes:**
- Full author lists (some papers have 5–11 co-authors) are in `References/included.bib`; this table abbreviates to the first author for readability.
- Study #11 (Li et al. 2010): the primary paper also tested genetically modified BDNF^Met/Met and BDNF+/- mice, but only the **wild-type** comparisons (coded `Strain = C57BL/6` in the extraction database) were carried into `data/db251124.csv` — the transgenic groups were not extracted as separate effect sizes. This does not change the strain audit reported elsewhere (§7 of the main audit report), but is noted here because the paper's own title references a transgenic line.
- "Unclear" means the paper's reported methods did not give enough detail to determine the exposure unit with confidence — it is not a claim that exposure was individual.
- See `CRIMEQ/independent_screening/reviewer_audit_exposure_unit.csv` for per-study quotes, page numbers, and confidence ratings underlying every classification in this table, and `reviewer_response_audit/REVIEWER_AUDIT_REPORT.md` (§3–4) for the full interpretation.
