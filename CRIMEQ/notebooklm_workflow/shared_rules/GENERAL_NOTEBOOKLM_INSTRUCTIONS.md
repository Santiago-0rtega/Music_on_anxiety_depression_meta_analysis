# General NotebookLM Instructions for CRIME-Q Extraction

Use these instructions together with the CRIME-Q codebook and the batch-specific
prompt.

## Scope

- Appraise each paper at the study level.
- Produce one assessment per paper, even if the paper contains multiple cohorts,
  experiments, contrasts, or behavioral tests.
- This is not a whole-paper appraisal of every experiment in the article. Score
  the CRIME-Q items only as they apply to the behavioral assays and the in vivo
  music/acoustic exposure.
- For items about feasibility, technical quality, alignment, attrition, outcome
  reporting, blinding, or limitations, focus on the animals/groups contributing
  behavioral outcomes and the acoustic/music delivery, exposure, and control
  conditions that could affect those outcomes.
- Do not give credit for, or penalize based on, details that apply only to
  molecular, biochemical, histological, hormonal, biomarker, or other
  non-behavioral procedures unless those details directly determine the
  behavioral assay, which animals contributed behavioral data, or the
  interpretation of the acoustic/music exposure.
- Use only the uploaded sources in the active NotebookLM notebook.
- Do not use other papers in the notebook to score a target study.

## Reading Requirements

For each paper, read beyond the abstract. Check:

- title page and journal information
- Methods, including animals, housing, intervention, outcomes, statistics
- tables, figures, legends, and flow diagrams
- ethics, funding, acknowledgments, and conflict-of-interest statements
- Results and Discussion

## Evidence Rules

- Every score must be grounded in evidence from the target paper.
- The `VERBATIM` cell must contain an exact quote from the target paper with a
  location tag such as `[p.2, Methods]`, `[Table 1]`, `[Fig 1]`, `[Ethics]`,
  `[Funding]`, or `[COI]`.
- If the relevant information is not reported, write exactly:
  `NOT REPORTED IN PAPER`.
- Do not paraphrase in `VERBATIM`.
- Do not infer good practice when the paper is silent.

## Score Values

Use only:

- `Yes`
- `No`
- `Partly`
- `Unclear`
- `NA`

When information is absent, use `Unclear` unless the codebook states that the
absence should be scored as `No`, `Partly`, or `NA`.

## Output Format

The batch-specific prompt controls the output destination. It may request a
Google Sheet, a Studio Data Table, or a copy-paste table in chat. Follow that
destination exactly.

- If the prompt requests a Google Sheet or Studio Data Table, create that
  destination and do not provide only a prose summary.
- If the prompt requests chat output, do not create a Google Sheet, Studio Data
  Table, note, report, or downloadable file.
- For chat copy-paste output, use one Markdown table unless the prompt explicitly
  asks for TSV.
- If TSV is requested, preserve one physical line per study. If NotebookLM cannot
  preserve row breaks, use a Markdown table instead.
- Do not add summary prose, comments, caveats, or extra rows.
