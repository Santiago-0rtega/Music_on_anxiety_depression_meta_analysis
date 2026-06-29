# Batch 01 Short NotebookLM Prompt

Use after uploading the five study PDFs in `study_manifest.md` plus all files in
`../shared_rules/`.

```text
Using only the uploaded sources, create a Google-Sheets-ready wide table for "CRIME-Q music extraction batch 01".

Use study_manifest.md to match each Study key to the correct uploaded paper title. Use WIDE_SHEET_COLUMN_TEMPLATE for the exact columns. Make one header row plus one row for each study, in this order:
Camargo2013, Chen2019, Cheng2024, Chikahisa2007, Escribano2014.

Apply CRIME-Q_CODEBOOK_FOR_NOTEBOOKLM and GENERAL_NOTEBOOKLM_INSTRUCTIONS. Score all 20 CRIME-Q items for each study at study level.

For every item fill SCORE, JUSTIFICATION, and VERBATIM. SCORE must be Yes, No, Partly, Unclear, or NA. VERBATIM must be an exact quote from the study with a location tag, or exactly NOT REPORTED IN PAPER.

Do not create generic fields such as Randomization, Blinding, Power Calculation, or Animal Characteristics. Use only the CRIME-Q item columns from WIDE_SHEET_COLUMN_TEMPLATE.

Do not leave blanks. If you cannot create an actual Google Sheet, return a tab-separated wide table that can be pasted directly into Google Sheets. Do not return a Markdown table.
```
