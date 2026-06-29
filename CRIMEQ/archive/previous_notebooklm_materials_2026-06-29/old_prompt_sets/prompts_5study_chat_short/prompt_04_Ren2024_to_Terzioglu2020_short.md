# Prompt 04: Ren2024_to_Terzioglu2020 Short Chat TSV

```text
Use ONLY these 5 PDFs:
Ren2024.pdf
Rizzolo2021.pdf
Saghari2021.pdf
Sampaio2017.pdf
Terzioglu2020.pdf

Use the uploaded manifest, CRIME-Q codebook, general instructions, calibration rules, and WIDE_SHEET_COLUMN_TEMPLATE.md.

Return the CRIME-Q assessment in chat only. Do not create a Google Sheet, Studio table, note, report, or file.

Output one copy-paste TSV code block only: exactly 6 physical lines, actual tabs between cells, no wrapped rows, no narrative.

Rows, in order:
Ren2024
Rizzolo2021
Saghari2021
Sampaio2017
Terzioglu2020

Columns: copy the exact 62-column header from WIDE_SHEET_COLUMN_TEMPLATE.md, including Study_Title. The item-ID columns are the score columns. Do not create ITEM_, _SCORE, or parenthesis-free item columns.

For every item: score must be Yes, No, Partly, Unclear, or NA; justification must be one concise sentence; verbatim must be quoted text plus a location tag, or exactly NOT REPORTED IN PAPER.

Before answering, verify all 5 exact article titles from all_studies_manifest.md. If any PDF is unreadable, stop and write only: Source access failed for: [filename].
```
