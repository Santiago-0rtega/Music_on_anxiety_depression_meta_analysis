# MUSIC-CRIME-Q: NotebookLM Extraction Manual

**Project:** *Music exposure reduces anxiety- and depression-like behavior in rodents: a systematic review and multilevel meta-analysis*
**Assessment framework:** Adapted CRIME-Q (Critical Appraisal of Methodological [technical] Quality, Quality of Reporting and Risk of Bias in Animal Research)
**Version:** 1.8 — 22 June 2026
**Changes from v1.7:** The separate music-specific acoustic-design flag has been removed. The primary matrix now contains **23 adapted CRIME-Q/SYRCLE item columns** (plus `Study_ID` and `Cohort_ID`), and all workflow, evidence, and sensitivity-analysis references to that separate flag have been deleted. Use the accompanying item-level codebook `CRIME-Q_Music_RoB_Codebook_v1.8.csv` for authoritative response options and operational rules.

**Changes from v1.2:** The **unit of assessment is the cohort, not the study.** Appraisal is grounded to a **frozen roster of 49 cohorts** (one per `Cohort_ID = Study_ID + Ex_ID`) generated from the meta-analysis extraction — NotebookLM rates exactly those 49 cohorts and never invents, splits, or drops one. The primary deliverable is a **wide CRIME-Q matrix: 49 rows (one per cohort) × 23 item columns** (`RoB_Matrix_cohort`). Study-level items are propagated identically across a study's cohorts; cohort-sensitive items are judged per cohort. **Reporting is by cohort distribution within each study** (no worst-case collapse, no total score), and **sensitivity analyses drop individual bad cohorts, not whole studies** — which the cohort-level variance–covariance structure supports directly.

---

## 1. Purpose and scope

Use this document to extract a transparent, cohort-level critical appraisal from the PDFs of the included primary animal studies (results are then described per study; see Section 11.2). The assessment is for experiments comparing a **music-exposure condition** with an appropriate **control condition** and measuring anxiety- or depression-like behavioural outcomes in laboratory rodents.

CRIME-Q distinguishes three constructs. Keep them separate:

- **QoR — quality of reporting:** whether the report contains enough information to understand and reproduce the work.
- **MQ — methodological/technical quality:** whether the described experiment appears technically feasible and appropriately implemented.
- **RoB — risk of bias:** whether design or conduct features could systematically distort the estimated music effect.

Do **not** turn the items into a total score, label a paper globally "high" or "low" quality, or recommend excluding studies. CRIME-Q intentionally does not prescribe an overall numerical score. The final review should present item-level results and, if appropriate, pre-specified sensitivity analyses.

This is an **assisted extraction protocol**, not an autonomous final appraisal. NotebookLM must extract evidence and provisional codes; a human reviewer must check every code against the source PDF. Final ratings should be reached by two independent human reviewers, followed by consensus adjudication.

---

## 2. Sources NotebookLM may use

For each study assessed, use only:

1. That study's primary PDF (the source being assessed);
2. Its associated supplementary material, appendices, or protocol **only when supplied as a source**;
3. This extraction manual;
4. The item-level codebook supplied as a source (`CRIME-Q_Music_RoB_Codebook_v1.8.csv`); and
5. The CRIME-Q paper supplied as a source (`s12874-024-02413-0.pdf`).

Do **not** use review articles, other included studies, author webpages, general knowledge, journal norms, or plausible laboratory practice to fill missing information. **Assess each study only against its own PDF.** A method is **not reported** unless it is stated in that study's PDF or its supplied supplement.

---

## 3. Unit of assessment — the cohort (grounded to a frozen roster)

### The unit is the cohort, fixed in advance

The unit of assessment is the **independent experimental cohort**, identified by `Cohort_ID = Study_ID + "_" + Ex_ID`. **You do not decide the cohorts.** They are fixed by the meta-analysis extraction and supplied to you as the **frozen cohort roster** (`crime_q_cohort_roster.csv` / the table in Section 5.1). This review has exactly **49 cohorts across 20 reports**.

This matters because a single paper often contains several cohorts, and some contrasts in a paper were deliberately **excluded** from the meta-analysis (e.g., non–music-versus-control arms, or co-intervention arms outside the contrast of interest). The roster already encodes those inclusion decisions. **Assess every cohort in the roster and only the cohorts in the roster** — do not add a cohort you find in a PDF, do not split one roster cohort into several, and do not merge two roster cohorts.

Each roster row gives you:

- `Cohort_ID` — the assessment unit (e.g., `Escribano_2014_APPANBSC_ex001`).
- `Study_ID`, `Ex_ID` — the parent study and experiment index.
- `Contrast(s)`, `Co-manipulation`, `Induced_model`, `Music_type`, `Control`, `Assays` — the **scope** of that cohort, so your judgments (especially attrition, baseline balance, and design) are based on the right animals and the right comparison.

### Why cohort, not study

Most CRIME-Q items are study-level and will be identical across a study's cohorts (see Section 9.3). But several papers run genuinely different cohorts — different induced models, sexes, or co-manipulations (e.g., Escribano's intact / ovariectomized / DMSO cohorts; Papadakakis's control-reared vs maternal-separation cohorts) — where attrition, baseline balance, or design adequacy can differ. Assessing per cohort captures that, and lets the review drop an individual weak cohort in sensitivity analysis instead of discarding a whole study.

### Cohorts that share animals

Some roster cohorts reuse the same animals against two control conditions (e.g., a `silence_music` and a `whitenoise_music` cohort that share the music arm). Their study-level **and** most cohort-level items will be identical by construction. That is expected — rate each as its own row; do not collapse them.

---

## 4. Non-negotiable extraction rules

1. **Evidence first.** Every code must include a compact supporting quotation or faithful paraphrase and a precise location (page, table, figure, supplement, or section).
2. **No inference from silence.** Absence of reporting is not evidence that a method was used.
3. **Differentiate "No" from "Unclear."**
   - For **QoR/MQ** items, use `No` when reporting is seriously insufficient or the relevant feature is absent; use `Partly` when the report has some useful information but lacks required detail.
   - For **RoB** items, use `Unclear` when the paper does not provide enough information to judge the feature. Use `No` only when a potentially biasing practice is explicitly reported or clearly demonstrated.
4. **Do not upgrade a rating based on a paper's conclusions, prestige, statistical significance, or peer-reviewed status.**
5. **Quote the methods/results, not the discussion.** A discussion statement such as "animals were carefully randomized" does not establish the allocation method unless the methods support it.
6. **Record uncertainty explicitly.** When two readings are plausible, retain the more conservative provisional code and explain the ambiguity.
7. **Use `NA` only where this protocol explicitly permits it.** `NA` means genuinely inapplicable, not merely unreported.
8. **Keep intervention fidelity separate from effect size.** A large or significant music effect does not demonstrate a good-quality intervention.
9. **Never invent a source.** Only assess reports that are actually supplied as sources. Do not fabricate a study, a row, or an evidence quotation to reach a target count.

---

## 5. Coverage protocol — assess all 49 cohorts (READ THIS FIRST)

NotebookLM tends to summarize a few sources, merge them, or truncate long output. This review requires the opposite: **every cohort in the frozen roster is assessed individually and none is dropped.** Follow this protocol exactly.

### 5.1 The frozen cohort roster (authoritative — do not regenerate)

The cohorts are fixed by the meta-analysis extraction and supplied as `crime_q_cohort_roster.csv` (added to the notebook as a source) and reproduced below. **There are exactly 49 cohorts across 20 studies. Assess each `Cohort_ID` once. Do not derive cohorts from the PDFs.** Match each roster cohort to its study PDF using `Study_ID` and the `Contrast(s)` / `Co-manipulation` scope. If you cannot find a PDF for a roster cohort, still create its row and flag it in `Human_Review_Priorities`; never silently drop it and never invent a cohort that is not in the roster.

**Frozen cohort roster (49 cohorts):**

| Index | Study_ID | Cohort_ID | Contrast(s) | Co-manipulation | Assays |
|---|---|---|---|---|---|
| 1 | Camargo_2013_PSYN | Camargo_2013_PSYN_ex001 | 0.silence_0.music | None | Elevated Plus Maze; Open Field Test |
| 2 | Chen_2019_BIOMEDRI | Chen_2019_BIOMEDRI_ex001 | control.prior_music.prior; control.after | None / fear conditioning | Elevated Plus Maze; Open Field Test |
| 3 | Chen_2019_BIOMEDRI | Chen_2019_BIOMEDRI_ex002 | control.prior_music.prior; control.after | None / fear conditioning | Elevated Plus Maze; Open Field Test |
| 4 | Cheng_2024_HLYN | Cheng_2024_HLYN_ex001 | CUMS_light | CUMS | Sucrose Preference Test; Forced Swim Test |
| 5 | Cheng_2024_HLYN | Cheng_2024_HLYN_ex002 | CUMS_Classical | CUMS | Sucrose Preference Test; Forced Swim Test |
| 6 | Cheng_2024_HLYN | Cheng_2024_HLYN_ex003 | CUMS_Atonal | CUMS | Sucrose Preference Test; Forced Swim Test |
| 7 | Cheng_2024_HLYN | Cheng_2024_HLYN_ex004 | CUMS_ROCK | CUMS | Sucrose Preference Test; Forced Swim Test |
| 8 | Chikahisa_2007_BBR | Chikahisa_2007_BBR_ex001 | SILENCE_MUSIC | None | Elevated Plus Maze |
| 9 | Chikahisa_2007_BBR | Chikahisa_2007_BBR_ex002 | WHITENOISE_MUSIC | None | Elevated Plus Maze |
| 10 | Chikahisa_2007_BBR | Chikahisa_2007_BBR_ex003 | SILENCE_MUSIC | None | Elevated Plus Maze |
| 11 | Chikahisa_2007_BBR | Chikahisa_2007_BBR_ex004 | WHITENOISE_MUSIC | None | Elevated Plus Maze |
| 12 | Chikahisa_2007_BBR | Chikahisa_2007_BBR_ex005 | SILENCE_MUSIC | Co-manipulation | Open Field Test; Elevated Plus Maze |
| 13 | Chikahisa_2007_BBR | Chikahisa_2007_BBR_ex006 | WHITENOISE_MUSIC | Co-manipulation | Open Field Test; Elevated Plus Maze |
| 14 | Chikahisa_2007_BBR | Chikahisa_2007_BBR_ex007 | SILENCE_MUSIC | Co-manipulation | Open Field Test; Elevated Plus Maze |
| 15 | Chikahisa_2007_BBR | Chikahisa_2007_BBR_ex008 | WHITENOISE_MUSIC | Co-manipulation | Open Field Test; Elevated Plus Maze |
| 16 | Escribano_2014_APPANBSC | Escribano_2014_APPANBSC_ex001 | SILENCE_MUSIC | None | Elevated Plus Maze; Light-Dark Box |
| 17 | Escribano_2014_APPANBSC | Escribano_2014_APPANBSC_ex002 | WHITE.NOISE_MUSIC | None | Elevated Plus Maze; Light-Dark Box |
| 18 | Escribano_2014_APPANBSC | Escribano_2014_APPANBSC_ex003 | SILENCE_MUSIC | Ovariectomized | Elevated Plus Maze; Light-Dark Box |
| 19 | Escribano_2014_APPANBSC | Escribano_2014_APPANBSC_ex004 | WHITE.NOISE_MUSIC | Ovariectomized | Elevated Plus Maze; Light-Dark Box |
| 20 | Escribano_2014_APPANBSC | Escribano_2014_APPANBSC_ex007 | SILENCE_MUSIC | DMSO (vehicle) | Elevated Plus Maze; Light-Dark Box |
| 21 | Escribano_2014_APPANBSC | Escribano_2014_APPANBSC_ex008 | WHITE.NOISE_MUSIC | DMSO (vehicle) | Elevated Plus Maze; Light-Dark Box |
| 22 | Flores_2018_NP | Flores_2018_NP_ex001 | NH-NoPAS/FST-NoPAS_NH-NoPAS/FST+PAS | None | Forced Swim Test |
| 23 | Flores_2018_NP | Flores_2018_NP_ex002 | NH-NoPAS/FST-NoPAS_NH+PAS/FST-NoPAS | None | Forced Swim Test |
| 24 | Flores_2018_NP | Flores_2018_NP_ex003 | NH-NoPAS/FST-NoPAS_NH+PAS/FST+PAS | None | Forced Swim Test |
| 25 | Flores_2018_NP | Flores_2018_NP_ex004 | ENR-NoPAS/FST-NoPAS_ENR-NoPAS/FST+PAS | Environmental enrichment | Forced Swim Test |
| 26 | Flores_2018_NP | Flores_2018_NP_ex005 | ENR-NoPAS/FST-NoPAS_ENR+PAS/FST-NoPAS | Environmental enrichment | Forced Swim Test |
| 27 | Flores_2018_NP | Flores_2018_NP_ex006 | ENR-NoPAS/FST-NoPAS_ENR+PAS/FST+PAS | Environmental enrichment | Forced Swim Test |
| 28 | Freitas_2020_ECNE | Freitas_2020_ECNE_ex001 | IENM_IECM | None | Open Field Test; Elevated Plus Maze |
| 29 | Freitas_2020_ECNE | Freitas_2020_ECNE_ex002 | EENM_EECM | Environmental enrichment | Open Field Test; Elevated Plus Maze |
| 30 | Fu_2023_TRANSPSY | Fu_2023_TRANSPSY_ex001 | control_music | None | Open Field Test; Novelty Suppressed Feeding |
| 31 | Fu_2023_TRANSPSY | Fu_2023_TRANSPSY_ex002 | CUMS_CUMS+MUSIC | Maternal separation | Open Field Test; Novelty Suppressed Feeding |
| 32 | Fu_2025_TRANSPSY | Fu_2025_TRANSPSY_ex001 | SHAM_SHAM+MUSIC | None | Open Field Test; Forced Swim Test |
| 33 | Krishnamurthy_2025_INDIANJTRADITKNOW | Krishnamurthy_2025_INDIANJTRADITKNOW_ex001 | CUMS_CUMS+MUSIC | CUMS | Elevated Plus Maze; Sucrose Preference Test |
| 34 | Li_2010_BR | Li_2010_BR_ex001 | wild.ambient_wild.music; wild.wn_wild.music | None | Open Field Test; Elevated Plus Maze |
| 35 | Li_2010_BR | Li_2010_BR_ex002 | wild.ambient_wild.music; wild.wn_wild.music | None | Open Field Test; Elevated Plus Maze |
| 36 | Milbratz_2017_ALN | Milbratz_2017_ALN_ex001 | CG_MG | Placebo (starch) | Open Field Test |
| 37 | Milbratz_2017_ALN | Milbratz_2017_ALN_ex002 | CPG_CPMG | Cocoa powder | Open Field Test |
| 38 | Niehues_2011_BCNEURO | Niehues_2011_BCNEURO_ex001 | SILENCE_MUSIC | None | Elevated Plus Maze; Open Field Test |
| 39 | Pangemanan_2024_PHJ | Pangemanan_2024_PHJ_ex001 | CUMS_CUMS+MUSIC | CUMS | Sucrose Preference Test |
| 40 | Papadakakis_2019_BBR | Papadakakis_2019_BBR_ex001 | CGambient.noise_CGMozart | Control-reared | Elevated Plus Maze; Forced Swim Test |
| 41 | Papadakakis_2019_BBR | Papadakakis_2019_BBR_ex002 | MSambient.noise_MSMozart | Maternal separation | Elevated Plus Maze; Forced Swim Test |
| 42 | Ren_2024_ASEAN | Ren_2024_ASEAN_ex001 | WT_HH (hip-hop) | None | Sucrose Preference Test; Tail Suspension Test |
| 43 | Ren_2024_ASEAN | Ren_2024_ASEAN_ex002 | WT_HM (heavy metal) | None | Sucrose Preference Test; Tail Suspension Test |
| 44 | Rizzolo_2021_CC | Rizzolo_2021_CC_ex001 | 19WN_19_M; 23_WN_23_M | None | Elevated Plus Maze |
| 45 | Saghari_2021_BIOINTERFACE | Saghari_2021_BIOINTERFACE_ex001 | control_music | None | Open Field Test |
| 46 | Saghari_2021_BIOINTERFACE | Saghari_2021_BIOINTERFACE_ex002 | ptsd_ptsd.music | PTSD | Open Field Test |
| 47 | Sampaio_2017_PSYNEURO | Sampaio_2017_PSYNEURO_ex001 | control_music.therapy | None | Open Field Test; Elevated Plus Maze |
| 48 | Sampaio_2017_PSYNEURO | Sampaio_2017_PSYNEURO_ex002 | control_music.therapy | None | Open Field Test; Elevated Plus Maze |
| 49 | Terzioglu_2020_CMJ | Terzioglu_2020_CMJ_ex001 | control_Classical; control_rock; control_sufi | None | Tail Suspension Test |

The untruncated roster (full contrast strings, species, strain, sex, music type, control, all assays) is in `crime_q_cohort_roster.csv`; use it as the authoritative scope reference.

### 5.2 Step 1 — Create one complete Google Sheet (primary deliverable)

Create the primary deliverable in **one direct Google Sheet creation task**: one Google Sheet named `MUSIC-CRIME-Q_RoB_assessment`. The Google Sheet itself is the sole canonical output. **Create the Google Sheet directly in NotebookLM Studio. Do not display any appraisal table in chat. Do not create a Markdown table, TSV, CSV, text table, spreadsheet copy, or second data artifact.**

The Google Sheet must contain exactly three tabs, in this order:

1. `Source_Coverage`
2. `RoB_Matrix_cohort`
3. `Human_Review_Priorities`

Create all three tabs in the same Google Sheet. Fill the complete assessment for all 49 roster cohorts. When the Google Sheet is complete, provide its clickable Google Sheet link as the only chat response.

### 5.3 Step 2 — Optional evidence tab

The primary Google Sheet contains only `Source_Coverage`, `RoB_Matrix_cohort`, and `Human_Review_Priorities`. Add `Item_Evidence` only when explicitly requested after review of the primary Google Sheet. When requested, add it as a fourth tab in the **same Google Sheet**, with exactly 23 evidence rows per cohort and ratings identical to `RoB_Matrix_cohort`. Do not recreate, rewrite, duplicate, or replace the three primary tabs.

### 5.4 Coverage rules

- **One row per `Cohort_ID`.** `RoB_Matrix_cohort` and `Source_Coverage` must each contain exactly 49 rows — one per roster cohort.
- **Never merge two cohorts into one row** or write "same as the previous cohort." Even cohorts that share animals get their own row (Section 3).
- **Never omit a cohort because its study is hard to read, short, non-English, or poorly reported.** A poorly reported cohort still gets a full row, with `No`/`Unclear`/`NR` codes and a `Human_Review_Priorities` entry.
- **Direct-file completeness rule:** do not attach a partial Google Sheet. Before finalizing the file, verify that `RoB_Matrix_cohort` and `Source_Coverage` each contain exactly 49 rows, corresponding one-to-one with the frozen roster.
- **Single-artifact rule:** create one Google Sheet only. Do not create batches, intermediate spreadsheets, copied tables, or a second data artifact.

---

## 6. Response categories

### QoR and MQ items

- `Yes` — the requirement is fully met under the operational rule below.
- `Partly` — some relevant information or adequate elements are present, but one or more pre-specified details are missing or uncertain.
- `No` — the feature is absent, seriously inadequate, or the methods are too poorly described to support the item.
- `NA` — only where expressly allowed below.

### RoB items

- `Yes` — the study was apparently free of the specified source of bias, with supporting evidence.
- `No` — the study clearly had the specified bias risk or a clearly problematic practice.
- `Unclear` — reporting does not permit a defensible judgment.
- `NA` — only when the item cannot apply to the design, as specified below.

**Important:** In RoB items, `Yes` means *apparently free from the bias*, not merely that the paper mentions the topic.

---

## 7. Required study-design summary before rating items

For every `Cohort_ID`, first extract the following information. Use `NR` for not reported.

| Field | What to extract |
|---|---|
| Full citation / DOI | Study identity and publication year |
| Species and strain/stock | Scientific/common name and strain, stock, or line |
| Sex | Female, male, mixed, sex not reported, or developmental stage where sex was not determined |
| Age/life stage and body mass | At exposure start and/or testing, with units |
| Induced model | None/innate behaviour, or stress/depression/anxiety induction method and timing |
| Music condition | Music type/title/composer/genre/file where stated |
| Acoustic delivery | Speaker/headphone/device, distance/location, room/cage arrangement, and whether sound pressure level (dB/SPL) was measured |
| Exposure schedule | Start age, session duration, sessions/day, days/week, total duration, timing relative to behavioural tests |
| Control condition | Silence, ambient room noise, sham speaker, white noise, alternative sound, or other control |
| Housing and exposure unit | Animals/cage, cages/group, room allocation, acoustic separation, and the apparent experimental unit (animal, cage, or room) |
| Allocation | Exact wording and method of assignment to groups |
| Behavioural assays | Assay, outcome, timing/order, and whether scoring was manual or automated |
| Sample sizes | Animals allocated, analysed, and excluded by group; cages/rooms where reported |
| Outcome-specific notes | Assay-specific exclusions, blinding, or deviations |

---

## 8. Adapted CRIME-Q item codebook

### 1X — Peer review (QoR)

**Question:** Did the paper undergo peer review before publication?

- `Yes`: The source is a full article in a scholarly journal.
- `No`: The source is clearly a preprint, thesis, conference abstract, unpublished manuscript, or other non-peer-reviewed report.
- Do not infer peer-review status from author affiliation alone.

---

### 2X — Bench-top/laboratory work: reporting (QoR)
### 2Y — Bench-top/laboratory work: technical quality (MQ)

**Adaptation for this review:** These items are normally irrelevant to a music-exposure behavioural experiment because no bench-top procedure is used to establish the animal model.

- Code `NA` for both items when there is no cell culture, surgery, implantation, genetic-model production, compound preparation, or other bench-top procedure central to the study.
- Code the items only when such work directly establishes the study model or intervention and is material to the behavioural experiment.
- Record the reason for `NA`: `No bench-top/model-establishment procedure relevant to acoustic music-exposure experiment.`

This is a transparent, pre-specified deviation from the original response options and must be documented in the final methods/supplement.

---

### 3X — Animals: reporting (QoR)

**Question:** Are experimental animals sufficiently described?

Assess: species, strain/stock, sex, age or developmental stage, body mass where relevant, and supplier/breeding source where reported.

- `Yes`: Species, strain/stock, sex, and age/life stage are stated, plus body mass **or** supplier/breeding source. Group sizes are identifiable.
- `Partly`: Some but not all key descriptors are reported; for example, species and strain but no sex or age; or age and sex but no strain/stock.
- `No`: Animals cannot be confidently identified beyond a generic label such as "rats" or "mice," or animal characteristics are seriously insufficient to interpret the experiment.

Do not penalize an early-life experiment merely because individual sex cannot yet be determined; record the developmental stage and whether sexing was possible.

---

### 3Y — Animals: technical quality (MQ)

**Question:** Were animal characteristics comparable between groups and appropriate for the intended behavioural experiment?

- `Yes`: Music and control groups are demonstrably comparable in species/strain, sex, developmental stage/age, and relevant baseline body mass or health; the animal model is appropriate for the stated behavioural assay and any induced condition.
- `Partly`: Groups appear likely comparable (e.g., same cohort/strain/age) but baseline balance, eligibility, or model appropriateness is incompletely documented.
- `No`: A relevant baseline imbalance is reported and not addressed; groups use materially different animal types without a justified design; or the stated model/animals are plainly unsuitable for the experimental question.

Do not treat a missing baseline table as evidence of imbalance. Usually it warrants `Partly`, not `No`.

---

### 3Z — Selection bias: baseline characteristics (RoB; SYRCLE item 2)

**Question:** Were relevant baseline characteristics balanced between music and control groups?

Relevant characteristics include sex, age/life stage, strain, body mass, induced-condition severity, litter origin where relevant, and baseline behavioural measurement where measured.

- `Yes`: Arm-specific baseline information demonstrates balance, or a clearly described matching/blocking/litter-balancing procedure ensures comparable groups.
- `No`: A relevant imbalance is shown or reported and is not addressed.
- `Unclear`: No arm-specific baseline information or balancing procedure is reported.
- `NA`: Only one group is genuinely relevant to the analysis; this should be rare in eligible controlled experiments.

---

### 4Y — Sample-size calculation (MQ)

**Question:** Did the study report an appropriate *a priori* sample-size calculation?

- `Yes`: An *a priori* calculation states enough information to assess it (e.g., target power, alpha, expected effect/variance, and planned group size) and appears appropriate for the primary comparison.
- `Partly`: A calculation or power rationale is mentioned but key assumptions are missing, it is retrospective/post hoc, or applicability to the music comparison is uncertain.
- `No`: No sample-size or power calculation is reported.

A statement that the sample size followed prior studies is not a sample-size calculation.

---

### 5X — In vivo design and performance: reporting (QoR)

**Question:** Is the music-exposure experiment described sufficiently for replication?

For `Yes`, the paper must report enough information to reconstruct the core intervention and comparison:

1. music stimulus (type/title/genre/file, where available);
2. delivery hardware and arrangement (speaker/device, location/distance, cage/room setup);
3. sound level or other intensity information, including how measured where reported;
4. exposure start, session length, frequency, total duration, and timing relative to tests;
5. control auditory condition;
6. animal housing/exposure arrangement sufficient to assess what animals could hear;
7. behavioural assay procedure and outcome measurement; and
8. induced-condition protocol and timing, if applicable.

- `Yes`: All core elements are reported with sufficient clarity to reproduce the study.
- `Partly`: The design is broadly understandable but one or more core elements are missing (commonly sound level, speaker/cage arrangement, control condition, or test timing).
- `No`: The report does not allow a reader to identify a reproducible music-versus-control experiment or outcome procedure.

Always list each required element as reported or `NR`, even when the overall rating is `Yes`.

---

### 5Y — In vivo design and performance: technical quality (MQ)

**Question:** Does the described music-exposure design appear technically feasible for the stated aim?

Evaluate only what is reported. Consider acoustic delivery, exposure fidelity, separation of music and control conditions, timing, behavioural assay implementation, and the likely experimental unit.

- `Yes`: The described design can plausibly deliver distinct music and control exposures; exposure conditions are coherent with the aim; no obvious acoustic cross-contamination, fatal timing problem, pseudoreplication, or assay-design flaw is evident.
- `Partly`: The design is plausible but essential information about sound verification, acoustic separation, cage/room replication, or exposure fidelity is incomplete.
- `No`: A clear technical problem threatens interpretability, such as controls demonstrably hearing the music condition, no meaningful control condition, a major mismatch between exposure and outcome timing, or an apparent cage/room-level intervention analysed as independent individual-level treatment without accounting for clustering.

Do not use subjective judgments about whether a particular genre of music "should work."

---

### 5Z(1) — Selection bias: sequence generation (RoB; SYRCLE item 1)

**Question:** Was allocation to music and control groups generated by an appropriate random method?

- `Yes`: The method is described and plausibly random (e.g., computer random number generator, random-number table, drawing lots) or an equivalent pre-specified random process.
- `No`: Allocation was clearly non-random (e.g., alternation, order of arrival, convenience, investigator choice).
- `Unclear`: The paper says only "randomly assigned" without method, or provides no allocation details.
- `NA`: Only for a non-interventional design; usually not applicable here.

---

### 5Z(2) — Performance bias: random housing (RoB; SYRCLE item 4)

**Question:** Were animals randomly housed or otherwise protected from systematic cage/position effects?

- `Yes`: The report describes random cage/room placement, counterbalancing, rotation, or an equivalent procedure that addresses housing position and acoustic environment.
- `No`: Housing/position was clearly systematic in a way likely confounded with the music condition (e.g., all music cages adjacent to speaker and all controls in another fixed position), without mitigation.
- `Unclear`: Housing arrangement or allocation is not reported sufficiently.
- `NA`: Only when housing position cannot affect the experiment, which is unlikely for acoustic exposure studies.

---

### 5Z(3) — Detection bias: random outcome assessment (RoB; SYRCLE item 6)

**Question:** Were animals assessed according to a pre-specified, unbiased selection rule?

- `Yes`: All allocated animals were tested at a pre-specified time, or a random/pre-specified sample-selection rule is described.
- `No`: Animals were selected for testing or analysis based on post-allocation response, survival, treatment response, or another potentially biased criterion.
- `Unclear`: It is not possible to tell who was assessed or how animals were selected for assessment.
- `NA`: Only if no animal-level outcome assessment is relevant.

---

### 6X — Compliance with animal-welfare regulations (QoR)

**Question:** Did the study report compliance with animal-welfare regulations?

- `Yes`: Ethics/animal-care approval and/or institutional/national guideline compliance is explicitly reported.
- `Partly`: A general welfare statement is present but approval body, protocol, or guideline details are incomplete.
- `No`: No ethics, animal-care, or welfare-compliance statement is reported.

---

### 7X — Blinding: reporting (QoR)

**Question:** Does the report describe blinding in any relevant phase?

- `Yes`: The report clearly states who was blinded, at what stage, and to which condition(s), especially for outcome assessment.
- `Partly`: It uses an unqualified term such as "blinded" or describes only limited blinding without enough detail to assess it.
- `No`: No blinding is described.

Automated tracking software is not, by itself, evidence of blinding. Record automation separately in the evidence notes.

---

### 7Z(1) — Performance bias: blinding of caregivers/researchers (RoB; SYRCLE item 5)

**Question:** Were caregivers and researchers conducting the intervention blinded to group assignment where feasible?

- `Yes`: Specific procedures prevented staff who handled animals or delivered treatment from knowing group assignment, or ensured equivalent handling with coded conditions.
- `No`: The report explicitly indicates that caregivers/researchers knew group assignment and this could affect handling or treatment.
- `Unclear`: No adequate information is provided.
- `NA`: Only where blinding is genuinely impossible and no handling-related influence is plausible; explain carefully. Do not use `NA` merely because the intervention is music.

---

### 7Z(2) — Allocation bias: allocation concealment (RoB; SYRCLE item 3)

**Question:** Could the person assigning animals to groups foresee the next assignment?

- `Yes`: Allocation was concealed (e.g., central/randomized coded allocation, sequential opaque sealed envelopes, independent allocator).
- `No`: Assignment was predictable or the allocator could knowingly influence group placement.
- `Unclear`: Allocation concealment is not described. Randomization alone does not establish concealment.
- `NA`: Only for non-interventional designs.

---

### 7Z(3) — Detection bias: blinding of outcome assessors (RoB; SYRCLE item 7)

**Question:** Were outcome assessors blinded to music/control assignment?

- `Yes`: The paper explicitly states that assessors, video coders, or analysts were blinded; or data were coded/masked before outcome extraction in a way that prevents condition knowledge.
- `No`: Assessors were explicitly unblinded and outcomes involved a judgment-sensitive assessment.
- `Unclear`: Assessor blinding is not reported. Automated tracking alone does not justify `Yes` unless masking/coding of treatment condition is also described.
- `NA`: Only for an outcome with no assessor-dependent stage; explain why.

---

### 8X — Congruency between methods and results (QoR)

**Question:** Are reported methods and results coherent and transparent?

- `Yes`: Outcomes, group labels, sample sizes, timing, and analyses in results correspond to the methods; all reported results can be traced to described procedures.
- `Partly`: Minor discrepancies, incomplete outcome-method descriptions, or partial traceability occur, but the primary comparison remains interpretable.
- `No`: Major outcomes/analyses appear in results without corresponding methods, group identities or denominators are inconsistent, or major method-result contradictions occur.

---

### 8Z(1) — Attrition bias: incomplete outcome data (RoB; SYRCLE item 8)

**Question:** Were outcome data complete, with exclusions and attrition adequately handled?

- `Yes`: Numbers allocated, analysed, and excluded are clear by group and outcome; reasons are given; or evidence indicates all allocated animals contributed to the relevant outcome.
- `No`: Missing/excluded animals are clearly unequal, outcome-related, inadequately explained, or likely to bias the comparison.
- `Unclear`: Denominators, exclusions, or reasons are insufficiently reported.

Do not label attrition `No` merely because any animal died or was excluded. The problem is incomplete or biased handling/reporting.

---

### 8Z(2) — Reporting bias: selective outcome reporting (RoB; SYRCLE item 9)

**Question:** Were prespecified or expected outcomes fully reported?

- `Yes`: A protocol/registration is available and outcomes match it; **or**, without a protocol, the methods clearly list outcomes and the results provide all corresponding group-level results.
- `No`: A stated/expected key outcome is missing, outcome reporting is selectively incomplete, or outcome switching is evident.
- `Unclear`: No protocol is available and the report does not permit a confident comparison between intended and reported outcomes.

Absence of a protocol alone is not enough for `No`.

---

### 9X — Presentation of limitations (QoR)

**Question:** Did the authors acknowledge study limitations relevant to interpretation or generalizability?

- `Yes`: The paper contains a substantive limitations discussion linked to the music experiment, animal model, behavioural measures, or design.
- `Partly`: It makes only a generic or brief limitation statement.
- `No`: No limitations are discussed.

---

### 10X — Conflict-of-interest statement (QoR)

**Question:** Did the paper include a conflict-of-interest/competing-interests declaration?

- `Yes`: A formal statement is present, including a declaration of no conflicts.
- `No`: No such statement appears in the paper or supplied supplement.

---

### 10Z — Other bias: inappropriate funder or commercial influence (RoB; adapted SYRCLE item 10)

**Question:** Was the study apparently free from inappropriate influence by a funder or a party with an interest in the music intervention/equipment?

- `Yes`: A conflict-of-interest statement declares no relevant conflicts and no inappropriate sponsor role is evident; or the funder had no role in design, conduct, analysis, or publication.
- `No`: A funder/company with a relevant commercial or other interest controlled or materially influenced design, conduct, analysis, or reporting without adequate safeguards; or a direct undeclared/acknowledged conflict clearly threatens independence.
- `Unclear`: Conflict and sponsor-role information is absent or insufficient.

Academic/public funding is not a bias signal by itself. Do not infer inappropriate influence from commercial provision of speakers/software alone unless the paper indicates a problematic role.

---

## 9. Required NotebookLM Google Sheet output

### 9.1 Canonical deliverable — one Google Sheet

Create one Google Sheet named `MUSIC-CRIME-Q_RoB_assessment` directly in NotebookLM Studio. This Google Sheet is the only data deliverable. It must contain exactly three tabs, in this order: `Source_Coverage`, `RoB_Matrix_cohort`, and `Human_Review_Priorities`.

Do not render an assessment table in chat. Do not create a Markdown table, TSV, CSV, text table, copied spreadsheet, or any second data artifact. Complete the assessment directly inside the Google Sheet. When complete, return only the clickable Google Sheet link in chat.

### 9.2 Google-Sheet-wide rules

- Use one header row and one record per row. Do not merge cells.
- Use the exact tab names, column names, and item codes below.
- Preserve missing information as `NR` (not reported) where the relevant table requests it; do not leave required fields blank.
- In every `Evidence` field, provide a compact direct quotation or a faithful, source-grounded paraphrase. Never manufacture a quotation.
- In every `Location` field, cite the PDF location precisely, such as `p. 3, Methods, Animals`, `p. 5, Fig. 2 legend`, or `Supplementary Methods, p. 2`.
- Use semicolons to separate multiple assays or details within a cell.
- Do not generate an overall risk-of-bias score, a global high/low-quality judgment, an exclusion recommendation, or an inference about intervention efficacy.
- Every rating in `RoB_Matrix_cohort` must be stored as literal text. Never use numbers, Boolean values, formulas, scores, dropdown encodings, or blank rating cells.

### 9.3 Study-level vs cohort-sensitive items (propagation rule)

Most CRIME-Q items describe the **paper/experiment as reported** and are identical for every cohort of the same `Study_ID`. Fill these the same across a study's cohorts unless the paper explicitly reports a cohort-specific procedure:

- **Study-level (propagate within a study):** `1X` (peer review), `2X`/`2Y` (bench-top; `NA` here), `3X` (animal reporting), `4Y` (sample-size calculation), `5Z(1)` (sequence generation), `6X` (welfare/ethics), `7X` (blinding reporting), `7Z(2)` (allocation concealment), `9X` (limitations), `10X` (conflict-of-interest statement), and `10Z` (funder influence).
- **Cohort-sensitive (judge per cohort):** `3Y` (group comparability), `3Z` (baseline balance), `5X`/`5Y` (design reporting/feasibility), `5Z(2)` (random housing), `5Z(3)` (random outcome assessment), `7Z(1)` (caregiver blinding), `7Z(3)` (assessor blinding), `8X` (method–result congruency), `8Z(1)` (attrition), `8Z(2)` (selective reporting).

A normally study-level item may differ when the paper explicitly describes a cohort-specific procedure. Follow the evidence; do not manufacture variation merely because the unit of assessment is the cohort.

---

### Tab 1 — `Source_Coverage` (one row per cohort)

| Index | Study_ID | Cohort_ID | Source | Contrast(s) | Matched PDF (Y/N) | Assessed (Y/N) | Notes |
|---|---|---|---|---|---|---|---|

- `Index` is the roster index (1…49). Copy `Study_ID`, `Cohort_ID`, and `Contrast(s)` from the frozen roster (Section 5.1).
- `Matched PDF` records whether a source PDF for that cohort's study was found.
- `Assessed` must be `Y` for every row.
- The tab must contain exactly 49 rows, one for each roster cohort.

---

### Tab 2 — `RoB_Matrix_cohort` (primary deliverable: wide, 49 rows × 23 item columns)

Wide format. **One row per cohort** (`Cohort_ID`) and **one column per CRIME-Q item** — 23 item columns in the fixed order below — each holding only the provisional rating. With two leading ID columns, each row is `Study_ID, Cohort_ID` followed by the 23 ratings. This tab must contain a row for **every** cohort in the frozen roster — exactly **49 rows**.

| Study_ID | Cohort_ID | 1X | 2X | 2Y | 3X | 3Y | 3Z | 4Y | 5X | 5Y | 5Z(1) | 5Z(2) | 5Z(3) | 6X | 7X | 7Z(1) | 7Z(2) | 7Z(3) | 8X | 8Z(1) | 8Z(2) | 9X | 10X | 10Z |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

Allowed cell values follow Section 6:

- QoR/MQ: `Yes`, `Partly`, `No`, `NA`
- RoB: `Yes`, `No`, `Unclear`, `NA`

Every cell must be filled. Do not leave a rating cell blank.

---

### Tab 3 — `Human_Review_Priorities`

One row for each issue that requires human attention. Use a proper table, not prose.

| Study_ID | Cohort_ID | Category | Priority | Issue requiring review | Related item(s) | Evidence / location | Needed human decision |
|---|---|---|---|---|---|---|---|

Allowed `Category` values:

- `Missing information materially preventing assessment`
- `Potentially important design or bias concern`
- `Item needing human adjudication`

Allowed `Priority` values are `High`, `Moderate`, or `Low`.

When a cohort has no qualifying issue, create one row with `Category = None identified`, `Priority = NA`, and `Issue requiring review = No material review priority identified from the supplied report.` Every one of the 49 cohorts must appear at least once in this tab.

---

### Optional Tab 4 — `Item_Evidence`

Add this tab only when explicitly requested after review of the primary Google Sheet. For each `Cohort_ID`, create exactly 23 rows in the codebook item order and use these columns:

| Study_ID | Cohort_ID | Item | Construct | Provisional rating | Evidence | Location | Operational rationale | Uncertainty / notes |
|---|---|---|---|---|---|---|---|---|

Every `Provisional rating` must match the corresponding `RoB_Matrix_cohort` rating exactly.

## 10. Direct-Google-Sheet prompt for NotebookLM

Select **all primary-study PDFs**, supplied supplements, this manual, the item-level codebook (`CRIME-Q_Music_RoB_Codebook_v1.8.csv`), the frozen cohort roster (`crime_q_cohort_roster.csv`), and the CRIME-Q paper as sources. Run the following prompt once.

> Create one Google Sheet directly in this NotebookLM Studio, named `MUSIC-CRIME-Q_RoB_assessment`.
>
> The Google Sheet is the only deliverable. Create it directly now. Do not display the appraisal in chat. Do not create a Markdown table, TSV, CSV, text table, copied spreadsheet, or any second data artifact.
>
> Follow `CRIME-Q_Music_RoB_NotebookLM_Extraction_Manual_v1.8.md` exactly. Use `CRIME-Q_Music_RoB_Codebook_v1.8.csv` as the authoritative item-level decision codebook. Assess exactly the 49 cohorts in `crime_q_cohort_roster.csv`. Do not invent, split, merge, omit, or substitute cohorts.
>
> Before assigning ratings, match each unique `Study_ID` to the correct primary-study PDF among the NotebookLM sources. Verify every match from the PDF first page using author, year, title, journal, or DOI; do not use filenames, source order, topic similarity, or guesses. Read the matched PDF's Methods, Results, tables, figures, and supplied supplement before rating its cohorts.
>
> In `Source_Coverage`, write the exact matched NotebookLM PDF source name in `Source`, set `Matched PDF (Y/N)` to `Y`, and write `Verified against PDF first page.` in `Notes`. Use the same matched PDF for cohorts sharing a `Study_ID`.
>
> In this Google Sheet, create exactly these three tabs in this order:
>
> 1. `Source_Coverage` — 49 rows, one for every roster cohort, with columns `Index, Study_ID, Cohort_ID, Source, Contrast(s), Matched PDF (Y/N), Assessed (Y/N), Notes`.
> 2. `RoB_Matrix_cohort` — 49 rows, one per `Cohort_ID`, with these 25 columns in this exact order: `Study_ID, Cohort_ID, 1X, 2X, 2Y, 3X, 3Y, 3Z, 4Y, 5X, 5Y, 5Z(1), 5Z(2), 5Z(3), 6X, 7X, 7Z(1), 7Z(2), 7Z(3), 8X, 8Z(1), 8Z(2), 9X, 10X, 10Z`.
> 3. `Human_Review_Priorities` — at least one row for every cohort; add separate rows for distinct issues. Where no material issue is identified, write `None identified` in `Category`, `NA` in `Priority`, and `No material review priority identified from the supplied report.` in `Issue requiring review`.
>
> For every matrix item, use the codebook's exact response options, assessment level, NA rule, and operational guidance. Apply study-level propagation only for codebook items marked `Study-level`; judge cohort-sensitive items using the roster's `Contrast(s)` and `Co-manipulation` scope. Every matrix cell must contain an exact permitted literal codebook label; never use numbers, Boolean values, formulas, scores, dropdown values, blanks, or alternative labels.
>
> Do not calculate an overall score, make a global paper-quality label, recommend exclusion, or infer music efficacy.
>
> Before completing the Google Sheet, verify that `Source_Coverage` and `RoB_Matrix_cohort` each contain all 49 roster cohorts exactly once; every `Source_Coverage` row names a matched PDF source; every cohort has `Matched PDF (Y/N) = Y` and `Assessed (Y/N) = Y`; headers are in the required order; every matrix cell is an exact item-permitted codebook label; and every cohort appears at least once in `Human_Review_Priorities`.
>
> Reply in chat with only the clickable link to the completed Google Sheet.

### Optional evidence-tab extension

After the primary Google Sheet has been reviewed, use this separate prompt only when evidence rows are required:

> Open the existing Google Sheet `MUSIC-CRIME-Q_RoB_assessment` and add one tab named `Item_Evidence`. Do not change the three existing tabs. For each of the 49 existing `Cohort_ID`s, add exactly 23 rows in the manual's item order, with columns `Study_ID, Cohort_ID, Item, Construct, Provisional rating, Evidence, Location, Operational rationale, Uncertainty / notes`. Every `Provisional rating` must match the corresponding cell in `RoB_Matrix_cohort` exactly. Preserve every rating as literal text. Reply with only the clickable link to the updated Google Sheet.

---

## 11. Quality control and study-level reporting

### 11.1 QC after extraction

1. Confirm `Source_Coverage` and `RoB_Matrix_cohort` each contain exactly **49 cohort rows**. Investigate any missing cohort before proceeding.
2. A reviewer checks all evidence locations in `Item_Evidence` and changes any unsupported provisional code; corrections must be propagated to `RoB_Matrix_cohort`.
3. A second reviewer independently completes the same form without seeing the first reviewer's ratings.
4. Compare item-level agreement before consensus; preserve both initial ratings and the final consensus rating.
5. Log all adaptations, especially `NA` for 2X/2Y.

### 11.2 Reporting: cohort distribution within each study

The assessment unit is the cohort, but results are **described per study by reporting the distribution of its cohorts' ratings** — not collapsed to a single per-study verdict and **never summed into a total score**. For each study and each item, report the spread across its cohorts (e.g., Escribano 8Z(1): "4 cohorts `Unclear`, 2 `Yes`"). For study-level items this is trivially one value; for cohort-sensitive items it shows the within-study range. Across the corpus, report each item/domain as a **distribution of cohort ratings** (e.g., % of the 49 cohorts `Yes`/`Unclear`/`No`).

The derived study-level distribution summary is generated deterministically from `RoB_Matrix_cohort` by the helper script `crime_q_rollup.R` (see repo), not by NotebookLM.

### 11.3 Sensitivity analysis: drop cohorts, not studies

Because the meta-analytic variance–covariance matrix now clusters at `Cohort_ID`, pre-specified RoB sensitivity analyses **remove individual high-risk cohorts** (specific `Cohort_ID` rows) rather than excluding whole studies — preserving the well-conducted cohorts that share a paper with a weak one. Pre-specify the critical domains used to flag a cohort (for example, allocation sequence `5Z(1)`, assessor blinding `7Z(3)`, attrition `8Z(1)`, selective reporting `8Z(2)`) before examining results.

---

## 12. References

- Andersen MS, Kofoed MS, Paludan-Müller AS, et al. **CRIME-Q—a unifying tool for critical appraisal of methodological (technical) quality, quality of reporting and risk of bias in animal research.** *BMC Medical Research Methodology.* 2024;24:306. Corrected 2025. https://doi.org/10.1186/s12874-024-02413-0
- Ortega RA, et al. **Music exposure reduces anxiety- and depression-like behavior in rodents: a systematic review and multilevel meta-analysis.**
