# All-20 Chat-Only NotebookLM Test Prompt

```text
Create the complete CRIME-Q assessment for all 20 uploaded study PDFs in this notebook.

Do not create a Google Sheet, Studio Data Table, note, report, or downloadable file. Write the answer in this chat only.

Write the output as one tab-separated table inside one plain-text code block. Do not add narrative before or after the table.

Use ONLY these uploaded study PDFs for this table:
Camargo2013.pdf
Chen2019.pdf
Cheng2024.pdf
Chikahisa2007.pdf
Escribano2014.pdf
Flores2018.pdf
Freitas2020.pdf
Fu2023.pdf
Fu2025.pdf
Krishnamurthy2025.pdf
Li2010.pdf
Milbratz2017.pdf
Niehues2011.pdf
Pangemanan2024.pdf
Papadakakis2019.pdf
Ren2024.pdf
Rizzolo2021.pdf
Saghari2021.pdf
Sampaio2017.pdf
Terzioglu2020.pdf

Use these uploaded instruction sources:
all_studies_manifest.md
CRIME-Q_CODEBOOK_FOR_NOTEBOOKLM.md
GENERAL_NOTEBOOKLM_INSTRUCTIONS.md
WIDE_SHEET_COLUMN_TEMPLATE.md
CRIME-Q_NOTEBOOKLM_CALIBRATION_RULES.md

Before creating the table, verify that you can read all 20 PDFs by finding each exact article title from all_studies_manifest.md. If any PDF is unavailable, stop and report only: Source access failed for: [filename].

The table must have exactly 20 study rows, in this order:
Camargo2013
Chen2019
Cheng2024
Chikahisa2007
Escribano2014
Flores2018
Freitas2020
Fu2023
Fu2025
Krishnamurthy2025
Li2010
Milbratz2017
Niehues2011
Pangemanan2024
Papadakakis2019
Ren2024
Rizzolo2021
Saghari2021
Sampaio2017
Terzioglu2020

Use CRIME-Q item IDs exactly. Do not replace them with generic fields.

Item meanings: 1X=Peer Review; 3X=Animals: Reporting; 3Y=Animals: Technical Quality; 3Z=Selection Bias: Baseline Characteristics; 4Y=Sample-Size Calculation; 5X=Music Intervention: Reporting; 5Y=Music Intervention: Technical Quality; 5Z(1)=Selection Bias: Sequence Generation; 5Z(2)=Performance Bias: Random Housing; 5Z(3)=Detection Bias: Outcome Assessment; 6X=Ethical Compliance; 7X=Blinding: Reporting; 7Z(1)=Performance Bias: Experimenter Blinding; 7Z(2)=Detection Bias: Assessor Blinding; 8X=Methods-Results Alignment; 8Z(1)=Attrition Bias: Incomplete Data; 8Z(2)=Reporting Bias: Selective Outcomes; 9X=Discussion: Limitations; 10X=Conflict-of-Interest Statement; 10Z=Other Bias: Funder Influence.

For every item, apply CRIME-Q_CODEBOOK_FOR_NOTEBOOKLM.md and CRIME-Q_NOTEBOOKLM_CALIBRATION_RULES.md. Use exactly the columns in WIDE_SHEET_COLUMN_TEMPLATE.md. The item-ID columns, such as 1X and 5Z(1), are the score columns.

Each item-ID score cell must be exactly one of: Yes, No, Partly, Unclear, NA.
JUSTIFICATION must be one concise sentence explaining the CRIME-Q score.
VERBATIM must be a short exact quote from the target paper with quoted words plus a location tag, or exactly NOT REPORTED IN PAPER. A page/table/figure location alone is invalid.

Do not use other papers in the notebook to score a target study.
Do not write "full text not available in source context" in any CRIME-Q cell.
Do not put location-only citations in VERBATIM cells.
Do not create columns beginning with ITEM_, columns ending in _SCORE, or columns that remove parentheses from item IDs.
Do not add standalone citation-number cells or citation-only cells.
Do not add extra columns.
Do not leave any cells blank.
Do not summarize.

Final self-check before responding:
- Header row exactly matches WIDE_SHEET_COLUMN_TEMPLATE.md.
- There are exactly 20 study rows.
- The rows are in the requested order.
- Every item-ID score cell is Yes, No, Partly, Unclear, or NA.
- Every VERBATIM cell contains quoted words plus a location tag, or exactly NOT REPORTED IN PAPER.
- No score column is named with ITEM_ or _SCORE.
```
