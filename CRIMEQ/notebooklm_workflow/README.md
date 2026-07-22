# NotebookLM CRIME-Q Five-Study Workflow

This workflow uses one clean NotebookLM notebook per five-study batch. Each
notebook should contain only the five target PDFs and one current copy of each
shared rule file. Do not reuse a notebook that contains older prompt, codebook,
or calibration sources.

This CRIME-Q adaptation is scoped to behavioral assays and in vivo
music/acoustic exposure. It is not a whole-paper appraisal of unrelated
molecular, histological, biochemical, hormonal, or mechanistic experiments
unless those details directly affect behavioral outcomes or acoustic exposure.

The NotebookLM output is treated as a first-pass extraction. A human reviewer
should manually check formatting, evidence, and recurring difficult CRIME-Q
items before using the table.

## Sources To Upload Per Batch

Upload exactly:

- the five study PDFs for the batch, renamed according to the batch manifest
- the batch-specific `study_manifest.md` from `batches/`
- `GENERAL_NOTEBOOKLM_INSTRUCTIONS.md`
- `CRIME-Q_CODEBOOK_FOR_NOTEBOOKLM.md`
- `CRIME-Q_NOTEBOOKLM_CALIBRATION_RULES.md`
- `WIDE_SHEET_COLUMN_TEMPLATE.md`

PDFs are not redistributed in public supplementary materials. Users should
obtain the articles independently and name them according to the manifest.
For local testing in this workspace, PDFs are organized under each batch's
ignored `pdfs/` subfolder.

## Folder Layout

- `batches/`: one folder per five-study batch, each containing the
  `study_manifest.md` to upload with that batch. Local testing PDFs, when
  present, are kept in ignored `pdfs/` subfolders.
- `prompts_5study_chat_table/`: one manual copy/paste prompt per batch.
- `shared_rules/`: the codebook, calibration rules, general NotebookLM
  instructions, and wide column template.
- `MANUAL_REVIEW_CHECKLIST.md`: checks to apply after NotebookLM returns each
  table.

## Prompt Order

Use the Markdown-table prompts in `prompts_5study_chat_table/`:

1. `prompt_01_Camargo2013_to_Escribano2014_table.md`
2. `prompt_02_Flores2018_to_Krishnamurthy2025_table.md`
3. `prompt_03_Li2010_to_Papadakakis2019_table.md`
4. `prompt_04_Ren2024_to_Terzioglu2020_table.md`

Run one prompt manually in NotebookLM, copy the resulting table, and review it
before moving to the next batch.

Each generated table should have exactly five study rows and the 62 columns
defined in `WIDE_SHEET_COLUMN_TEMPLATE.md`. The score columns are the bare
CRIME-Q item IDs such as `1X` and `5Z(1)`, not `1X_SCORE` or
`ITEM_1X_SCORE`.

## Manual Review

After each NotebookLM table, use `MANUAL_REVIEW_CHECKLIST.md`.

Review is especially important for:

- `9X` limitations
- `10Z` funder influence
- `7Z(2)` assessor blinding
- `8Z(1)` attrition
- verbatim evidence cells that contain only a page, table, or figure location

Do not add target-study answers or worked examples to public prompts or
NotebookLM sources.
