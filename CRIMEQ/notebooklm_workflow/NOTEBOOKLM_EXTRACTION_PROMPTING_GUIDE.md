# NotebookLM Extraction Prompting Guide

These notes summarize practical lessons from building and testing a NotebookLM extraction workflow. They are written for researchers, students, and AI assistants adapting the pattern to other projects.

## Core Principle

NotebookLM is useful when the task is constrained like a data-entry job. It performs best when the notebook contains a small, explicit source set and the prompt tells it exactly what sources, rows, columns, score values, evidence rules, and stopping conditions to use.

Do not rely on general instructions such as "extract the data" or "make a table." Name the files, name the rows, name the columns, define allowed values, and define what to do when information is missing.

## Recommended File Set

Use separate files for stable rules and batch-specific prompts.

Recommended shared sources:

- `study_manifest.md`: study keys, filenames, article titles, DOI/source, and row order.
- `codebook.md`: item definitions, response options, and scoring rules.
- `calibration_rules.md`: general decision rules for common ambiguities and failure modes.
- `column_template.md`: exact output columns in exact order.
- `general_instructions.md`: source-use rules, missing-information rules, and evidence rules.

Recommended prompt files:

- One prompt per extraction batch.
- Keep prompts short enough that users can copy/paste them without editing.
- Put the target filenames and row order directly in the prompt.

Do not include completed target-study answers, worked examples from the target set, or validation labels in the NotebookLM sources or public prompts.

## Source Preparation

Use short, stable filenames. A good pattern is `LastNameYear.pdf`, such as `Ortega2026.pdf`.

The manifest should map each short study key to:

- exact uploaded filename,
- exact article title,
- citation or DOI/source,
- expected row order.

Ask NotebookLM to verify access before extraction by finding each exact article title. If a target PDF is missing or unreadable, the model should stop instead of silently filling a row from memory or from another source.

## Output Destination

State the output destination in the first lines of the prompt.

For chat tests:

- Say: "Write the answer in this chat only."
- Say: "Do not create a Google Sheet, Studio Data Table, note, report, or downloadable file."
- Prefer one Markdown table when the user needs a copy-paste table from NotebookLM chat.
- Say: "Return only the Markdown table, with no narrative before or after it."
- State the expected physical shape, for example: "exactly one header row, one separator row, and five data rows."
- Use TSV only when the downstream parser truly requires TSV. NotebookLM may collapse TSV into one physical line, so always verify that every study is on its own line before using it.

For Studio/Data Table tests:

- Say: "Create a Studio Data Table named ..."
- Still include the full column template and row-order rules.
- Expect wide tables to be fragile. If rows are omitted, reduce batch size.

For Google Sheets-style extraction:

- Make the prompt say "Google Sheet or Studio Data Table" only if that is acceptable.
- If the tool writes in chat instead, test whether the chat table is easier to copy/export than forcing sheet creation.
- Do not mix destination instructions. A prompt that asks for both chat output and a sheet-like output often produces the wrong destination.

## Batch Size

Wide extraction tables are hard for NotebookLM. A table with many rows and many evidence fields can cause omitted rows, truncated outputs, or simplified columns.

Practical strategy:

- Use 1 or 2 studies per prompt for highly detailed extraction.
- Use 5-study Markdown-table prompts after the output schema is stable; this is a useful compromise between reproducibility and row completeness.
- Use a clean notebook for each five-study batch. Do not keep old instruction or calibration sources in the same notebook.
- Use all-study prompts only as stress tests or when the output is chat-only. Expect lower evidence completeness and more scoring drift.
- If a 5-study table loses rows, split into smaller prompts rather than adding more wording.

## Column Design

Use one fixed column template. Put it in a shared source and repeat the critical rule in each prompt.

For item-based assessments, use the item ID itself as the score column when possible:

- Good: `1X`, `1X_JUSTIFICATION`, `1X_VERBATIM`
- Avoid: `ITEM_1X_SCORE`
- Avoid: `1X_SCORE` if the downstream sheet expects bare item IDs
- Preserve parentheses in item IDs such as `5Z(1)` and `7Z(2)`.

Explicitly forbid generic replacement columns such as `Randomization`, `Blinding`, `Power Calculation`, or `Animal Characteristics` when the rubric requires item IDs.

## Evidence Rules

Require evidence for every scored item.

A useful pattern:

- Score cell: one allowed value only.
- Justification cell: one concise sentence explaining the score.
- Verbatim cell: exact quote plus location tag, or one exact missing-information phrase.

Define invalid evidence patterns. For example:

- location-only cells are invalid,
- `See Table 1` is invalid,
- citation markers alone are invalid,
- "not available in source context" is invalid if the source is an uploaded PDF.

Use one missing-information phrase everywhere, such as `NOT REPORTED IN PAPER`.

## Wording That Helped

Effective wording patterns:

- "Use ONLY these uploaded study PDFs for this table."
- "Do not use other papers in the notebook to score a target study."
- "Before creating the table, verify that you can read each PDF by finding the exact article title."
- "If any PDF is unavailable, stop and report only: Source access failed for: [filename]."
- "Use exactly the columns in `column_template.md`."
- "The item-ID columns are the score columns."
- "Do not create columns beginning with `ITEM_`, columns ending in `_SCORE`, or columns that remove parentheses from item IDs."
- "Every verbatim cell must contain quoted words plus a location tag, or exactly `NOT REPORTED IN PAPER`."
- "Do not summarize."
- "Return one copy-paste Markdown table only."
- "Include exactly one header row, one separator row, and N data rows."
- "If duplicate calibration sources exist, use the newest UPDATED calibration rules source."

## Calibration Rules

A codebook often needs a second file with general calibration rules. This file should clarify recurring ambiguities without giving answers for the target studies.

Good calibration rules describe how to interpret the rubric, for example:

- define the appraisal scope before item scoring starts, especially when the
  paper includes secondary molecular, biochemical, histological, hormonal, or
  mechanistic experiments that are outside the target extraction;
- randomization alone does not prove baseline balance,
- group size reporting is not a sample-size calculation,
- separate rooms can introduce a room confound,
- partial blinding should not be generalized to all outcomes,
- automated measurement does not automatically mean assessor blinding,
- future-directions language is not the same as acknowledging a limitation.
- unclear manual or live outcome assessment should not be scored as unblinded unless the paper supports that inference,
- attrition judgments should compare allocated animals with analyzed animals across methods, results, figures, legends, and denominators,
- limitation judgments should search Discussion and Conclusion sections for concrete caveats even when there is no formal limitations heading,
- for scoped appraisals, limitations should count only when they affect the target domain, such as behavioral assays, acoustic/music delivery, exposure/control conditions, or interpretation of behavioral outcomes.

Calibration rules should be generic and portable. They should not say how a named target study should be scored.

## Common Failure Modes

Observed NotebookLM failure modes:

- It writes a table in chat instead of creating a sheet.
- It creates a Studio artifact but keeps only some rows from a very wide table.
- It creates a Google Sheet or Studio artifact when the test needs chat output.
- It collapses TSV rows into one physical line, especially for very wide tables.
- It renames columns, especially by adding `ITEM_` or `_SCORE`.
- It removes parentheses from item IDs, such as changing `5Z(1)` to `5Z1`.
- It omits metadata columns such as `Study_Title` unless they are named directly in the prompt.
- It uses a page/table location as verbatim evidence without quoted words.
- It inserts standalone citation-number cells into copied table text.
- It uses evidence from the wrong paper when many related sources are in one notebook.
- It reports "not available in source context" instead of treating the uploaded PDF as the source.
- It follows an older uploaded instruction source if duplicate source versions remain in the notebook.

Countermeasures:

- Reduce batch size.
- Use a manifest and exact row order.
- Repeat the most important column and evidence constraints in the prompt itself.
- Ask for a source-access precheck.
- Use a final self-check list.
- Keep shared source files short and non-conflicting.
- Remove or avoid stale versions of instruction files in the same notebook.
- Prefer Markdown tables for copy-paste chat output; use TSV only after checking physical line breaks.
- Explicitly require `Study_Key` and `Study_Title` as the first two columns.
- If stale rule sources cannot be removed, tell NotebookLM to use the newest UPDATED source.

## Prompt Structure

A robust prompt usually follows this order:

1. Output destination and format.
2. Target source filenames.
3. Shared instruction filenames.
4. Source-access precheck.
5. Required row order.
6. Item meanings or variables to extract.
7. Column template rule.
8. Allowed values and evidence rules.
9. Prohibitions and missing-information phrase.
10. Final self-check.

## QA Workflow

After NotebookLM produces output:

1. Confirm the row count and row order.
2. Confirm the header exactly matches the template, including metadata columns such as `Study_Title`.
3. Check that all score cells use allowed values.
4. Check that verbatim cells contain quoted words plus a location tag, or the exact missing-information phrase.
5. Manually review known difficult items and evidence cells before using the extraction.
6. Evaluate outputs outside NotebookLM using the project's independent review process, if one exists.
7. Record mismatches by item and failure type.
8. Revise only general prompt wording or general calibration rules for repeated, portable failures.
9. Stop tuning when improvements begin trading one item error for another; keep the stable prompt and handle residual errors by manual review.
10. Do not add target-study answers to public prompts or NotebookLM sources.

Manual review is not a failure of the workflow. For detailed appraisal tasks,
NotebookLM can produce a structured first pass, but human review should remain
part of the method for ambiguous items and evidence quality.

## Reproducibility Notes

For public supplementary materials, provide the prompts, manifest, codebook, calibration rules, and column template. Do not redistribute copyrighted PDFs unless you have permission. Instead, tell users how to obtain the articles and how to rename files to match the manifest.

Keep the public workflow runnable by a person who has only NotebookLM, the article PDFs they obtained independently, and the supplementary prompt files.
