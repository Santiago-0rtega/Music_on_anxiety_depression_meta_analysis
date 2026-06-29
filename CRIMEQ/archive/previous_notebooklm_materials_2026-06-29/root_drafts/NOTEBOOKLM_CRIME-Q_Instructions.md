# NotebookLM Instructions: Music CRIME-Q Assessment

## Task
Assess 20 animal music intervention studies using the CRIME-Q tool (music-adapted, study-level assessment).

## Quick Start
1. **Read the complete instruction manual**: See the "Instructions" sheet in `data/MUSIC-CRIME-Q_RoB_assessment_v2.xlsx`
2. **Reference the codebook**: See "Codebook" sheet for detailed criteria for each of 20 items
3. **Output format**: Write a **GOOGLE SHEET** (tab-separated values) that can be directly pasted into Google Sheets

## Output Structure

For each of the 20 studies and 20 CRIME-Q items, provide **3 columns per item**:

1. **SCORE**: Yes, No, Partly, Unclear, or NA
2. **JUSTIFICATION**: 1-2 sentences explaining why you gave this score
3. **VERBATIM**: Direct quote from the paper with [page X] or [section name]

### Example Output Format (First 2 Items):

```
Study_ID | Study_Title | 1X_Peer_review_SCORE | 1X_Peer_review_JUSTIFICATION | 1X_Peer_review_VERBATIM | 3X_Animals_reporting_SCORE | 3X_Animals_reporting_JUSTIFICATION | 3X_Animals_reporting_VERBATIM | ...

AuthorName_YYYY | Title of Paper | Yes | Published in peer-reviewed journal Psychoneuroendocrinology | [cover page] Psychoneuroendocrinology Vol 146, pp 105-113 | Partly | Study reports strain (C57BL/6), sex (male), age (10-12 weeks), and n per group but not housing enrichment details | [page 2, Methods] Male C57BL/6 mice (n=12 per group), aged 10-12 weeks, housed 4 per cage | ...
```

## Key Rules

1. **Reference the Codebook sheet** for detailed assessment criteria for each item
2. **Keep JUSTIFICATION SHORT**: 1-2 sentences max
3. **VERBATIM must include** [page X], [Methods], [Results], or [section name] reference
4. For **missing information**, note what was NOT reported
5. Use **NA** when item is not applicable
6. Use **Partly** when criteria are incomplete (not all elements present)
7. **Be consistent**: 
   - **Yes** = fully meets all criteria
   - **Partly** = partially meets criteria  
   - **No** = does not meet criteria
   - **Unclear** = insufficient information to assess
   - **NA** = not applicable to this study

## 20 Items to Assess

| Item | Domain | Item | Domain |
|------|--------|------|--------|
| 1X | Peer review | 5Z(3) | Detection bias: outcome assessment |
| 3X | Animals reporting | 6X | Ethical compliance |
| 3Y | Animals technical quality | 7X | Blinding reporting |
| 3Z | Selection bias: baseline | 7Z(1) | Performance bias: experimenter blinding |
| 4Y | Sample size | 7Z(2) | Detection bias: assessor blinding |
| **5X** | **Music reporting (CRITICAL)** | 8X | Methods-results alignment |
| **5Y** | **Music technical quality (CRITICAL)** | 8Z(1) | Attrition bias: incomplete data |
| 5Z(1) | Selection bias: randomization | 8Z(2) | Reporting bias: selective outcomes |
| 5Z(2) | Performance bias: random housing | 9X | Discussion: limitations |
| | | 10X | Conflict-of-interest statement |
| | | 10Z | Other bias: funder influence |

*Items 5X and 5Y are CRITICAL for music studies*

## Deliverable

Output as **tab-separated values (TSV)** formatted as a table that can be directly pasted into Google Sheets:

- **All 20 studies** (one row each)
- **All 20 CRIME-Q items** (3 columns per item)
- **Total data: 20 studies × 20 items × 3 columns = 1,200 cells**

## Study List (20 Studies)

1. Camargo_2013_PSYN
2. Chen_2019_BIOMEDRI
3. Cheng_2024_HLYN
4. Chikahisa_2007_BBR
5. Escribano_2014_APPANBSC
6. Flores_2018_NP
7. Freitas_2020_ECNE
8. Fu_2023_TRANSPSY
9. Fu_2025_TRANSPSY
10. Krishnamurthy_2025_INDIANJTRADITKNOW
11. Li_2010_BR
12. Milbratz_2017_ALN
13. Niehues_2011_BCNEURO
14. Pangemanan_2024_PHJ
15. Papadakakis_2019_BBR
16. Ren_2024_ASEAN
17. Rizzolo_2021_CC
18. Saghari_2021_BIOINTERFACE
19. Sampaio_2017_PSYNEURO
20. Terzioglu_2020_CMJ

---

**Template Location**: `data/MUSIC-CRIME-Q_RoB_assessment_v2.xlsx`
- Codebook sheet: Detailed criteria + music examples
- Assessment sheet: 62 columns (ready for filling)
- Instructions sheet: Full guidance
