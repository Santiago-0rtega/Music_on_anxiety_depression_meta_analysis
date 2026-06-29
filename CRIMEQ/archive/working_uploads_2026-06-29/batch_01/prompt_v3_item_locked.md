# Batch 01 Prompt v3 - Item-Locked Data Table

```text
Create a Studio Data Table named "CRIME-Q music extraction batch 01 v3".

Use ONLY these uploaded study PDFs:
Camargo2013.pdf
Chen2019.pdf
Cheng2024.pdf
Chikahisa2007.pdf
Escribano2014.pdf

Use these uploaded instruction sources:
study_manifest.md
CRIME-Q_CODEBOOK_FOR_NOTEBOOKLM.md
GENERAL_NOTEBOOKLM_INSTRUCTIONS.md
WIDE_SHEET_COLUMN_TEMPLATE.md

The table must have exactly 5 rows, one row per study, in this order:
Camargo2013
Chen2019
Cheng2024
Chikahisa2007
Escribano2014

The table must use CRIME-Q item IDs exactly. Do not replace them with generic fields.

Item meanings:
1X = Peer Review
3X = Animals: Reporting
3Y = Animals: Technical Quality
3Z = Selection Bias: Baseline Characteristics
4Y = Sample-Size Calculation
5X = Music Intervention: Reporting
5Y = Music Intervention: Technical Quality
5Z(1) = Selection Bias: Sequence Generation
5Z(2) = Performance Bias: Random Housing
5Z(3) = Detection Bias: Outcome Assessment
6X = Ethical Compliance
7X = Blinding: Reporting
7Z(1) = Performance Bias: Experimenter Blinding
7Z(2) = Detection Bias: Assessor Blinding
8X = Methods-Results Alignment
8Z(1) = Attrition Bias: Incomplete Data
8Z(2) = Reporting Bias: Selective Outcomes
9X = Discussion: Limitations
10X = Conflict-of-Interest Statement
10Z = Other Bias: Funder Influence

For every item, apply the criteria and decision rules from CRIME-Q_CODEBOOK_FOR_NOTEBOOKLM.md.

Columns must be exactly:
Study, Study_Title,
1X_SCORE, 1X_JUSTIFICATION, 1X_VERBATIM,
3X_SCORE, 3X_JUSTIFICATION, 3X_VERBATIM,
3Y_SCORE, 3Y_JUSTIFICATION, 3Y_VERBATIM,
3Z_SCORE, 3Z_JUSTIFICATION, 3Z_VERBATIM,
4Y_SCORE, 4Y_JUSTIFICATION, 4Y_VERBATIM,
5X_SCORE, 5X_JUSTIFICATION, 5X_VERBATIM,
5Y_SCORE, 5Y_JUSTIFICATION, 5Y_VERBATIM,
5Z(1)_SCORE, 5Z(1)_JUSTIFICATION, 5Z(1)_VERBATIM,
5Z(2)_SCORE, 5Z(2)_JUSTIFICATION, 5Z(2)_VERBATIM,
5Z(3)_SCORE, 5Z(3)_JUSTIFICATION, 5Z(3)_VERBATIM,
6X_SCORE, 6X_JUSTIFICATION, 6X_VERBATIM,
7X_SCORE, 7X_JUSTIFICATION, 7X_VERBATIM,
7Z(1)_SCORE, 7Z(1)_JUSTIFICATION, 7Z(1)_VERBATIM,
7Z(2)_SCORE, 7Z(2)_JUSTIFICATION, 7Z(2)_VERBATIM,
8X_SCORE, 8X_JUSTIFICATION, 8X_VERBATIM,
8Z(1)_SCORE, 8Z(1)_JUSTIFICATION, 8Z(1)_VERBATIM,
8Z(2)_SCORE, 8Z(2)_JUSTIFICATION, 8Z(2)_VERBATIM,
9X_SCORE, 9X_JUSTIFICATION, 9X_VERBATIM,
10X_SCORE, 10X_JUSTIFICATION, 10X_VERBATIM,
10Z_SCORE, 10Z_JUSTIFICATION, 10Z_VERBATIM.

SCORE must be exactly one of: Yes, No, Partly, Unclear, NA.
JUSTIFICATION must be one concise sentence explaining the CRIME-Q score.
VERBATIM must be an exact quote from the target paper with a location tag, or exactly NOT REPORTED IN PAPER.

Before filling a row, identify the target PDF by filename. Do not use another study's paper to fill that row.

Do not add extra columns.
Do not leave any cells blank.
Do not summarize.
```
