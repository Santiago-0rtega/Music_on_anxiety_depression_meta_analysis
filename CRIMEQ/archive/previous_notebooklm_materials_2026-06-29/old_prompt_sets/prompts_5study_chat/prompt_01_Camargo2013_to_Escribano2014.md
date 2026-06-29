# Prompt 01: Camargo2013_to_Escribano2014 Chat-Only 5-Study Test

```text
Create the CRIME-Q assessment for these 5 uploaded study PDFs in this notebook.

Do not create a Google Sheet, Studio Data Table, note, report, or downloadable file. Write the answer in this chat only.

Write the output as one copy-paste TSV table inside one plain-text code block. Do not add narrative before or after the table.

Copy-paste TSV format requirements:
- Use actual tab characters between cells.
- Use actual newline characters between rows.
- The code block must contain exactly 6 physical lines: line 1 is the header, then one line for each of the 5 studies.
- Do not put more than one study row on the same physical line.
- Do not wrap a row by inserting extra newlines inside cells.
- Include Study_Title as the second column.
- The header line must be exactly this TSV header:
Study	Study_Title	1X	1X_JUSTIFICATION	1X_VERBATIM	3X	3X_JUSTIFICATION	3X_VERBATIM	3Y	3Y_JUSTIFICATION	3Y_VERBATIM	3Z	3Z_JUSTIFICATION	3Z_VERBATIM	4Y	4Y_JUSTIFICATION	4Y_VERBATIM	5X	5X_JUSTIFICATION	5X_VERBATIM	5Y	5Y_JUSTIFICATION	5Y_VERBATIM	5Z(1)	5Z(1)_JUSTIFICATION	5Z(1)_VERBATIM	5Z(2)	5Z(2)_JUSTIFICATION	5Z(2)_VERBATIM	5Z(3)	5Z(3)_JUSTIFICATION	5Z(3)_VERBATIM	6X	6X_JUSTIFICATION	6X_VERBATIM	7X	7X_JUSTIFICATION	7X_VERBATIM	7Z(1)	7Z(1)_JUSTIFICATION	7Z(1)_VERBATIM	7Z(2)	7Z(2)_JUSTIFICATION	7Z(2)_VERBATIM	8X	8X_JUSTIFICATION	8X_VERBATIM	8Z(1)	8Z(1)_JUSTIFICATION	8Z(1)_VERBATIM	8Z(2)	8Z(2)_JUSTIFICATION	8Z(2)_VERBATIM	9X	9X_JUSTIFICATION	9X_VERBATIM	10X	10X_JUSTIFICATION	10X_VERBATIM	10Z	10Z_JUSTIFICATION	10Z_VERBATIM

Use ONLY these uploaded study PDFs for this table:
Camargo2013.pdf
Chen2019.pdf
Cheng2024.pdf
Chikahisa2007.pdf
Escribano2014.pdf

Use these uploaded instruction sources:
all_studies_manifest.md
CRIME-Q_CODEBOOK_FOR_NOTEBOOKLM.md
GENERAL_NOTEBOOKLM_INSTRUCTIONS.md
WIDE_SHEET_COLUMN_TEMPLATE.md
CRIME-Q_NOTEBOOKLM_CALIBRATION_RULES.md

Before creating the table, verify that you can read all 5 target PDFs by finding each exact article title from all_studies_manifest.md. If any PDF is unavailable, stop and report only: Source access failed for: [filename].

The table must have exactly 5 study rows, in this order:
Camargo2013
Chen2019
Cheng2024
Chikahisa2007
Escribano2014

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
- Header row exactly matches the TSV header provided above and WIDE_SHEET_COLUMN_TEMPLATE.md.
- The code block has exactly 6 physical lines: 1 header line plus exactly 5 study rows.
- The rows are in the requested order.
- Every item-ID score cell is Yes, No, Partly, Unclear, or NA.
- Every VERBATIM cell contains quoted words plus a location tag, or exactly NOT REPORTED IN PAPER.
- No score column is named with ITEM_ or _SCORE.
```



