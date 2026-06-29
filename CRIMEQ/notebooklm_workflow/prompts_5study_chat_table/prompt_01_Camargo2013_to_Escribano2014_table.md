# Prompt 01: Camargo2013_to_Escribano2014 Chat Markdown Table

```text
Use ONLY these 5 PDFs:
Camargo2013.pdf
Chen2019.pdf
Cheng2024.pdf
Chikahisa2007.pdf
Escribano2014.pdf

Use study_manifest.md, CRIME-Q_CODEBOOK_FOR_NOTEBOOKLM.md, GENERAL_NOTEBOOKLM_INSTRUCTIONS.md, CRIME-Q_NOTEBOOKLM_CALIBRATION_RULES.md, and WIDE_SHEET_COLUMN_TEMPLATE.md. This should be a clean batch notebook; if any extra instruction source is present, ignore it unless it is one of those files.

Return the CRIME-Q assessment in chat only. Do not create a Google Sheet, Studio table, note, report, or file.

Output one copy-paste Markdown table only. Do not use a code block. Do not add narrative before or after the table.

Rows, in order:
Camargo2013
Chen2019
Cheng2024
Chikahisa2007
Escribano2014

Table rules:
- Include exactly 7 physical table rows: 1 header row, 1 Markdown separator row, and 5 study rows.
- The first two header cells must be exactly Study and Study_Title.
- Use uppercase suffixes exactly: _JUSTIFICATION and _VERBATIM.
- Use the exact columns from WIDE_SHEET_COLUMN_TEMPLATE.md.
- The item-ID columns are the score columns.
- Do not create Study_ID, ITEM_, _SCORE, _Justification, _Verbatim, or parenthesis-free item columns.
- Keep each study on its own table row.
- Do not omit 5Z(3), 5Z(3)_JUSTIFICATION, or 5Z(3)_VERBATIM.
- Before finalizing, count exactly 62 header cells and exactly 20 score cells in every study row. If any column is missing, rebuild the table before answering.

5X check: score reporting completeness of the music intervention. If the paper reports the music stimulus/piece or genre, exposure duration/schedule, sound intensity/level, and control/comparator condition, score 5X = Yes. Missing speaker placement or hardware details may affect 5Y, not 5X.

5Z(3) check: this is not assessor blinding. Score 5Z(3) = Yes when animals/groups were assessed at planned or fixed outcome timepoints with no outcome-dependent selection or exclusion reported. Use 7Z(2), not 5Z(3), for assessor blinding.

For every item: score must be Yes, No, Partly, Unclear, or NA; justification must be one concise sentence; verbatim must be quoted text plus a location tag, or exactly NOT REPORTED IN PAPER.

VERBATIM self-check: a location tag by itself is invalid. A page range, table label, figure label, or parenthetical summary without quoted words is invalid. Do not write cells such as [Table 1], [p.30-37], or [p.3-4, Methods] (OFT, EPM...). Use exact quoted words from the paper plus a location tag, or exactly NOT REPORTED IN PAPER.

Before answering, verify all 5 exact article titles from study_manifest.md. If any PDF is unreadable, stop and write only: Source access failed for: [filename].
```

