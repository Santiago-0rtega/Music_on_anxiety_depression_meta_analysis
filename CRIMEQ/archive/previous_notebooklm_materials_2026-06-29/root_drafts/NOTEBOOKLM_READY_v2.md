# NotebookLM Ready - CSV/Markdown Version

## ✅ Files Ready for NotebookLM

Since NotebookLM cannot read Excel files, all files are now available in CSV and Markdown formats:

### 1. **CRIME-Q_Codebook_v2.md** ← Attach this to NotebookLM
- Detailed assessment criteria for all 20 CRIME-Q items
- Format: Markdown (readable by NotebookLM)
- Structure: Item ID | Domain | Construct | Question | Detailed Criteria

### 2. **CRIME-Q_Assessment_Template_v2.csv** ← Attach this to NotebookLM
- Empty template with all 62 column headers
- 20 rows (one per study)
- Format: CSV (comma-separated)
- Columns: Study_ID, Study_Title, then 20 items × 3 columns each (SCORE, JUSTIFICATION, VERBATIM)

### 3. **CRIME-Q_Codebook_v2.csv** (backup)
- Same codebook as .md file but in CSV format

---

## 🎯 How to Use with NotebookLM

### Step 1: Copy the prompt
File: **NOTEBOOKLM_SHORT_PROMPT_v2.txt**
- Copy the entire text

### Step 2: Upload to NotebookLM
1. Upload 20 study PDFs
2. Attach: `CRIME-Q_Codebook_v2.md` (for assessment criteria)
3. Attach: `CRIME-Q_Assessment_Template_v2.csv` (for reference)
4. Paste the prompt from **NOTEBOOKLM_SHORT_PROMPT_v2.txt**

### Step 3: NotebookLM outputs
- CSV format (comma or tab-separated)
- 20 studies × 20 items × 3 columns = 1,200 data cells

### Step 4: Import results
- Copy NotebookLM's CSV output
- Import into Google Sheets or Excel
- Or paste into the original Excel template if preferred

---

## 📄 File Formats

| File | Format | Purpose |
|------|--------|---------|
| CRIME-Q_Codebook_v2.md | Markdown | Attach to NotebookLM for assessment criteria |
| CRIME-Q_Assessment_Template_v2.csv | CSV | Attach to NotebookLM as reference template |
| CRIME-Q_Codebook_v2.csv | CSV | Backup codebook (optional) |
| NOTEBOOKLM_SHORT_PROMPT_v2.txt | Text | Copy & paste into NotebookLM |

---

## 📋 Column Structure

Each CRIME-Q item has 3 columns:

```
{ItemID}_{Domain}_SCORE, {ItemID}_{Domain}_JUSTIFICATION, {ItemID}_{Domain}_VERBATIM

Examples:
1X_Peer review_SCORE, 1X_Peer review_JUSTIFICATION, 1X_Peer review_VERBATIM
3X_Animals reporting_SCORE, 3X_Animals reporting_JUSTIFICATION, 3X_Animals reporting_VERBATIM
5X_Music reporting_SCORE, 5X_Music reporting_JUSTIFICATION, 5X_Music reporting_VERBATIM
...
```

---

## 📊 Assessment Data

- **20 studies**: Camargo_2013_PSYN through Terzioglu_2020_CMJ
- **20 CRIME-Q items**: 8 QoR + 2 MQ + 10 RoB
- **3 columns per item**: Score + Justification + Verbatim
- **Total**: 20 × 20 × 3 = 1,200 data cells

---

## 🚀 Quick Start

1. **Copy prompt**: `NOTEBOOKLM_SHORT_PROMPT_v2.txt`
2. **Upload PDFs** to NotebookLM
3. **Attach files**:
   - `CRIME-Q_Codebook_v2.md` (criteria)
   - `CRIME-Q_Assessment_Template_v2.csv` (template reference)
4. **Paste prompt** into NotebookLM
5. **Get CSV output** from NotebookLM
6. **Import** into your spreadsheet

---

## 📝 Key Rules for Assessment

1. **Score options**: Yes, No, Partly, Unclear, or NA
2. **Justification**: Keep to 1-2 sentences
3. **Verbatim**: Include [page X] or [section name]
4. **Assessment level**: STUDY (not cohort)
5. **Reference**: Use CRIME-Q_Codebook_v2.md for criteria

---

## ✨ Improvements in v2

- ✅ Removed Excel dependency (NotebookLM compatible)
- ✅ Uses Markdown for human-readable codebook
- ✅ Uses CSV for structured data
- ✅ Ready to paste prompt directly to NotebookLM
- ✅ Output can be imported directly to Google Sheets

---

**Status**: Ready for NotebookLM  
**Format**: CSV + Markdown (no Excel)  
**Studies**: 20  
**Items**: 20  
**Data cells**: 1,200
