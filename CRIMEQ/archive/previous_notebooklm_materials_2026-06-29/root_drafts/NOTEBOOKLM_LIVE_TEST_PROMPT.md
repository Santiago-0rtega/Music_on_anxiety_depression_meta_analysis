# NotebookLM CRIME-Q Live-Test Prompt

This is the prompt to send through NotebookLM/NotebookLM MCP. Replace
`[STUDY_ID]` with one study ID from `NOTEBOOKLM_SOURCE_MANIFEST.md`.

Primary deliverable: NotebookLM should create or update a Google Sheet. The chat
response should only confirm the sheet name/link and completion status. Do not
accept a Markdown table in chat as the primary output.

Recommended calibration order:

1. `Niehues_2011_BCNEURO` - simple classical-music/silence study.
2. `Pangemanan_2024_PHJ` - catches outcome-dependent selection, n mismatch, and dropped FST.
3. `Terzioglu_2020_CMJ` - catches volume/genre confounding and perinatal litter/cage issues.
4. `Chikahisa_2007_BBR` - catches same-room acoustic conditions and multi-cohort study-level scoring.

## Prompt

```text
You are appraising ONE animal music-intervention study with the CRIME-Q tool.

STUDY TO APPRAISE: [STUDY_ID]

PRIMARY DELIVERABLE: CREATE OR UPDATE A GOOGLE SHEET.

Do not return the extraction as Markdown in the chat unless Google Sheets export
is genuinely unavailable. Write the completed extraction into a Google Sheet
named:

CRIME-Q NotebookLM Live Test - [STUDY_ID]

Create one worksheet/tab named exactly:

[STUDY_ID]

Use exactly these sources:
1. The target paper identified in NOTEBOOKLM_SOURCE_MANIFEST for [STUDY_ID].
2. CRIME-Q_Detailed_Codebook_v3 for all scoring rules.

Do not use any other paper in this notebook. Do not use outside knowledge except
to recognize that a journal article is peer reviewed when scoring 1X.

Before scoring, identify the target source internally by Study_ID, PDF filename,
and title. Then read the whole target paper, not only the abstract. Check:
Subjects/Animals, Study Design, Intervention, Statistics, Results, figure/table
legends, flow diagram if present, Ethics, Funding/COI, and Discussion.

Score all 20 items in this exact order:
1X, 3X, 3Y, 3Z, 4Y, 5X, 5Y, 5Z(1), 5Z(2), 5Z(3), 6X, 7X, 7Z(1), 7Z(2), 8X, 8Z(1), 8Z(2), 9X, 10X, 10Z.

For each item:
- SCORE must be exactly one of: Yes, No, Partly, Unclear, NA.
- Follow CRIME-Q_Detailed_Codebook_v3, including DECISION RULES.
- JUSTIFICATION must be 1-2 sentences and mention the decisive evidence or absence.
- VERBATIM must be an exact quote copied from the paper with a location tag such
  as [p.2, Methods], [Table 1], [Fig 1], [Ethics], [Funding], or [COI].
- If supporting text is absent, VERBATIM must be exactly: NOT REPORTED IN PAPER.
- Never paraphrase in VERBATIM. Never invent a quote. Never write "same as above".

Apply these recurring calibration rules:
- 1X: any journal article, including open-access/lower-tier journals, = Yes; only preprints/theses/stand-alone abstracts = No.
- 3X: missing animal supplier OR body weight, but otherwise adequate, = Partly.
- 3Y: homogeneous animals + randomization but no actual baseline balance/matching data = Partly, not Yes.
- 3Z: explicit matching/blocking/litter-balancing/weight-balancing = Yes even without a baseline table; randomization alone = Unclear.
- 4Y: "based on prior studies" without a real power calculation = No or Partly per codebook, not Yes.
- 5X: if sound level in dB is missing, score at most Partly.
- 5Y: genre confounded with volume/duration, one cage/litter per group, or unavoidable pseudoreplication = No; lesser unresolved cage/litter issues = at most Partly.
- 5Z(1): "randomly assigned" without the randomization method = Unclear.
- 5Z(2): separate music/control rooms with no matching/counterbalancing = No; explicitly matched separate rooms = Unclear; same room without cage-position randomization = Unclear.
- 5Z(3): fixed-time testing of all animals = Yes; selecting animals because they show the target phenotype after allocation = No.
- 6X: named ethics committee or protocol number = Yes; guideline/society compliance only = Partly; no welfare statement = No.
- 7X: blinding mentioned only vaguely = Partly; no blinding mentioned = No.
- 7Z(1)/7Z(2): if the paper is silent on blinding, default to Unclear, not No.
- 7Z(2): "blind to genotype" does not prove blind to music/control condition.
- 8X: cross-check Methods vs Results, including n in text, tables, figures, and flow diagrams.
- 8Z(1): if allocation n matches analysis n and no exclusions are reported, zero attrition is implied = Yes; if allocation n is never clear, = Unclear.
- 8Z(2): if Methods enumerate outcomes and Results report all with group statistics = Yes; a measured/dropped primary behavioral outcome = No.
- 9X: "more studies are needed" alone = No; a specific weakness of this study = Yes.
- 10X: a formal COI/competing-interest statement = Yes; no statement = No.
- 10Z: academic/government funding = Yes unless funder control is reported; no funding statement = Unclear.

GOOGLE SHEET REQUIREMENTS:

- Write one row per CRIME-Q item, 20 rows total.
- Use exactly these four columns, in this order:
  `Item`, `SCORE`, `JUSTIFICATION`, `VERBATIM`
- Fill every cell. No blanks. No "same as above". No ellipses.
- Keep SCORE values exactly as: Yes, No, Partly, Unclear, or NA.
- Preserve item order exactly:
  1X, 3X, 3Y, 3Z, 4Y, 5X, 5Y, 5Z(1), 5Z(2), 5Z(3), 6X, 7X, 7Z(1), 7Z(2), 8X, 8Z(1), 8Z(2), 9X, 10X, 10Z.
- Freeze the header row if the interface allows it.
- Do not add extra prose, caveats, or summary rows to the sheet.

CHAT RESPONSE AFTER THE SHEET IS WRITTEN:

Return only:

Study_ID: [STUDY_ID]
Google Sheet: [link or sheet name]
Rows completed: 20

FALLBACK ONLY IF GOOGLE SHEETS OUTPUT IS NOT AVAILABLE:

If and only if you cannot create/update a Google Sheet, return a tab-separated
table in chat that can be pasted into Google Sheets. Do not use Markdown pipes
in the fallback.

Fallback TSV format:

Study_ID: [STUDY_ID]

Item<TAB>SCORE<TAB>JUSTIFICATION<TAB>VERBATIM
1X<TAB>...<TAB>...<TAB>...
3X<TAB>...<TAB>...<TAB>...
3Y<TAB>...<TAB>...<TAB>...
3Z<TAB>...<TAB>...<TAB>...
4Y<TAB>...<TAB>...<TAB>...
5X<TAB>...<TAB>...<TAB>...
5Y<TAB>...<TAB>...<TAB>...
5Z(1)<TAB>...<TAB>...<TAB>...
5Z(2)<TAB>...<TAB>...<TAB>...
5Z(3)<TAB>...<TAB>...<TAB>...
6X<TAB>...<TAB>...<TAB>...
7X<TAB>...<TAB>...<TAB>...
7Z(1)<TAB>...<TAB>...<TAB>...
7Z(2)<TAB>...<TAB>...<TAB>...
8X<TAB>...<TAB>...<TAB>...
8Z(1)<TAB>...<TAB>...<TAB>...
8Z(2)<TAB>...<TAB>...<TAB>...
9X<TAB>...<TAB>...<TAB>...
10X<TAB>...<TAB>...<TAB>...
10Z<TAB>...<TAB>...<TAB>...
```

## Validation

Preferred: export the completed Google Sheet tab as TSV/CSV and save it locally
with the `Study_ID` in the filename, or pass the `Study_ID` as the second
argument:

```powershell
python score_notebooklm.py Niehues_2011_BCNEURO.tsv
python score_notebooklm.py sheet_export.csv Niehues_2011_BCNEURO
```

The scorer compares parsed scores against
`data/MUSIC-CRIME-Q_GOLD-STANDARD_assessment.xlsx` via `build_gold_standard.py`.
