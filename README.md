This repository hosts the data and analytical workflow for a systematic review and multilevel meta-analysis of music exposure effects on anxiety- and depression-like behavior in rodents.

In the `data/` folder:
- `extraction_mm_251105.xlsx` contains the full data extraction, coding metadata, and complete extracted dataset.
- `db251124.csv` contains the cleaned database used for effect size estimation.
- `db_effect_sizes.csv` contains the processed database with the three calculated effect sizes used in the analyses.

In the `book/` folder, all analytical code is provided and organized into multiple Quarto (`.qmd`) files corresponding to different parts of the workflow.

In the `CRIMEQ/` folder:
- `notebooklm_workflow/` contains the finalized NotebookLM CRIME-Q extraction materials, organized as one clean five-study batch notebook per run.
- `notebooklm_workflow/batches/*/pdfs/` contains local ignored PDFs organized by batch for private testing.
- `archive/` contains previous NotebookLM prompt and instruction drafts, old working-upload scaffolding, and dated zip archives.



