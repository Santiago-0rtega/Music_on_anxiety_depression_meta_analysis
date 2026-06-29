# Prompt 03: Li2010_to_Papadakakis2019 Short Chat TSV

```text
Use ONLY these 5 PDFs:
Li2010.pdf
Milbratz2017.pdf
Niehues2011.pdf
Pangemanan2024.pdf
Papadakakis2019.pdf

Use the uploaded manifest, CRIME-Q codebook, general instructions, calibration rules, and WIDE_SHEET_COLUMN_TEMPLATE.md.

Return the CRIME-Q assessment in chat only. Do not create a Google Sheet, Studio table, note, report, or file.

Output one copy-paste TSV code block only: exactly 6 physical lines, actual tabs between cells, no wrapped rows, no narrative.

Rows, in order:
Li2010
Milbratz2017
Niehues2011
Pangemanan2024
Papadakakis2019

Columns: copy the exact 62-column header from WIDE_SHEET_COLUMN_TEMPLATE.md, including Study_Title. The item-ID columns are the score columns. Do not create ITEM_, _SCORE, or parenthesis-free item columns.

For every item: score must be Yes, No, Partly, Unclear, or NA; justification must be one concise sentence; verbatim must be quoted text plus a location tag, or exactly NOT REPORTED IN PAPER.

Before answering, verify all 5 exact article titles from all_studies_manifest.md. If any PDF is unreadable, stop and write only: Source access failed for: [filename].
```
