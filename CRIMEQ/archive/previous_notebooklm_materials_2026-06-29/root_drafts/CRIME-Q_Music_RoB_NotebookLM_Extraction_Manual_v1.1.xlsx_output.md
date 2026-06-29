# MUSIC-CRIME-Q: NotebookLM Extraction Manual

**Project:** *Music exposure reduces anxiety- and depression-like behavior in rodents: a systematic review and multilevel meta-analysis*  
**Assessment framework:** Adapted CRIME-Q (Critical Appraisal of Methodological [technical] Quality, Quality of Reporting and Risk of Bias in Animal Research)  
**Version:** 1.1 — 19 June 2026

---

## 1. Purpose and scope

Use this document to extract a transparent, study-level critical appraisal from the PDF of each included primary animal study. The assessment is for experiments comparing a **music-exposure condition** with an appropriate **control condition** and measuring anxiety- or depression-like behavioural outcomes in laboratory rodents.

CRIME-Q distinguishes three constructs. Keep them separate:

- **QoR — quality of reporting:** whether the report contains enough information to understand and reproduce the work.
- **MQ — methodological/technical quality:** whether the described experiment appears technically feasible and appropriately implemented.
- **RoB — risk of bias:** whether design or conduct features could systematically distort the estimated music effect.

Do **not** turn the items into a total score, label a paper globally “high” or “low” quality, or recommend excluding studies. CRIME-Q intentionally does not prescribe an overall numerical score. The final review should present item-level results and, if appropriate, pre-specified sensitivity analyses.

This is an **assisted extraction protocol**, not an autonomous final appraisal. NotebookLM must extract evidence and provisional codes; a human reviewer must check every code against the source PDF. Final ratings should be reached by two independent human reviewers, followed by consensus adjudication.

---

## 2. Sources NotebookLM may use

For a given assessment, use only:

1. The primary-study PDF currently being assessed;
2. Its associated supplementary material, appendices, or protocol **only when supplied as a source**;
3. This extraction manual; and
4. The CRIME-Q paper supplied as a source.

Do **not** use review articles, cited papers, author webpages, general knowledge, journal norms, or plausible laboratory practice to fill missing information. A method is **not reported** unless it is stated in the study PDF or its supplied supplement.

---

## 3. Unit of assessment

### Primary unit: independent experiment/cohort

Create one assessment record for each **independent experimental cohort** in which rodents were allocated to a music-exposure and control condition.

Assign IDs as follows:

- `Study_ID`: existing identifier in the meta-analysis database.
- `Experiment_ID`: `Study_ID_E01`, `Study_ID_E02`, etc.
- `Outcome_assays`: all behavioural assays measured in that cohort (e.g., EPM, OFT, FST).

### Split into separate experiments when

- a paper reports clearly separate cohorts, experiments, or replications;
- different animals receive distinct exposure schedules or music conditions;
- a factorial study contains distinct music-versus-control contrasts using different animal groups;
- allocation, housing, music delivery, or animal model differs between cohorts.

### Do not split merely because

- the same animals complete several behavioural assays;
- the same cohort contributes several effect sizes, measures, time points, or directions of the same assay;
- the paper reports several graphs or outcomes from an otherwise identical cohort.

When outcome-level procedures differ within the same cohort (e.g., different assessor blinding, exclusions, or outcome-specific attrition), keep the shared experiment-level rating and record the deviation in `Outcome_specific_notes`.

---

## 4. Non-negotiable extraction rules

1. **Evidence first.** Every code must include a compact supporting quotation or faithful paraphrase and a precise location (page, table, figure, supplement, or section).
2. **No inference from silence.** Absence of reporting is not evidence that a method was used.
3. **Differentiate “No” from “Unclear.”**
   - For **QoR/MQ** items, use `No` when reporting is seriously insufficient or the relevant feature is absent; use `Partly` when the report has some useful information but lacks required detail.
   - For **RoB** items, use `Unclear` when the paper does not provide enough information to judge the feature. Use `No` only when a potentially biasing practice is explicitly reported or clearly demonstrated.
4. **Do not upgrade a rating based on a paper’s conclusions, prestige, statistical significance, or peer-reviewed status.**
5. **Quote the methods/results, not the discussion.** A discussion statement such as “animals were carefully randomized” does not establish the allocation method unless the methods support it.
6. **Record uncertainty explicitly.** When two readings are plausible, retain the more conservative provisional code and explain the ambiguity.
7. **Use `NA` only where this protocol explicitly permits it.** `NA` means genuinely inapplicable, not merely unreported.
8. **Keep intervention fidelity separate from effect size.** A large or significant music effect does not demonstrate a good-quality intervention.

---

## 5. Required study-design summary before rating items

For every `Experiment_ID`, first extract the following information. Use `NR` for not reported.

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

## 7. Adapted CRIME-Q item codebook

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
- `No`: Animals cannot be confidently identified beyond a generic label such as “rats” or “mice,” or animal characteristics are seriously insufficient to interpret the experiment.

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

Do not use subjective judgments about whether a particular genre of music “should work.”

---

### 5Z(1) — Selection bias: sequence generation (RoB; SYRCLE item 1)

**Question:** Was allocation to music and control groups generated by an appropriate random method?

- `Yes`: The method is described and plausibly random (e.g., computer random number generator, random-number table, drawing lots) or an equivalent pre-specified random process.
- `No`: Allocation was clearly non-random (e.g., alternation, order of arrival, convenience, investigator choice).
- `Unclear`: The paper says only “randomly assigned” without method, or provides no allocation details.
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
- `Partly`: It uses an unqualified term such as “blinded” or describes only limited blinding without enough detail to assess it.
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

## 8. Music-specific companion design flag (report separately; do not include in a CRIME-Q score)

### MUSIC-D1 — Acoustic allocation, contamination, and experimental-unit integrity

This is a pre-specified contextual flag for a threat especially relevant to music-exposure experiments. It supplements, rather than replaces, CRIME-Q items 5X, 5Y, and 5Z(2).

**Question:** Does the paper demonstrate that music/control exposure was distinct, acoustically isolated where needed, and analysed at the appropriate experimental unit?

- `Low concern`: Music/control exposure groups are acoustically separated or individually delivered; the number of independent cages/rooms is reported; and analysis/design appropriately accounts for the actual exposure unit.
- `Some concerns`: The set-up appears plausible but cage/room replication, acoustic spillover, or clustering is incompletely reported.
- `High concern`: Controls were likely exposed to the music condition; treatment was delivered at cage/room level but individual animals were analysed as independent without accounting for clustering; or only one exposure unit per condition was used.
- `Unclear`: The sound-delivery, housing, or experimental-unit arrangement is too poorly described to judge.
- `NA`: Only for a demonstrably individually delivered and independently randomized exposure with no shared acoustic environment.

Record why the flag was assigned; do not silently infer sound isolation from different group labels.

---

## 9. Required NotebookLM spreadsheet output

### 9.1 Deliverable

Generate an **Excel-ready report** consisting of exactly three data tables. Do not present a narrative appraisal before, between, or after the tables. The three tables are designed to export from NotebookLM to Google Sheets and then download as an `.xlsx` workbook.

Use these exact table names and worksheet names:

1. `Experiment_Summary`
2. `Item_Assessment`
3. `Human_Review_Priorities`

When exporting, use NotebookLM's **Export to Sheets** function. Each data table should become one worksheet. Then, in Google Sheets, use **File → Download → Microsoft Excel (.xlsx)**. Do not attempt to compress all information into a single worksheet.

### 9.2 Spreadsheet-wide rules

- Use one header row and one record per row. Do not merge cells.
- Use the exact column names and item codes below.
- Preserve missing information as `NR` (not reported), not blank cells and not inferred text.
- In every `Evidence` field, provide a compact direct quotation or a faithful, source-grounded paraphrase. Never manufacture a quotation.
- In every `Location` field, cite the PDF location precisely, such as `p. 3, Methods, Animals`, `p. 5, Fig. 2 legend`, or `Supplementary Methods, p. 2`.
- Do not place a citation marker, explanatory footnote, or multiple records in the same cell when separate rows are required.
- Use semicolons to separate multiple assays, details, or related items within a cell.
- Do not generate an overall risk-of-bias score, a global high/low-quality judgment, an exclusion recommendation, or an inference about intervention efficacy.

### A. Worksheet: `Experiment_Summary`

Create **one row per `Experiment_ID`**.

| Study_ID | Experiment_ID | Cohort / comparison description | Full citation / DOI | Species/strain | Sex | Age/stage and body mass | Induced model | Music condition | Acoustic delivery | Exposure schedule | Control condition | Housing and exposure unit | Allocation | n allocated / analysed / excluded by group | Outcome assays | Key music-delivery details | Outcome-specific notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

Use `NR` in any field that is absent from the supplied sources. Keep this worksheet descriptive: do not place CRIME-Q ratings here.

### B. Worksheet: `Item_Assessment`

Create **exactly 24 rows per `Experiment_ID`**, one for each item below, in this exact order. Do not omit an item because it is `NA`, `No`, or `Unclear`.

| Study_ID | Experiment_ID | Item | Construct | Provisional rating | Evidence | Location | Operational rationale | Uncertainty / notes |
|---|---|---|---|---|---|---|---|---|

The 24 required rows are:

`1X, 2X, 2Y, 3X, 3Y, 3Z, 4Y, 5X, 5Y, 5Z(1), 5Z(2), 5Z(3), 6X, 7X, 7Z(1), 7Z(2), 7Z(3), 8X, 8Z(1), 8Z(2), 9X, 10X, 10Z, MUSIC-D1`.

Use the following exact `Construct` labels:

| Item | Construct |
|---|---|
| 1X | QoR |
| 2X | QoR |
| 2Y | MQ |
| 3X | QoR |
| 3Y | MQ |
| 3Z | RoB |
| 4Y | MQ |
| 5X | QoR |
| 5Y | MQ |
| 5Z(1) | RoB |
| 5Z(2) | RoB |
| 5Z(3) | RoB |
| 6X | QoR |
| 7X | QoR |
| 7Z(1) | RoB |
| 7Z(2) | RoB |
| 7Z(3) | RoB |
| 8X | QoR |
| 8Z(1) | RoB |
| 8Z(2) | RoB |
| 9X | QoR |
| 10X | QoR |
| 10Z | RoB |
| MUSIC-D1 | Music-specific design flag |

Apply the response categories in Section 6 and the item-specific operational rules in Section 7. Use `MUSIC-D1` only as the companion design flag, not as a CRIME-Q total-score component.

### C. Worksheet: `Human_Review_Priorities`

Create one row for each issue that requires human attention. It must be a proper table, not three prose paragraphs.

| Study_ID | Experiment_ID | Category | Priority | Issue requiring review | Related item(s) | Evidence / location | Needed human decision |
|---|---|---|---|---|---|---|---|

Allowed `Category` values are:

- `Missing information materially preventing assessment`
- `Potentially important design or bias concern`
- `Item needing human adjudication`

Allowed `Priority` values are `High`, `Moderate`, or `Low`.

When no issue qualifies, create one row with `Category = None identified`, `Priority = NA`, and state `No material review priority identified from the supplied report.`

---

## 10. Brief prompt to use in NotebookLM

Select the primary-study PDF, any supplied supplement, this manual, and the CRIME-Q paper as sources. Then use this prompt:

> Create the Excel-ready three-table CRIME-Q extraction specified in Section 9 of the MUSIC-CRIME-Q manual. Use one `Experiment_ID` per independent cohort, include all 24 item rows per experiment, cite PDF locations for every code, and do not infer unreported methods.

For a paper with multiple cohorts, add:

> First identify the independent cohorts and propose the `Experiment_ID` structure; then create the three export-ready tables.

After NotebookLM generates the report, select its three-dot menu and choose **Export to Sheets**. Confirm that the resulting Google Sheet contains the `Experiment_Summary`, `Item_Assessment`, and `Human_Review_Priorities` worksheets, then download it as an Excel `.xlsx` file.

---

## 11. Quality-control procedure after NotebookLM extraction

1. A reviewer checks all evidence locations and changes any unsupported provisional code.
2. A second reviewer independently completes the same form without seeing the first reviewer’s ratings.
3. Compare item-level agreement before consensus; preserve both initial ratings and the final consensus rating.
4. Log all adaptations, especially `NA` for 2X/2Y and the separate MUSIC-D1 flag.
5. Analyse/report CRIME-Q items as distributions by item/domain. Do not sum ratings into a pseudo-validated total score.
6. Pre-specify any sensitivity analysis based on a small, defensible subset of critical domains (for example, allocation sequence, assessor blinding, attrition, selective reporting, and MUSIC-D1), rather than selecting items after examining results.

---

## 12. References

- Andersen MS, Kofoed MS, Paludan-Müller AS, et al. **CRIME-Q—a unifying tool for critical appraisal of methodological (technical) quality, quality of reporting and risk of bias in animal research.** *BMC Medical Research Methodology.* 2024;24:306. Corrected 2025. https://doi.org/10.1186/s12874-024-02413-0
- Ortega RA, et al. **Music exposure reduces anxiety- and depression-like behavior in rodents: a systematic review and multilevel meta-analysis.** Online supplementary workflow: https://santiago-0rtega.github.io/Music_on_anxiety_depression_meta_analysis/

