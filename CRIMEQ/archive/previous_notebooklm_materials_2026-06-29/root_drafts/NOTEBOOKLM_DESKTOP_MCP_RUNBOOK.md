# NotebookLM MCP Runbook for CRIME-Q Live Testing

This workflow uses the local `notebooklm-mcp` server at:

`C:\Users\zannt\OneDrive\Github repos\notebooklm-mcp`

The MCP drives the NotebookLM web UI through Playwright. NotebookLM has no public
API, so this depends on a logged-in local browser profile and can break if the
NotebookLM UI changes.

## Why this workflow is structured this way

1. The codebook must be a NotebookLM source. Upload `CRIME-Q_Detailed_Codebook_v3.md`.
2. The source manifest must be a NotebookLM source. Upload `NOTEBOOKLM_SOURCE_MANIFEST.md` because the study PDFs have UUID filenames.
3. Query one study at a time. A 20-study x 20-item x 3-cell single output is too likely to truncate or drift.
4. The primary output is a Google Sheet, not a Markdown table in chat.
5. Require exact quotes or `NOT REPORTED IN PAPER`. Citations alone are not enough.
6. Validate against the human gold standard with `score_notebooklm.py`.

## Step 0 - Wire in the MCP

If using Claude Code, add the MCP server:

```powershell
claude mcp add notebooklm -- uv run --directory "C:\Users\zannt\OneDrive\Github repos\notebooklm-mcp" notebooklm-mcp
```

If using Claude Desktop, copy the `notebooklm` block from:

`C:\Users\zannt\OneDrive\Github repos\notebooklm-mcp\claude_desktop_config.example.json`

into `%APPDATA%\Claude\claude_desktop_config.json`, then restart Claude Desktop.

Authenticate once if needed:

```powershell
uv run --directory "C:\Users\zannt\OneDrive\Github repos\notebooklm-mcp" notebooklm-mcp-auth
```

## Step 1 - Create the NotebookLM notebook

Create a notebook named:

`Music CRIME-Q appraisal`

Upload these 22 sources:

- all 20 PDFs in `References\`
- `CRIME-Q_Detailed_Codebook_v3.md`
- `NOTEBOOKLM_SOURCE_MANIFEST.md`

If local file upload through MCP fails, upload the PDFs/codebook/manifest through
the NotebookLM web UI once, then use the existing notebook ID for queries.

## Step 2 - Live calibration test

Run the per-study query from `NOTEBOOKLM_LIVE_TEST_PROMPT.md` for these first:

1. `Niehues_2011_BCNEURO`
2. `Pangemanan_2024_PHJ`
3. `Terzioglu_2020_CMJ`
4. `Chikahisa_2007_BBR`

These four cover the main failure modes: simple music/silence scoring,
outcome-dependent selection, n mismatch, dropped outcomes, genre-volume
confounding, litter/cage pseudoreplication, and multi-cohort study-level scoring.

For each query, replace `[STUDY_ID]` in `NOTEBOOKLM_LIVE_TEST_PROMPT.md`.

Expected NotebookLM deliverable:

- A Google Sheet named `CRIME-Q NotebookLM Live Test - [STUDY_ID]`.
- One worksheet/tab named exactly `[STUDY_ID]`.
- Four columns: `Item`, `SCORE`, `JUSTIFICATION`, `VERBATIM`.
- Twenty filled rows, one for each CRIME-Q item.

Expected chat response after the sheet is written:

```text
Study_ID: Niehues_2011_BCNEURO
Google Sheet: [link or sheet name]
Rows completed: 20
```

Do not accept a Markdown table in chat as the primary deliverable. Chat tables
are only a fallback if Google Sheets output is unavailable.

## Step 3 - Validate against gold standard

Export the completed Google Sheet tab as TSV/CSV for validation. Save it with
the `Study_ID` in the filename, or pass the `Study_ID` as the second argument.
Then run:

```powershell
python score_notebooklm.py Niehues_2011_BCNEURO.tsv
python score_notebooklm.py sheet_export.csv Niehues_2011_BCNEURO
```

The scorer reports:

- studies parsed and cells compared
- overall agreement
- per-item agreement
- every mismatch as `study | item | GOLD -> NotebookLM`
- missing/unparsed rows

## Step 4 - Iterate

For each mismatch, inspect whether the issue is:

- NotebookLM missed or paraphrased evidence.
- The prompt needs another calibration rule.
- The codebook is ambiguous.
- The PDF/source OCR caused a retrieval miss.

Tighten `NOTEBOOKLM_LIVE_TEST_PROMPT.md` or `CRIME-Q_Detailed_Codebook_v3.md`,
then rerun only the affected studies.

## Full study list

`Camargo_2013_PSYN, Chen_2019_BIOMEDRI, Cheng_2024_HLYN, Chikahisa_2007_BBR, Escribano_2014_APPANBSC, Flores_2018_NP, Freitas_2020_ECNE, Fu_2023_TRANSPSY, Fu_2025_TRANSPSY, Krishnamurthy_2025_INDIANJTRADITKNOW, Li_2010_BR, Milbratz_2017_ALN, Niehues_2011_BCNEURO, Pangemanan_2024_PHJ, Papadakakis_2019_BBR, Ren_2024_ASEAN, Rizzolo_2021_CC, Saghari_2021_BIOINTERFACE, Sampaio_2017_PSYNEURO, Terzioglu_2020_CMJ`

## Files that stay local for validation

- `data\MUSIC-CRIME-Q_GOLD-STANDARD_assessment.xlsx`
- `build_gold_standard.py`
- `score_notebooklm.py`

Do not upload the gold-standard file to NotebookLM during testing.
