# Wide Google Sheet Column Template

Create one Google Sheet or Studio Data Table per prompt with exactly one
worksheet/table. The output must have one header row and the exact number of
study rows requested in the prompt.

Do not replace these CRIME-Q item columns with generic extraction fields such as
Randomization, Blinding, Power Calculation, or Animal Characteristics. The output
must use the item IDs below exactly.

The item-ID column itself is the score column. For example, column `1X`
contains the score for item `1X`; there is no column named `1X_SCORE`.

Do not create columns beginning with `ITEM_`. Do not create columns ending in
`_SCORE`. Preserve parentheses in `5Z(1)`, `5Z(2)`, `5Z(3)`, `7Z(1)`,
`7Z(2)`, `8Z(1)`, and `8Z(2)`.

Use these columns in this exact order:

```text
Study,Study_Title,1X,1X_JUSTIFICATION,1X_VERBATIM,3X,3X_JUSTIFICATION,3X_VERBATIM,3Y,3Y_JUSTIFICATION,3Y_VERBATIM,3Z,3Z_JUSTIFICATION,3Z_VERBATIM,4Y,4Y_JUSTIFICATION,4Y_VERBATIM,5X,5X_JUSTIFICATION,5X_VERBATIM,5Y,5Y_JUSTIFICATION,5Y_VERBATIM,5Z(1),5Z(1)_JUSTIFICATION,5Z(1)_VERBATIM,5Z(2),5Z(2)_JUSTIFICATION,5Z(2)_VERBATIM,5Z(3),5Z(3)_JUSTIFICATION,5Z(3)_VERBATIM,6X,6X_JUSTIFICATION,6X_VERBATIM,7X,7X_JUSTIFICATION,7X_VERBATIM,7Z(1),7Z(1)_JUSTIFICATION,7Z(1)_VERBATIM,7Z(2),7Z(2)_JUSTIFICATION,7Z(2)_VERBATIM,8X,8X_JUSTIFICATION,8X_VERBATIM,8Z(1),8Z(1)_JUSTIFICATION,8Z(1)_VERBATIM,8Z(2),8Z(2)_JUSTIFICATION,8Z(2)_VERBATIM,9X,9X_JUSTIFICATION,9X_VERBATIM,10X,10X_JUSTIFICATION,10X_VERBATIM,10Z,10Z_JUSTIFICATION,10Z_VERBATIM
```

Each study row must contain all 20 CRIME-Q items. No cells should be blank.
