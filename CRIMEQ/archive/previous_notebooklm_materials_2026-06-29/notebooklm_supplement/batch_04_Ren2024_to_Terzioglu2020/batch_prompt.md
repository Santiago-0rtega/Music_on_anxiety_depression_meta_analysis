# Batch 04 NotebookLM Prompt

Paste this prompt into the NotebookLM notebook after uploading the five study
PDFs listed in `study_manifest.md` and the shared rules files.

```text
You are extracting study-level CRIME-Q assessments for five animal music-intervention papers.

Use only the sources uploaded in this NotebookLM notebook:
- the five target study PDFs for this batch
- GENERAL_NOTEBOOKLM_INSTRUCTIONS
- CRIME-Q_CODEBOOK_FOR_NOTEBOOKLM
- WIDE_SHEET_COLUMN_TEMPLATE

Create or update a Google Sheet named:
CRIME-Q music extraction batch 04

Create one worksheet/tab named:
batch_04

The sheet must be a wide table with exactly 6 rows:
- row 1: column headers from WIDE_SHEET_COLUMN_TEMPLATE
- rows 2-6: one row for each study below

Studies to assess, in this exact row order:
1. Ren2024
2. Rizzolo2021
3. Saghari2021
4. Sampaio2017
5. Terzioglu2020

For each study, score all 20 CRIME-Q items at study level:
1X, 3X, 3Y, 3Z, 4Y, 5X, 5Y, 5Z(1), 5Z(2), 5Z(3), 6X, 7X, 7Z(1), 7Z(2), 8X, 8Z(1), 8Z(2), 9X, 10X, 10Z.

For every item, fill three cells:
- SCORE: exactly one of Yes, No, Partly, Unclear, or NA
- JUSTIFICATION: one or two concise sentences explaining the score
- VERBATIM: exact quote from the target paper with a location tag; if absent, write exactly NOT REPORTED IN PAPER

Do not leave blank cells. Do not write "same as above". Do not add summary rows.
Do not return the extraction as a Markdown table in chat. The primary deliverable is the Google Sheet.

When the sheet is complete, reply only with:
Google Sheet: [link or sheet name]
Worksheet: batch_04
Rows completed: 5
```
