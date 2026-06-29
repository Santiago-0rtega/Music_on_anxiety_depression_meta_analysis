# NotebookLM Manual Review Checklist

Use this checklist after NotebookLM produces a five-study CRIME-Q table.

## Table Structure

- Confirm exactly five study rows are present.
- Confirm the first two columns are `Study` and `Study_Title`.
- Confirm the table has exactly 62 columns.
- Confirm every CRIME-Q item is present, including `5Z(3)`,
  `5Z(3)_JUSTIFICATION`, and `5Z(3)_VERBATIM`.
- Confirm score columns use item IDs only, with no `ITEM_` prefix and no
  `_SCORE` suffix.
- Confirm each score is one of `Yes`, `No`, `Partly`, `Unclear`, or `NA`.

## Evidence Review

- Confirm every `VERBATIM` cell contains quoted words from the paper plus a
  location tag.
- Replace or flag location-only evidence such as `[Table 1]`, `[Fig 2]`, or
  `[p.30-37]`.
- Confirm `NOT REPORTED IN PAPER` is used only when the paper does not report
  the relevant information.
- Check that evidence comes from the target paper row, not from another source
  in the notebook.

## Item Checks

- `5Z(3)`: Do not treat this as assessor blinding. It asks whether
  animals/groups were assessed at planned or fixed outcome timepoints without
  outcome-dependent selection or exclusion.
- `7Z(2)`: Check whether outcome assessment was actually blinded. If behavior
  was live/manual and the observer could know condition, this may be higher risk
  than NotebookLM reports.
- `8Z(1)`: Check allocation-to-analysis denominators across Methods, Results,
  figures, legends, tables, and statistical degrees of freedom. A single
  matching `n` is not enough if the full flow is unclear.
- `9X`: Search Discussion and Conclusion for concrete current-study caveats,
  discrepancies, uncertainties, untested mechanisms, or measurement/model
  limits. Do not rely only on a formal `Limitations` heading.
- `10Z`: Distinguish no funding statement from academic/government funding. No
  funding information is usually `Unclear`; academic/government funding without
  funder influence is usually lower concern.

## After Review

- Keep corrections in the working extraction sheet, not in the public prompt.
- If the same error repeats across batches, update only the general calibration
  rules, not target-study answers.
- Do not add completed answers, worked examples from target studies, or
  validation labels to NotebookLM sources.
