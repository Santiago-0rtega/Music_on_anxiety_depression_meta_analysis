# CRIME-Q Music Assessment — NotebookLM Prompt

## YOUR TASK

You are appraising **animal music-intervention studies** (rodent anxiety/depression) with the **CRIME-Q** tool. For **each study**, score **20 items**. This is a **STUDY-LEVEL** appraisal: ONE assessment per paper, regardless of how many cohorts, contrasts, or experiments it contains.

For every item you output three cells: **SCORE**, **JUSTIFICATION**, **VERBATIM**.

---

## NON-NEGOTIABLE RULES (read carefully)

### 1. Read the ENTIRE paper — not the abstract
Most answers live in **Methods**, figure/table legends, the **flow diagram**, the **ethics statement**, the **funding/COI footnotes**, and the **Discussion** — NOT the abstract. Before scoring, locate and read: Subjects/Animals, Study Design, Intervention, Statistical Analysis, Results tables/figures, Limitations, Ethics, Funding, COI. If you only read the abstract you WILL score wrong.

### 2. Ground EVERY score in a real quote
- **VERBATIM must be an exact, word-for-word quote copied from the paper**, with a location tag: `[p.X, Methods]`, `[Table 1]`, `[Fig 1]`, `[Ethics statement]`, etc.
- **Never paraphrase inside VERBATIM. Never invent or guess a quote.** If you cannot find supporting text, the VERBATIM cell must say `NOT REPORTED IN PAPER` and the SCORE must reflect that (usually Unclear, No, or NA per the codebook).
- If a fact is absent, say so explicitly in JUSTIFICATION ("The paper does not report..."). Do NOT assume good practice that is not stated.

### 3. Use the codebook for EVERY item
Open `CRIME-Q_Detailed_Codebook_v3.csv`. For each item it gives `Yes_Criteria`, `Partly_Criteria`, `No_Criteria`, `Unclear_Criteria`, `Music_Examples`, and `Common_Pitfalls` (many contain a **DECISION RULE** — follow it exactly). Match the paper to those criteria; do not invent your own thresholds.

### 4. Deliver the COMPLETE table — no blanks, no "..."
Every study × every item × 3 cells must be filled. Do not stop early, do not summarize, do not write "same as above." If the table is long, continue until all 20 items for all studies are done.

### 5. Cross-check numbers
Compare the n in the **flow diagram / figures / tables** against the n in the **text**. Internal contradictions (e.g., text says 42 rats, flow diagram says 39) are real findings — flag them under item 8X and 8Z(1).

---

## SCORING VALUES

- **Yes** — fully meets the Yes_Criteria
- **Partly** — meets some but not all (only where the item allows Partly)
- **No** — meets the No_Criteria
- **Unclear** — the paper does not report enough to decide
- **NA** — item genuinely does not apply (explain why)

When the paper is SILENT on something, default to **Unclear** (not No), unless the codebook's DECISION RULE says otherwise.

---

## OUTPUT FORMAT — Google Sheet

Produce a **Google Sheet** (or a tab/comma-separated table that pastes cleanly into Google Sheets).

- **One row per study** (20 studies total).
- **Columns**: `Study_ID`, `Study_Title`, then for each of the 20 items in order: `<ItemID>_<Name>_SCORE`, `<ItemID>_<Name>_JUSTIFICATION`, `<ItemID>_<Name>_VERBATIM`.
- That is **62 columns** and **20 data rows** = 1,240 filled cells (incl. headers).

Item order: 1X, 3X, 3Y, 3Z, 4Y, 5X, 5Y, 5Z(1), 5Z(2), 5Z(3), 6X, 7X, 7Z(1), 7Z(2), 8X, 8Z(1), 8Z(2), 9X, 10X, 10Z.

If a single 62-column sheet is unwieldy, you MAY instead deliver one sheet per study (20 sheets), each a tidy 3-column table: `Item | Score | Justification | Verbatim`. Either format is acceptable — but it must be COMPLETE.

---

## WORKED EXAMPLE (verify your formatting against this)

These are two REAL, correct rows produced by applying the codebook to the actual PDFs. Match this depth and grounding.

**Study: Niehues_2011_BCNEURO** — "The Power of Classic Music to Reduce Anxiety in Rats Treated with Simvastatin"

| Item | SCORE | JUSTIFICATION | VERBATIM |
|---|---|---|---|
| 1X Peer Review | Yes | Published in the peer-reviewed journal Basic and Clinical Neuroscience. | `[p.1] "Basic and Clinical Neuroscience, Summer 2011, Volume 2, Number 4"` |
| 3X Animals Reporting | Yes | Species, strain, sex, age, weight, source and group size all reported. | `[p.2, Methods] "A total of sixty male Wistar albino rats (Rattus norvegicus)... 3 to 5 months of age, weighing 220 to 310 g"` |
| 3Y Animals Tech Quality | Partly | Homogeneous animals and randomization, but no baseline behavioural comparison reported (DECISION RULE). | `[p.2] "They were randomized with ten rats per subgroup"` |
| 5X Music Reporting | Yes | Genre, piece, duration, volume, schedule and control all specified. | `[p.2, Methods] "Music (Mozart's piano sonata, KV361, Largo, 8:35 min duration)... music 65-75 dB"` |
| 5Z(2) Random Housing | Unclear | Silence and music in separate rooms described as identical except sound — matched but still a residual room confound (SEPARATE-ROOMS RULE). | `[p.2] "The silence room was exactly the same as the room in which music were played but here there was no sounds except for ambient noises"` |
| 6X Ethics | Partly | Names guideline/society compliance but no ethics-committee approval or protocol number (DECISION RULE). | `[p.2] "performed in compliance with the recommendations of SBNeC... based on the US National Institutes of Health Guide"` |
| 9X Limitations | No | Discussion offers only future directions, no specific weakness of this study (DECISION RULE). | `[p.5] "There is a need to conduct more studies, which replicate the designs..."` |

**Study: Pangemanan_2024_PHJ** — "Mozart K488 Addition Can Improve Depressive-Like Behavior in Rats"

| Item | SCORE | JUSTIFICATION | VERBATIM |
|---|---|---|---|
| 3Z Baseline Balance | Yes | Pre-CUMS body weights reported per group and not significantly different (p=0.825). | `[Table 1] "Pre CUMS ... 0.825a ANOVA"` |
| 5Z(3) Outcome Assessment | No | Animals were included into the treatment group based on showing the target phenotype (low SPT) — outcome-dependent selection. | `[p.2] "criteria for inclusion involved selecting male rats... demonstrating depressive-like behavior in the treatment group as determined by the Sucrose Preference Test"` |
| 6X Ethics | Yes | Named ethics committee approval with a protocol reference number. | `[p.1, Methods] "received approval from the Animal Care and Use Committee of the Faculty of Veterinary Medicine, Universitas Airlangga... reference number 2.KE.120.10.2021"` |
| 8X Methods-Results | Partly | Internal n contradiction (text "42 rats" vs flow diagram "39 included") and FST dropped, but the primary SPT comparison remains interpretable. | `[p.3, Results] "A total of 42 rats were included"` vs `[Fig 1] "39 rats included"` |
| 8Z(1) Attrition | No | 42 allocated but only 39 analysed, with the 3 lost not explained. | `[Fig 1] "Wistar rats (n=42)" → "39 rats included"` |
| 8Z(2) Selective Reporting | No | FST was measured but dropped from results "due to technical problems" (disclosed, but a primary depression outcome is unreported). | `[p.2] "due to technical problems, FST cannot be analyzed"` |
| 9X Limitations | Yes | Multiple specific limitations of this study are stated. | `[p.5] "This study has several limitations, such as the measurement of only the plasma corticosterone, hippocampal melatonin..."` |

**Study: Terzioglu_2020_CMJ** — "Effects of music on stress induced hormones and oxidative stress levels" (three genres at different volumes, perinatal exposure)

| Item | SCORE | JUSTIFICATION | VERBATIM |
|---|---|---|---|
| 5Y Music Tech Quality | No | Each genre was played at a different volume (classical 60 dB, sufi 30 dB, rock 120 dB), so genre is confounded with loudness; only one cage of dams per group (litter confound). | `[p.2, Methods] "classical (Canon in D Major/ Johann Pachelbel, 60 dB) (n=4), traditional Sufi (... 30 dB) (n=4), and rock (... 120 dB) (n=4)"` |
| 7Z(2) Assessor Blinding | Yes | Observers scoring the tail-suspension test were blinded to group. | `[p.2, Measures] "The observers were blinded to the groups."` |
| 10X COI | Yes | An explicit competing-interests declaration is present. | `[p.5] "Conflict of Interest: Authors declared no conflict of interest."` |

**Study: Chikahisa_2007_BBR** — note this paper has 8 cohorts; still produce ONE study-level row.

| Item | SCORE | JUSTIFICATION | VERBATIM |
|---|---|---|---|
| 5Z(2) Random Housing | Unclear | All acoustic conditions were run in the SAME room (no separate-room confound), but cage-position randomization across conditions is not reported. | `[p.2, Methods] "The silence condition was performed in the same room as the music and white-noise groups"` |
| 6X Ethics | Yes | Named ethics committee approval with an approval number. | `[p.2] "approved by the Animal Study Committee of Tokushima University (No. 05047)"` |

---

## THE 20 STUDIES

1. Camargo_2013_PSYN
2. Chen_2019_BIOMEDRI
3. Cheng_2024_HLYN
4. Chikahisa_2007_BBR
5. Escribano_2014_APPANBSC
6. Flores_2018_NP
7. Freitas_2020_ECNE
8. Fu_2023_TRANSPSY
9. Fu_2025_TRANSPSY
10. Krishnamurthy_2025_INDIANJTRADITKNOW
11. Li_2010_BR
12. Milbratz_2017_ALN
13. Niehues_2011_BCNEURO
14. Pangemanan_2024_PHJ
15. Papadakakis_2019_BBR
16. Ren_2024_ASEAN
17. Rizzolo_2021_CC
18. Saghari_2021_BIOINTERFACE
19. Sampaio_2017_PSYNEURO
20. Terzioglu_2020_CMJ

---

## THE 20 ITEMS (full criteria in CRIME-Q_Detailed_Codebook_v3.csv)

| # | Item | Domain | Construct |
|---|------|--------|-----------|
| 1 | 1X | Peer Review | QoR |
| 2 | 3X | Animals: Reporting | QoR |
| 3 | 3Y | Animals: Technical Quality | MQ |
| 4 | 3Z | Selection Bias: Baseline | RoB |
| 5 | 4Y | Sample-Size Calculation | QoR |
| 6 | 5X | Music Intervention: Reporting | QoR |
| 7 | 5Y | Music Intervention: Technical Quality | MQ |
| 8 | 5Z(1) | Selection Bias: Sequence Generation | RoB |
| 9 | 5Z(2) | Performance Bias: Random Housing | RoB |
| 10 | 5Z(3) | Detection Bias: Outcome Assessment | RoB |
| 11 | 6X | Ethical Compliance | QoR |
| 12 | 7X | Blinding: Reporting | QoR |
| 13 | 7Z(1) | Performance Bias: Experimenter Blinding | RoB |
| 14 | 7Z(2) | Detection Bias: Assessor Blinding | RoB |
| 15 | 8X | Methods-Results Alignment | QoR |
| 16 | 8Z(1) | Attrition Bias: Incomplete Data | RoB |
| 17 | 8Z(2) | Reporting Bias: Selective Outcomes | RoB |
| 18 | 9X | Discussion: Limitations | QoR |
| 19 | 10X | Conflict-of-Interest Statement | QoR |
| 20 | 10Z | Other Bias: Funder Influence | RoB |

Items **5X and 5Y are the heart of a music appraisal** — give them extra care.

---

## CALIBRATION (how a human expert scored these papers)

A two-person human gold-standard assessment of all 20 papers already exists in `data/MUSIC-CRIME-Q_GOLD-STANDARD_assessment.xlsx`. Your output should reproduce it. Recurring decisions in that key (apply them):

- **1X**: every journal article = Yes (including open-access journals); only preprints/theses/abstracts = No.
- **3X**: missing the animal supplier OR body weight (one descriptor) = Partly, not No.
- **3Z**: if animals were matched/balanced on litter, age, sex, or body weight, score Yes even without a baseline table.
- **5X**: if the sound level (dB) is not reported, the item is Partly even when everything else is given.
- **5Z(2)**: separate rooms for music vs control with no matching/counterbalancing = No; same room or matched rooms = Unclear.
- **6X**: a named ethics committee (or protocol number) = Yes; compliance with only a guideline/EU directive (86/609, 2010/63, NIH Guide) with no committee = Partly.
- **7X vs 7Z(2)**: "blinded to genotype" reports blinding (7X = Yes) but does not by itself mean blind to the music/control condition (7Z(2) = Unclear).
- **7Z(1)/7Z(2)**: if the paper is silent on blinding, default to Unclear (not No).
- **9X**: "more studies are needed" alone = No; a stated specific weakness of THIS study = Yes.
- **10Z**: academic/government funding = Yes; no funding statement at all = Unclear.

## FINAL CHECK BEFORE YOU RETURN THE SHEET

- [ ] Every study has all 20 items scored (no blanks, no "...").
- [ ] Every VERBATIM is an exact quote with a location tag, OR explicitly `NOT REPORTED IN PAPER`.
- [ ] No score relies on the abstract alone.
- [ ] Flow-diagram / table numbers were cross-checked against the text.
- [ ] Scores follow the codebook DECISION RULES and the calibration above, not your own judgment.
