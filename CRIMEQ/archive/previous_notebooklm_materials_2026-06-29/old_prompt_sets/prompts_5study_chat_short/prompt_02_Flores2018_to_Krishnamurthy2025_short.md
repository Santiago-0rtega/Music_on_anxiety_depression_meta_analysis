# Prompt 02: Flores2018_to_Krishnamurthy2025 Short Chat TSV

```text
Use ONLY these 5 PDFs:
Flores2018.pdf
Freitas2020.pdf
Fu2023.pdf
Fu2025.pdf
Krishnamurthy2025.pdf

Use the uploaded manifest, CRIME-Q codebook, general instructions, calibration rules, and WIDE_SHEET_COLUMN_TEMPLATE.md.

Return the CRIME-Q assessment in chat only. Do not create a Google Sheet, Studio table, note, report, or file.

Output one copy-paste TSV code block only: exactly 6 physical lines, actual tabs between cells, no wrapped rows, no narrative.

Rows, in order:
Flores2018
Freitas2020
Fu2023
Fu2025
Krishnamurthy2025

Columns: copy the exact 62-column header from WIDE_SHEET_COLUMN_TEMPLATE.md, including Study_Title. The item-ID columns are the score columns. Do not create ITEM_, _SCORE, or parenthesis-free item columns.

For every item: score must be Yes, No, Partly, Unclear, or NA; justification must be one concise sentence; verbatim must be quoted text plus a location tag, or exactly NOT REPORTED IN PAPER.

Before answering, verify all 5 exact article titles from all_studies_manifest.md. If any PDF is unreadable, stop and write only: Source access failed for: [filename].
```
