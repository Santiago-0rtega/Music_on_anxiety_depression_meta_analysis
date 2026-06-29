# NotebookLM CRIME-Q Extraction Supplement

This folder contains public, reproducible NotebookLM materials for extracting
study-level CRIME-Q assessments from animal music-intervention studies.

PDFs are not redistributed here. Users should obtain each article through lawful
library, publisher, institutional, or open-access routes, then upload their own
copies to NotebookLM.

## Folder Layout

- `shared_rules/`
  - codebook and general instructions used for every batch
  - wide Google Sheet output template
- `batch_01_Camargo2013_to_Escribano2014/`
- `batch_02_Flores2018_to_Krishnamurthy2025/`
- `batch_03_Li2010_to_Papadakakis2019/`
- `batch_04_Ren2024_to_Terzioglu2020/`

Each batch folder contains:

- `study_manifest.md`: the five studies to upload
- `short_prompt.md`: the short prompt to paste/run in NotebookLM after upload
- `batch_prompt.md`: a longer fallback prompt with the same requirements
- `part_*_prompt_*.md`: smaller prompts for 1-2 studies at a time; use these
  when the wide five-study table omits rows or uses placeholder text

## Recommended NotebookLM Workflow

1. Create one NotebookLM notebook for one batch of five studies.
2. Upload the five study PDFs for that batch.
3. Upload that batch folder's `study_manifest.md`.
4. Upload all files from `shared_rules/`.
5. Paste the batch `short_prompt.md` into NotebookLM's chat box and run it. If
   the output omits rows, run the `part_*` prompts instead.
6. Paste/export the resulting Google-Sheets-ready table(s) into Google Sheets
   if NotebookLM does not create a Sheet directly.
7. Export the completed sheet as CSV/TSV if further analysis is needed.

The requested output is one wide sheet per batch: one header row plus five study
rows. Each study row contains a score, justification, and verbatim evidence cell
for all 20 CRIME-Q items.

## Prompt Length

Use `short_prompt.md` first. It assumes the study PDFs and shared rules have
already been uploaded as notebook sources, including the batch `study_manifest.md`.
The longer `batch_prompt.md` is a fallback/reference version if the short prompt
does not give enough instruction.

In testing, very wide five-study outputs may exceed NotebookLM Studio's practical
capacity. The more reliable workflow is one five-study notebook with several
`part_*` prompts, each extracting one or two study rows using the same wide
column template.
