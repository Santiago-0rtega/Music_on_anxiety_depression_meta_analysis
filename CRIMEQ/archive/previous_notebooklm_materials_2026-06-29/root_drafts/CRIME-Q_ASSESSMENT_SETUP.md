# Music CRIME-Q Assessment Setup - Study-Level Assessment

## Overview

A new study-level (not cohort-level) CRIME-Q assessment template has been created for your 20 rodent music studies.

**File**: `data/MUSIC-CRIME-Q_RoB_assessment_v2.xlsx`

---

## Key Changes from Old Assessment

| Aspect | Old (Cohort-based) | New (Study-level) |
|--------|-------------------|------------------|
| **Structure** | 49 rows (one per cohort) | 20 rows (one per study) |
| **Columns per item** | 1 column (score only) | 3 columns (score + justification + verbatim) |
| **Total columns** | ~27 | 62 (Study_ID + Title + 20 items × 3) |
| **Assessment focus** | Multiple behavioral contrasts per study | Single assessment per paper |
| **Data source** | Existing partial assessments | Start from zero (fresh assessment) |

---

## File Structure: `MUSIC-CRIME-Q_RoB_assessment_v2.xlsx`

### Sheet 1: **Study Roster** 
- Lists all 20 unique studies
- Maps Study_ID to Study_Title

### Sheet 2: **Codebook**
- 20 CRIME-Q items with:
  - Item ID (1X, 3X, 3Y, etc.)
  - Domain (Peer review, Animals: reporting, Music reporting, etc.)
  - Construct (QoR, MQ, RoB)
  - Question for each item

### Sheet 3: **Assessment** ⭐ (Main Sheet)
- **Rows**: 20 studies (one per row)
- **Columns**: 62 total
  - Column 1: Study_ID
  - Column 2: Study_Title
  - Columns 3-62: 20 items × 3 columns each
    - `1X_Peer_review_SCORE`
    - `1X_Peer_review_JUSTIFICATION`
    - `1X_Peer_review_VERBATIM`
    - ... (repeat for all 20 items)

### Sheet 4: **Instructions**
- Short NotebookLM guidance
- Key rules for assessment
- Study list

---

## 20 Studies Included

From your roster (20 unique Study_IDs):

1. Camargo_2013_PSYN (1 cohort)
2. Chen_2019_BIOMEDRI (2 cohorts)
3. Cheng_2024_HLYN (4 cohorts)
4. Chikahisa_2007_BBR (8 cohorts)
5. Escribano_2014_APPANBSC (6 cohorts)
6. Flores_2018_NP (6 cohorts)
7. Freitas_2020_ECNE (2 cohorts)
8. Fu_2023_TRANSPSY (2 cohorts)
9. Fu_2025_TRANSPSY (1 cohort)
10. Krishnamurthy_2025_INDIANJTRADITKNOW (1 cohort)
11. Li_2010_BR (2 cohorts)
12. Milbratz_2017_ALN (2 cohorts)
13. Niehues_2011_BCNEURO (1 cohort)
14. Pangemanan_2024_PHJ (1 cohort)
15. Papadakakis_2019_BBR (2 cohorts)
16. Ren_2024_ASEAN (2 cohorts)
17. Rizzolo_2021_CC (1 cohort)
18. Saghari_2021_BIOINTERFACE (2 cohorts)
19. Sampaio_2017_PSYNEURO (2 cohorts)
20. Terzioglu_2020_CMJ (1 cohort)

**Note**: These 20 studies represent 49 cohorts total in your data extraction (ranging from 1-8 cohorts per study).

---

## 20 CRIME-Q Items (Study-Level Assessment)

| # | Item | Domain | Type |
|---|------|--------|------|
| 1 | 1X | Peer review | QoR |
| 2 | 3X | Animals: reporting | QoR |
| 3 | 3Y | Animals: technical quality | MQ |
| 4 | 3Z | Selection bias: baseline | RoB |
| 5 | 4Y | Sample size | QoR |
| 6 | **5X** | **Music reporting (CRITICAL)** | **QoR** |
| 7 | **5Y** | **Music technical quality (CRITICAL)** | **MQ** |
| 8 | 5Z(1) | Randomization | RoB |
| 9 | 5Z(2) | Random housing | RoB |
| 10 | 5Z(3) | Outcome assessment | RoB |
| 11 | 6X | Ethics compliance | QoR |
| 12 | 7X | Blinding: reporting | QoR |
| 13 | 7Z(1) | Experimenter blinding | RoB |
| 14 | 7Z(2) | Assessor blinding | RoB |
| 15 | 8X | Methods-results alignment | QoR |
| 16 | 8Z(1) | Attrition bias | RoB |
| 17 | 8Z(2) | Selective reporting | RoB |
| 18 | 9X | Limitations | QoR |
| 19 | 10X | Conflict-of-interest | QoR |
| 20 | 10Z | Funder influence | RoB |

**Removed items**: 2X, 2Y (bench-top/lab work - not applicable to behavioral animal studies)

---

## How to Use with NotebookLM

### Short Prompt to Give NotebookLM:

> "Read the Instructions sheet in the attached assessment template. For each of 20 animal studies, assess 20 CRIME-Q items. For each item: 
> 1. Provide SCORE (Yes/No/Partly/Unclear/NA)
> 2. Write JUSTIFICATION (1-2 sentences explaining the score)
> 3. Provide VERBATIM (direct quote with [page X] reference)
> 
> Output as a Google Sheet (tab-separated) that can be directly pasted into Google Sheets. Reference the Codebook sheet for detailed assessment criteria. Assessment is at STUDY level (not cohort level)."

### Data Format NotebookLM Should Output:

Tab-separated values (TSV) table:
```
Study_ID | Study_Title | 1X_Peer_review_SCORE | 1X_Peer_review_JUSTIFICATION | 1X_Peer_review_VERBATIM | 3X_Animals_reporting_SCORE | ...

Camargo_2013_PSYN | Camargo_2013_PSYN | Yes | Published in peer-reviewed journal | [cover page] Title in Psychoneuroendocrinology | Partly | Study reports strain, sex, age but not housing | [page 2, Methods] C57BL/6 mice...
```

---

## Column Structure Example

Each of the 20 CRIME-Q items follows this pattern:

```
{ItemID}_{Domain}_SCORE | {ItemID}_{Domain}_JUSTIFICATION | {ItemID}_{Domain}_VERBATIM
1X_Peer_review_SCORE | 1X_Peer_review_JUSTIFICATION | 1X_Peer_review_VERBATIM
3X_Animals_reporting_SCORE | 3X_Animals_reporting_JUSTIFICATION | 3X_Animals_reporting_VERBATIM
5X_Music_reporting_SCORE | 5X_Music_reporting_JUSTIFICATION | 5X_Music_reporting_VERBATIM
... (20 items total)
```

---

## Key Assessment Rules

1. **Study-level assessment**: One assessment per study (not per cohort)
2. **Keep justification short**: 1-2 sentences max
3. **Include page references**: VERBATIM must have [page X] or [section]
4. **Use Partly when incomplete**: Not all criteria met, but some present
5. **NA when not applicable**: Item not relevant to this study
6. **Refer to Codebook sheet**: For detailed criteria for each item

---

## Next Steps

1. ✅ **Assessment template created** and ready in `data/MUSIC-CRIME-Q_RoB_assessment_v2.xlsx`
2. ⏭️ **Upload 20 study PDFs** to NotebookLM
3. ⏭️ **Provide short prompt** (above) to NotebookLM
4. ⏭️ **Copy output** (TSV format) from NotebookLM into the Assessment sheet
5. ⏭️ **Verify and review** completed assessments

---

## Files Related to This Assessment

- **New template** (study-level): `data/MUSIC-CRIME-Q_RoB_assessment_v2.xlsx`
- **Old template** (cohort-level): `data/MUSIC-CRIME-Q_RoB_assessment.xlsx` (keep for reference)
- **Roster**: `data/crime_q_cohort_roster.csv` (maps Study_ID to Cohort_IDs)
- **Instructions**: `NOTEBOOKLM_CRIME-Q_Instructions.md` (detailed guidance)
- **This setup guide**: `CRIME-Q_ASSESSMENT_SETUP.md`

---

**Last Updated**: June 26, 2026  
**Assessment Type**: Study-level (one row per paper, 20 items per study, 3 columns per item)  
**Total Data Cells**: 20 studies × 20 items × 3 columns = 1,200 cells
