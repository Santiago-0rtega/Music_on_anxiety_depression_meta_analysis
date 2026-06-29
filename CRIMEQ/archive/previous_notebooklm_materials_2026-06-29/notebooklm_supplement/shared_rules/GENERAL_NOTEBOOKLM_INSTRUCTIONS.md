# General NotebookLM Instructions for CRIME-Q Extraction

Use these instructions together with the CRIME-Q codebook and the batch-specific
prompt.

## Scope

- Appraise each paper at the study level.
- Produce one assessment per paper, even if the paper contains multiple cohorts,
  experiments, contrasts, or behavioral tests.
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

## Google Sheet Output

The primary deliverable is a Google Sheet, not a prose response. If NotebookLM
cannot directly create a Google Sheet, return tab-separated values that can be
pasted into Google Sheets without reformatting.

Do not add summary prose, comments, caveats, or extra rows to the sheet.
