# Reviewer-response audit: experimental units, sample sizes, variability, strain, sex, and the assumed VCV correlation

Repository: `Music_on_anxiety_depression_meta_analysis` (systematic review + multilevel meta-analysis of music exposure on anxiety-/depression-like behaviour in rodents).

This is a **read-only audit**. No existing analysis file was changed in a way that alters results; the only source-file edit is one additive line in `book/_quarto.yml` registering the new appendix (see §12). All findings below are tagged:

- **Directly supported by database** — read directly from `data/db251124.csv` / `data/db_effect_sizes.csv` / the extraction workbook.
- **Directly supported by primary paper** — read directly from the extracted full text of an included study.
- **Derived/calculated** — computed by this audit from the above (code shown or available in the accompanying scratch scripts).
- **Inference** — a reasonable but not directly documented interpretation.
- **Unclear / not reported** — the repository does not contain enough information to answer.

Companion files produced for this audit (see final table for the full list):
`reviewer_response_audit/repository_file_map.csv`, `CRIMEQ/independent_screening/reviewer_audit_exposure_unit.csv` (+ `_SUMMARY.md`), `CRIMEQ/independent_screening/reviewer_audit_codebook_prisma.md`, `book/correlation_sensitivity.qmd` (+ rendered `docs/correlation_sensitivity.html`, `data/sensitivity_r_overall_results.csv`, `data/sensitivity_r_anxiety_depression_contrast.csv`, `Plots/sensitivity_r_overall.pdf`/`.jpg`).

---

## 1. Project structure and analytical workflow

See `reviewer_response_audit/repository_file_map.csv` for the full machine-readable table. In brief, the workflow is:

`data/extraction_mm_251105.xlsx` (raw extraction + `metadata` codebook sheet) → `data/db251124.csv` (cleaned, 298 effect sizes × 90 columns) → `book/effect_size_calculation.qmd` (continuity corrections, `calculate_lnRR()`/`calculate_lnVR()`/`calculate_lnCVR()`) → `data/db_effect_sizes.csv` (298 × 97, adds `Cohort_ID`, `lnRR`/`lnVR`/`lnCVR` + variances) → `book/overall_effect.qmd` (VCV construction + 3 intercept-only `rma.mv()` models) → `book/uni_moderators.qmd` / `book/multi_moderator.qmd` (moderator models) → `book/main_figures.qmd`, `book/publication_bias.qmd`, `book/leave_one_out.qmd`, `book/Alluvial.qmd`, `book/crime_q.qmd` (figures/diagnostics). The CRIME-Q source-document workflow lives under `CRIMEQ/notebooklm_workflow/` (extraction prompts + `all_studies_manifest.md`) and `CRIMEQ/independent_screening/` (independent gold-standard screening + the page-numbered full-text extraction of all 20 included papers used in §3 below). **Directly supported by database/codebase.**

---

## 2. Sample-size terminology and requested summaries

**What `C_n`/`Ex_n` represent — Directly supported by codebook.** The `extraction_mm_251105.xlsx` `metadata` sheet defines them verbatim as: `C_n` = "Sample size of control group (**number of animals**)"; `Ex_n` = "Sample size of experimental group (**number of animals**)". They are defined as counts of individual animals — not cages, litters, or dams — and the codebook contains no cage/litter-level sample-size field at all (confirmed: no column name in `data/db251124.csv` contains "cage" or "room").

**Distinguishing units (Directly supported by database, except statistical-unit judgment which is per-study — see §3):**
- *Number of animals contributing to an outcome* = `C_n`/`Ex_n` as coded.
- *Treatment/exposure unit* = whatever physically received the independently assignable music exposure — **this is not recorded as its own field in the extraction database** and must be read from the primary paper (§3); it is frequently a cage or room rather than an individual animal.
- *Behavioural measurement unit* = the animal (or occasionally cage) actually scored in the behavioural test — also not a dedicated database field; assessed per-study in §3.
- *Social housing/group size* = animals per cage — not extracted as a database field; assessed per-study in §3 from the primary text.
- *Statistical/experimental unit* = whatever the **original paper** treated as its N for inferential statistics — assessed per-study in §3; not necessarily equal to `C_n`/`Ex_n`.

**⚠️ Caution flagged, not resolved (Derived/calculated):** despite `C_n`/`Ex_n` being defined as "number of animals," **55 of 298 rows (18%) contain non-integer values** (e.g. `Li_2010_BR`: `C_n = Ex_n = 7.5`; `Terzioglu_2020_CMJ`: `Ex_n = 11.333`; `Chikahisa_2007_BBR`: values of `12.5`/`13.5`/`14.5`). No `Exp_note`/`Stat_comment` explains these fractional values, and the codebook does not document a rule for splitting/averaging animal counts across shared or reused comparison groups. This means the reviewer-facing sample-size numbers below are internally consistent with the database as coded, but the fractional values themselves are an unresolved data-provenance question (most plausibly a shared/uneven cohort split across multiple sub-comparisons, based on the pattern of repeated Ex_ID codes, but this is an **inference**, not confirmed in the notes fields).

### Requested summary statistics (Derived/calculated from `data/db251124.csv`)

**Effect-size level (n = 298 rows):**

| | C_n (control) | Ex_n (music) |
|---|---|---|
| Mean | 9.76 | 9.81 |
| SD | 2.53 | 2.59 |
| Median | 10.0 | 10.0 |
| IQR | [8.0, 11.0] | [8.0, 11.0] |
| Min – Max | 6.0 – 14.5 | 6.0 – 14.5 |

**Cohort level (n = 57 distinct `Study_ID × Ex_ID` cohorts, de-duplicating rows that repeat the same cohort's n across multiple outcomes):**

| | C_n | Ex_n |
|---|---|---|
| Mean | 10.14 | 10.16 |
| SD | 2.88 | 2.91 |
| Median | 10.0 | 10.0 |
| IQR | [8.0, 13.0] | [8.0, 13.0] |
| Min – Max | 6.0 – 14.5 | 6.0 – 14.5 |

**Study-level average n (n = 20 studies; each study's own mean C_n/Ex_n across its cohorts):** mean C_n = 9.59 (SD 2.40), mean Ex_n = 9.60 (SD 2.26); median 10.0 for both; **range of study-level average sample size = 6–14 animals per arm** for both control and music conditions.

---

## 3. Unit of music exposure and unit of replication (primary-study audit)

See `CRIMEQ/independent_screening/reviewer_audit_exposure_unit.csv` and its companion `reviewer_audit_exposure_unit_SUMMARY.md`, produced by a dedicated pass over the page-numbered full-text extraction of all 20 included studies (`CRIMEQ/independent_screening/pdf_text/*.json`). **Directly supported by primary paper**, with per-classification quotes, page numbers, and confidence levels in the CSV. All 20 source files were readable; none required an "unavailable" fallback.

### Pseudoreplication-flag distribution across the 20 included studies

| Flag | n studies | Studies |
|---|---|---|
| Potential cage-level pseudoreplication | 5 | Chikahisa2007, Escribano2014, Cheng2024, Flores2018, Freitas2020 |
| Potential room-level pseudoreplication | 6 | Camargo2013, Chen2019, Milbratz2017, Krishnamurthy2025, Fu2025, Rizzolo2021 |
| Potential cage- **and** room/litter-level pseudoreplication | 4 | Li2010 [cage], Niehues2011 [room], Papadakakis2019 [cage+litter], Pangemanan2024 [cage+room] |
| Potential cage-level (severe — single shared cage per whole condition) | 1 | Terzioglu2020 |
| Potential room-level (attenuated by individual housing) | 1 | Fu2023 |
| Unclear — insufficient reporting to judge | 2 | Ren2024, Saghari2021 |
| No apparent issue | 0 | — |

**Headline finding: 18 of 20 studies (90%) show at least a plausible cage- or room-level pseudoreplication concern that is directly supported by the paper's own reported methods, and 0 of 20 studies unambiguously avoided the issue.** In every one of the 18 classifiable studies, music/sound was delivered to a shared acoustic environment (a cage, a group of cages within one room, or a single sound source serving a whole condition group) rather than to independently, individually assignable units — yet in every one of those studies the original statistical analysis (ANOVA, Kruskal–Wallis, or t-test) treated individual animals as fully independent replicates, with no cage/room/litter term in the model. This is a **systematic, cross-study pattern**, not an isolated issue confined to one or two papers.

**Most severe individual case (high confidence, `Terzioglu2020`):** all dams and pooled litters for an entire music condition were housed in a **single shared cage** — only 4 cages existed for the whole study (control, classical, Sufi, rock; one cage each) — fully confounding cage with condition, yet offspring (n≈34 across the 3 music conditions) were analyzed as independent units in a one-way ANOVA on tail-suspension immobility.

**Working hypothesis** ("music delivered in the home cage in most studies; concurrent-with-testing exposure delivered to individually tested animals") **partially held, with a refinement**: it holds directionally for most studies, but the actual exposure unit in the majority of cases was better described as a shared **room** (or several cages within a room) than a strictly independent home cage. The concurrent-exposure clause held cleanly for `Chikahisa2007`, `Escribano2014`, and part of `Flores2018` (sound continued during individual behavioural testing). Two studies complicated the hypothesis: `Chen2019` exposed cohorts in a dedicated soundproof room rather than the home cage, and `Niehues2011` contains an internal textual contradiction (states exposure continued "during the tests" but separately states testing occurred in "a sound-isolated room") and is marked unclear. `Ren2024` and `Saghari2021` lacked enough housing/delivery detail to classify at all.

Full per-study evidence (quotes, page numbers, confidence per classification A–E) is in `CRIMEQ/independent_screening/reviewer_audit_exposure_unit.csv`; narrative synthesis in `CRIMEQ/independent_screening/reviewer_audit_exposure_unit_SUMMARY.md`.

---

## 4. Can the meta-analysis distinguish animals from independent treatment replicates?

**Directly supported by codebase/database — traced through the code, not inferred:**

- **Does the model use reported animal n as the effective sample size?** Yes. `calculate_lnRR()`/`calculate_lnVR()`/`calculate_lnCVR()` (`book/effect_size_calculation.qmd`) pass `C_n`/`Ex_n` directly into `metafor::escalc(n1i =, n2i =, ...)` (or `ni = (Ex_n + C_n)/2` for dependent comparisons). No design effect, deflation factor, or cage-count adjustment is applied anywhere in this pipeline.
- **Is cage/room clustering represented anywhere in the sampling variances or random-effects structure?** No. `data/db251124.csv` (90 columns) and `data/db_effect_sizes.csv` (97 columns) contain **no cage or room identifier field of any kind** (confirmed by name search across all columns). The only clustering identifiers available anywhere in the pipeline are `Study_ID`, `Ex_ID` (→ `Cohort_ID = Study_ID_Ex_ID`, used only to correlate *different outcomes measured on the same cohort* via `vcalc(rho = 0.5)`), `ES_ID`, and `Strain` — none of which represent a physical cage or housing room. A cohort in this database is an *experimental group/condition*, not a physical cage.
- **If primary studies treated animals from a shared exposure cage as independent, would this make the corresponding sampling variances too small?** Yes — this is a direct consequence of `escalc()`'s variance formulas, which assume `n1i`/`n2i` independent draws. If the true independently-replicated unit is the cage rather than the animal (i.e., all animals in a cage received the identical, non-separable music exposure), then using the animal count as `n` understates the true sampling variance (a classic pseudoreplication/design-effect problem), making that effect size look more precise than it is and giving it more influence than warranted in the pooled model.
- **Does the current meta-analytic model correct this in any way, or is it inherited from the primary studies?** It is **inherited, uncorrected, at the level of an individual effect size's sampling variance**. The `vcalc(rho = 0.5, cluster = Cohort_ID)` step only adjusts the **covariance between different effect sizes drawn from the same cohort** (a multivariate-dependency correction), and the `~1 | Study_ID` / `~1 | Strain` random effects only absorb **between-study/between-strain heterogeneity** in the pooled mean. Neither mechanism reduces the precision (inflates the variance) of a single effect size whose own primary-study `n` was inflated by treating cage-mates as independent. Whether this is a real problem in this dataset therefore depends on whether primary studies actually did this — which is exactly what §3 assesses on a study-by-study basis.

---

## 5. Repeated-measures designs and lnVR interpretation

**Directly supported by database + primary paper — Derived/calculated:** `Comparison_structure == "Dependent"` identifies **40 of 298 effect sizes, and these all come from a single study**, `Sampaio_2017_PSYNEURO` (confirmed: `n_distinct(Study_ID)` among Dependent rows = 1). All 40 rows are also coded `Experimental_design == "Repeated Measures"`. (Three further rows — `es151` `Pangemanan_2024_PHJ`, `es233`/`es234` `Rizzolo_2021_CC` — are coded design = "Repeated Measures" but `Comparison_structure == "Independent"`, i.e. their pairing was *not* propagated into the dependent-sample variance estimator; this internal inconsistency is flagged for the authors to check, not resolved here.)

**What was repeatedly measured (Directly supported by primary paper, `CRIMEQ/independent_screening/pdf_text/Sampaio2017.json`, page 3):** the same two cohorts (`Ex_ID` = `ex001`, `ex002`; `C_n = Ex_n = 10` each) were tested **before** and **after** a Mozart's-Sonata music-therapy session, and this before/after comparison was **repeated at four life stages** (juvenile, adolescent, young adult, adult ≈ months 1, 2, 3, 4) across five behavioural measures (Open Field motion; EPM open-arm entries, time in open arms, closed-arm entries; FST immobility) — giving 2 cohorts × 4 ages × 5 measures = 40 rows. Direct quote: *"The animals underwent two stages of testing at each age: an evaluation without music therapy (control), and a reevaluation after music therapy... repeated at 2, 3, and 4 months of age."*

**What the extracted SD represents (Derived/calculated + Inference):** because the "control" and "music" conditions at each age are the **same set of 10 animals** tested twice, the SD entered for each condition is a **cross-sectional SD among those animals at that occasion** (i.e., dispersion in the group's score on that one test day), not a change-score SD and not an SD pooled across ages. Within-individual change over time is what the paired comparison targets, but it enters the sampling-variance calculation only through the assumed correlation parameter (`ri = 0.5` in `escalc(measure = "ROMC"/"VRC")`), not through the SD value itself. **A further point not corrected anywhere in the model:** the four age-specific effect sizes per cohort are also mutually non-independent (same physical animals across all four ages), and this repeated-testing-across-time dependency is captured only insofar as all four ages share the same `Cohort_ID` and therefore the same assumed `rho = 0.5` in the cross-effect-size VCV — a single correlation value doing duty for both "same cohort, different outcome" and "same cohort, different age" dependency simultaneously (see §12).

**Is "inter-individual variability" technically justified for every design? (Inference, offered as a recommendation, not a finding):** For the 258 independent-groups effect sizes, lnVR straightforwardly reflects between-animal (inter-individual) dispersion. For the 40 Sampaio-2017 repeated-measures rows, the SD entering lnVR is *still* a cross-sectional, between-animal SD at a given occasion — so "inter-individual variability" is not technically wrong for these rows either — but because the comparison partners are the same individuals measured twice, describing the *contrast* itself as purely "inter-individual" risks obscuring that a within-subject/repeated-testing element is also built into how precisely that difference is estimated. **Recommendation:** use a broader, single term consistently throughout the manuscript — e.g. **"behavioural variability"** or **"dispersion in behavioural responses"** — reserving "inter-individual variability" for explicit discussion of the independent-groups subset, since it is the more precise term only there.

---

## 6. Sex imbalance, especially for depression outcomes

**Derived/calculated from `data/db251124.csv` (298 rows, `Sex` has no missing/blank values):**

| | Female | Male | Mixed | Total |
|---|---|---|---|---|
| **All outcomes** | 115 (38.6%) | 180 (60.4%) | 3 (1.0%) | 298 |
| **Anxiety-like** (`Outcome_type == "Anxiety"`) | 108 (46.8%) | 123 (53.2%) | 0 (0%) | 231 |
| **Depression-like** (`Outcome_type == "Depression"`) | 6 (9.4%) | 55 (85.9%) | 3 (4.7%) | 64 |

(A further 3 rows are coded `Outcome_type == "both"` — Novelty Suppressed Feeding effect sizes from `Fu_2023_TRANSPSY` (2 rows, Male) and `Fu_2025_TRANSPSY` (1 row, Female) — kept separate from the two tables above because they are not classified as exclusively anxiety- or depression-like.)

There is no "unknown"/unreported sex category in the current data (all 298 rows carry a definite Female/Male/Mixed code).

**Exact replacement for "almost no data for females" (Derived/calculated):** depression-like outcomes include **6 female effect sizes out of 64 depression-like effect sizes = 9.4%** (not "almost no data," but a small and heavily male-skewed minority). **These 6 female depression-like effect sizes come from only 2 independent studies**: `Fu_2025_TRANSPSY` and `Sampaio_2017_PSYNEURO` — i.e., the female-depression evidence base rests on 2 of the 20 included studies, which is the more decision-relevant number for judging generalizability than the raw effect-size percentage.

---

## 7. Species and strain audit

**Directly supported by database, cross-checked against primary text for genetic background — Derived/calculated:**

| Species | Strain | Studies | Effect sizes | Genetic background |
|---|---|---|---|---|
| Mouse | BALB/c | 3 | 37 | Standard inbred strain |
| Mouse | C57BL/6 | 3 | 36 | Standard inbred strain |
| Mouse | ICR | 1 | 16 | Standard outbred stock |
| Mouse | Slc:ddY | 1 | 54 | Standard outbred stock |
| Rat | Sprague Dawley | 2 | 30 | Standard outbred stock |
| Rat | Wistar | 10 | 125 | Standard outbred stock |

**2 species, 6 strains** (4 mouse strains, 2 rat strains). **No genetically modified/transgenic/knockout line was identified**: the `Strain` field never carries a GM qualifier (no "knockout," "Tg," "Cre," or "-/-" notation), and the manipulations recorded elsewhere in the database (`Combined_manipulation`/`Inducing_procedure`: CUMS, ovariectomy, maternal separation, fear conditioning, single prolonged stress, environmental enrichment) are physiological/pharmacological/environmental, not genetic. This is a database-level determination cross-checked against strain-name domain knowledge; it was **not** independently re-verified line-by-line against every primary paper's methods section, so a residual "unclear" should be assumed for any single study not spot-checked.

**One caveat found while compiling the exposure-unit supplementary table (Directly supported by primary paper):** `Li_2010_BR`'s own title is *"Anxiolytic effect of music exposure on BDNF^Met/Met transgenic mice"* — the primary paper does test genetically modified BDNF^Met/Met and BDNF+/- mice. However, checking `data/db251124.csv` directly shows that **only the wild-type comparisons were extracted** (all 8 `Li_2010_BR` rows are coded `Strain = C57BL/6`, `Comparison ∈ {wild.ambient_wild.music, wild.wnwild.music}`) — the transgenic-mouse comparisons from this paper were not carried into the analytical database as separate effect sizes. The §7 conclusion (no GM strain in the analytical database) therefore still holds, but this is worth the authors double-checking, since it means the database silently omits part of one primary paper's design rather than recording an explicit inclusion/exclusion decision for it.

**How Strain enters the model (Directly supported by codebase — confirmed identically in `overall_effect.qmd`, `uni_moderators.qmd`, `multi_moderator.qmd`, `main_figures.qmd`, `leave_one_out.qmd`, `publication_bias.qmd`):** `Strain` is entered **only** as a simple, non-nested, non-crossed random intercept, `random = list(~1|Study_ID, ~1|ES_ID, ~1|Strain)`. It is never used as a fixed-effect moderator, and it is never nested within or crossed with `Species` in any `rma.mv()` call (the only place `Species_latin` and `Strain` co-occur is a descriptive alluvial/Sankey plot in `Alluvial.qmd`, not a statistical model).

**The "<0.01%" variance claim (Unclear/not reported as literal text in this repository; Directly supported by rendered output for the underlying number):** the exact phrase "<0.01%" was not found anywhere in `book/*.qmd` or in the rendered `docs/overall_effect.html`/`docs/uni_moderators.html` — it likely appears in the manuscript text itself, which is not part of this repository. The underlying computed quantity it would be based on, however, is directly traceable: `orchaRd::i2_ml()` on the fitted models gives an `I2_Strain` on the order of **10⁻⁷ %** (e.g. 8.6×10⁻⁷ % for lnRR, 1.6×10⁻⁷ % for lnVR, 1.4×10⁻⁷ % for lnCVR) — far below even a rounded "<0.01%," with `sigma^2_Strain` rounding to 0.0000 in every model. **Caution warranted (Inference, directly requested by the reviewer prompt):** this variance component is estimated from only **6 Strain levels**, two of which (`ICR`, `Slc:ddY`) are contributed by a single study each. A near-zero variance-component *estimate* with so few, unevenly-replicated levels is at least as consistent with **limited power to detect strain heterogeneity** as with a genuine absence of strain effects, and the manuscript should not describe this as evidence that strain "does not matter" biologically.

---

## 8. Proportional outcomes excluded from lnVR

**Directly supported by codebase + database — Derived/calculated:**

- `book/effect_size_calculation.qmd` states the rule explicitly: *"Proportional outcomes (`Data_type == "percentage"`) are treated separately for lnRR (variance-stabilizing arcsine-square-root transformation) and excluded from lnVR and lnCVR because bounded scales induce a mechanical mean–variance relationship that complicates biological interpretation of variability metrics."*
- **Exactly 76 of 298 effect sizes (25.5%), from 14 of the 20 included studies**, are coded `Data_type == "percentage"`. Cross-checked directly in `data/db_effect_sizes.csv`: all 76 have a non-missing `lnRR` value but **zero** have a non-missing `lnVR` (or `lnCVR`) value — confirming the exclusion is applied consistently and completely, and that percentage-type rows are the *only* source of missing `lnVR` in the current dataset (298 − 222 = 76 missing `lnVR` values, all and only the percentage rows).
- **Technical explanation suitable for Methods/Results:** log variability ratios compare standard deviations directly; for outcomes bounded on a 0–100% (or 0–1) scale, the variance is mechanically constrained near the boundaries (e.g., a mean near 0% or 100% cannot have a large SD), so a change in the mean under music exposure would mechanically change the SD regardless of any true change in behavioural dispersion. lnRR for these outcomes is instead computed on the arcsine-square-root-transformed scale, which stabilizes but does not equalize variance across the full range, and is not considered adequate grounds for a variability-ratio interpretation — hence lnVR/lnCVR are not computed for percentage-type outcomes.
- **Was this specified in a preregistration/protocol, or implemented later? Unclear/not reported.** No preregistration or protocol document exists locally in this repository. `book/_quarto.yml` links an OSF registration (`https://osf.io/mv78t`) but no corresponding file is present on disk to check against, so whether this exclusion rule was specified a priori or decided during analysis cannot be determined from repository contents alone.

---

## 9. Anxiety- vs depression-specific lnVR estimates

**Derived/calculated — refit using the identical specification already present in `book/uni_moderators.qmd`** (`rma.mv()`, VCV via `vcalc(rho = 0.5, cluster = Cohort_ID)`, `random = list(~1|Study_ID, ~1|ES_ID, ~1|Strain)`, REML, `test = "t"`, k≥5 level filter — the `"both"` level, k=3, is dropped by that same rule). The manuscript's own model is parameterized with an intercept (reference = Anxiety) and a Depression offset; re-parameterizing without an intercept (mathematically equivalent, coefficients only) recovers each subgroup's own pooled estimate directly:

| Outcome type | Pooled lnVR | 95% CI | t (df=217) | p | ≈ % change in SD under music |
|---|---|---|---|---|---|
| Anxiety-like (k=167) | 0.304 | [0.012, 0.596] | 2.05 | 0.041 | +35.5% |
| Depression-like (k=52) | −0.320 | [−0.737, 0.097] | −1.51 | 0.132 | −27.4% |
| **Depression − Anxiety contrast** | **−0.624** | **[−1.059, −0.190]** | **−2.83** | **0.0051** | — |

Interpretation consistent with the manuscript's existing inferential framework: music exposure is associated with a statistically significant **increase** in behavioural-response variability for anxiety-like outcomes (~36% higher SD), a non-significant **decrease** for depression-like outcomes (~27% lower SD, CI crosses zero), and the **difference between the two domains is itself statistically significant** (p = 0.0051). Random-effects variance components for this model: `Study_ID` σ² = 0.147, `ES_ID` σ² = 1.197, `Strain` σ² ≈ 0 (6 levels) — consistent with §7.

---

## 10. Coding definitions for a compact main-text moderator table

Full operational definitions (quoted from `data/extraction_mm_251105.xlsx` sheet `metadata` and its lookup sheets) with study/effect-size counts per level are compiled in `CRIMEQ/independent_screening/reviewer_audit_codebook_prisma.md`, Task 1 (§1.3). Summary of what is covered there for: `Outcome_type`, `Assay_type`, `Induced behaviour` (innate vs induced), `Experimental_design` (Factorial/Posttest-Only/Repeated Measures — only 3 of 14 catalogued design types occur in this dataset), `Control_conditions`, `Meta_genre`, `Relative_timing`, `Music_exposure_duration` (the categorical Acute/Short/Medium/Long variable — note this is a **different column** from the continuous `Exposure_duration`/`Exposure_span` fields, which record raw hours/day and days respectively), `Experimental_procedures` (Sham vs blank/"None"), `Lifestage_exposure`, and `Sex`. **Directly supported by codebook**, with per-level (n Study_ID / n ES_ID) counts **derived/calculated** from `data/db251124.csv`.

One coding artefact worth flagging for a Methods correction: `Experimental_procedures` codes "Sham" explicitly (60 rows / 3 studies) but its "no such intervention" level is represented as a **blank/NaN cell** (238/298 rows) rather than the codebook's literal "None" string — a cosmetic but reproducibility-relevant inconsistency between the codebook description and the exported CSV.

---

## 11. PRISMA reconciliation

**Directly supported by database for the terminal count; Unclear/not reported for everything upstream.** Full trace in `CRIMEQ/independent_screening/reviewer_audit_codebook_prisma.md`, Task 2. A repo-wide search for "PRISMA" returns zero hits in any source `.qmd`/`.md`/`.py`/`.R`/rendered `.html` file. Two PRISMA-related files exist at the repo root (`PRISMAEcoEvo.pdf` — the guideline paper itself, a reference document; `PRISMA-EcoEvo_WordChecklist.docx` — a completed compliance checklist) but neither contains the actual screening counts; the checklist instead **points to** a flowchart and a "Table S4" in the manuscript's own supplementary material, which is **not present in this repository**.

**What is directly reconstructable:** final included studies = **20** (confirmed three independent ways: `Study_ID` count in the database, 20 paired `.json`/`.txt` files in `pdf_text/`, and the CRIME-Q gold-standard workbook's per-item response totals), and final total effect sizes = **298**. **Not available anywhere in this repository:** records identified through searching, records after de-duplication, records screened at title/abstract, number excluded at that stage, number sought/not retrieved for full text, number assessed at full text, or full-text exclusion reasons/counts. Because none of the upstream counts are present, **arithmetic reconciliation of the PRISMA funnel cannot be verified from this repository** — only its terminal node (20 studies / 298 effect sizes).

**"retrival" typo:** searched case-insensitively across every `.qmd`/`.md`/`.py`/`.R`/`.csv`/`.json`/`.txt`/`.html` file, all three `.xlsx` workbooks (cell-by-cell), the one `.docx`, and the one `.pdf` in the repository. **Zero matches anywhere.** If this misspelling exists, it is in the manuscript text itself (not part of this repository) rather than in any repository-tracked source, data, or supporting document.

---

## 12. Sensitivity analysis to the assumed correlation *r*

**Where r = 0.5 is specified, and that it represents two distinct parameters (Directly supported by codebase):**

1. **`ri = 0.5`** inside `calculate_lnRR()`/`calculate_lnVR()`/`calculate_lnCVR()` (`book/effect_size_calculation.qmd`), passed to `metafor::escalc(measure = "ROMC"/"VRC"/"CVRC", ri = 0.5)`. This is the assumed **within-subject correlation for a single paired/dependent comparison's sampling-variance formula**. It applies only to the 40 `Comparison_structure == "Dependent"` rows (all from `Sampaio_2017_PSYNEURO`; §5) and affects only their `lnRR_var`/`lnVR_var`/`lnCVR_var`, not their point estimates.
2. **`rho = 0.5`** inside `metafor::vcalc(rho = 0.5, cluster = Cohort_ID, obs = ES_ID)`, used identically in `overall_effect.qmd`, `uni_moderators.qmd`, `multi_moderator.qmd`, `main_figures.qmd`, `leave_one_out.qmd`, and `publication_bias.qmd`. This is the assumed **correlation between the sampling errors of different effect sizes drawn from the same cohort** (e.g., two behavioural outcomes on the same animals), and structures the off-diagonal entries of the VCV matrix `V` fed into every `rma.mv()` call. It potentially affects any of the 57 cohorts contributing more than one effect size — i.e., most of the dataset.

These are genuinely **two different correlation parameters that happen to share the same conventional value**, not one parameter reused verbatim.

**New appendix created:** `book/correlation_sensitivity.qmd` (registered as a new `appendices:` entry in `book/_quarto.yml`; no existing chapter was modified). It refits parameter (2) — the cross-effect-size VCV correlation — at `rho = 0.00, 0.25, 0.50, 0.75, 0.90`, using `data/db_effect_sizes.csv` and the exact random-effects specification from `overall_effect.qmd`. The appendix was subsequently **extended to also vary parameter (1)**: it reproduces the exact continuity-correction preprocessing from `effect_size_calculation.qmd` on the raw `data/db251124.csv`, recomputes `lnRR_var`/`lnVR_var`/`lnCVR_var` for the 40 dependent rows at each `ri`, and includes an explicit validation chunk confirming the recomputed variances at `ri = 0.5` reproduce `data/db_effect_sizes.csv` exactly (`all.equal`, tolerance 1e-8) — independently re-checked against the rendered output below. It also empirically confirms (via a toy `escalc()` comparison) that `ri` changes only the sampling variance, never the point estimate, of `ROMC`/`VRC`/`CVRC`. The file **rendered successfully with no errors** (`quarto render correlation_sensitivity.qmd` → `docs/correlation_sensitivity.html`, 57/57 chunks); outputs are saved as `data/sensitivity_r_overall_results.csv`, `data/sensitivity_r_anxiety_depression_contrast.csv` (rho-only), `data/sensitivity_ri_overall_results.csv`, `data/sensitivity_ri_anxiety_depression_contrast.csv` (ri-only, rho fixed at 0.5), `data/sensitivity_ri_rho_grid_results.csv` (joint 5×5 grid, 25 combinations × 3 models), and `Plots/sensitivity_r_overall.pdf`/`.jpg`, `Plots/sensitivity_ri_overall.pdf`/`.jpg`, `Plots/sensitivity_ri_rho_grid.pdf`/`.jpg`.

**`ri`-only results (rho fixed at 0.5; Derived/calculated):**

| ri | lnRR estimate [95% CI] | p | lnVR estimate [95% CI] | p |
|---|---|---|---|---|
| 0.00 | −0.2368 [−0.3711, −0.1025] | <0.001 | 0.1316 [−0.1099, 0.3731] | 0.284 |
| 0.25 | −0.2363 [−0.3707, −0.1020] | <0.001 | 0.1313 [−0.1101, 0.3727] | 0.285 |
| 0.50 | −0.2357 [−0.3701, −0.1013] | <0.001 | 0.1304 [−0.1108, 0.3716] | 0.288 |
| 0.75 | −0.2348 [−0.3693, −0.1002] | <0.001 | 0.1288 [−0.1122, 0.3697] | 0.293 |
| 0.90 | −0.2340 [−0.3687, −0.0993] | <0.001 | 0.1274 [−0.1134, 0.3681] | 0.298 |

Depression-minus-anxiety lnVR contrast across the same `ri` range: −0.626 (ri=0) to −0.619 (ri=0.9), p ≈ 0.0050–0.0052 throughout; anxiety-specific pooled lnVR ≈ 0.301–0.305 (nominally significant throughout), depression-specific pooled lnVR ≈ −0.318 to −0.321 (non-significant throughout). The `ri = 0.5` row reproduces the §9 baseline numbers exactly.

**Joint `ri × rho` grid (25 combinations; Derived/calculated):** overall lnRR ranges −0.250 to −0.226 (95% CI excludes zero in all 25 combinations, p 0.0005–0.0011); overall lnVR ranges 0.116 to 0.141 (95% CI includes zero in all 25 combinations); the depression-minus-anxiety lnVR contrast ranges −0.639 to −0.616, never changes sign, and never loses significance (p stays below 0.006 throughout). The full grid is in `data/sensitivity_ri_rho_grid_results.csv`; a compact heatmap is in `Plots/sensitivity_ri_rho_grid.pdf`/`.jpg`.

**Results (Derived/calculated):**

| rho | lnRR estimate [95% CI] | p | lnVR estimate [95% CI] | p |
|---|---|---|---|---|
| 0.00 | −0.250 [−0.389, −0.111] | <0.001 | 0.141 [−0.111, 0.392] | 0.271 |
| 0.25 | −0.242 [−0.378, −0.106] | <0.001 | 0.136 [−0.111, 0.382] | 0.279 |
| 0.50 | −0.236 [−0.370, −0.101] | <0.001 | 0.130 [−0.111, 0.372] | 0.288 |
| 0.75 | −0.231 [−0.365, −0.097] | <0.001 | 0.125 [−0.111, 0.361] | 0.298 |
| 0.90 | −0.229 [−0.364, −0.095] | <0.001 | 0.122 [−0.111, 0.354] | 0.304 |

Depression-minus-anxiety lnVR contrast across the same range: −0.634 (rho=0) to −0.616 (rho=0.9), p ≤ 0.006 throughout; the anxiety-specific pooled lnVR stays positive and nominally significant for rho ≤ 0.75, the depression-specific pooled lnVR stays negative and non-significant throughout.

**Conclusion:** whether varying `rho` alone, `ri` alone, or both jointly, the overall lnRR effect stays negative and significant (95% CI excludes zero every time); the overall lnVR effect stays non-significant (95% CI spans zero every time); and the depression-vs-anxiety lnVR contrast stays negative and significant throughout (never changes sign, p never exceeds ~0.006). Because `ri` only reweights 40 of 298 rows (13% of the database, all one study) through their sampling variance — never their point estimate — its leverage on any pooled estimate is inherently small, which is exactly what both the single-parameter and joint analyses show. **None of the manuscript's substantive conclusions about the overall or contrast effects depend on the specific choice of `ri = 0.5`, `rho = 0.5`, or their combination.**

---

## Summary table

| Reviewer issue | Evidence found | Manuscript change needed | Additional analysis needed | Relevant output/file |
|---|---|---|---|---|
| Meaning of sample-size variables | C_n/Ex_n = number of animals per codebook; 18% of rows are non-integer for an undocumented reason | Clarify in Methods that n = animals (not cages), and add a footnote/appendix note on the non-integer n values | None required; provenance of fractional n could be traced back to raw extraction if authors want it resolved | §2 above; `data/db251124.csv` |
| Sample-size summary stats requested by reviewer | Computed at ES, cohort, and study level | Insert the requested mean/SD/median/IQR/range numbers into the response letter and, if desired, a supplementary table | None | §2 above |
| Unit of exposure / replication in primary studies | 18/20 studies (90%) show a plausible cage- or room-level pseudoreplication concern directly supported by the paper's own methods; 0/20 unambiguously free of the issue; 2/20 unclear (insufficient reporting) | Add an explicit Discussion/Limitations paragraph stating that music exposure was delivered at the cage/room level in the large majority of included studies while original analyses treated animals as independent, and that this is inherited, uncorrected, in the meta-analysis (§4) | Optional: robustness check restricting to studies without an identified flag (currently none exist, so this would need to loosen the flag definition or be framed as a limitation instead) | `CRIMEQ/independent_screening/reviewer_audit_exposure_unit.csv`, `..._SUMMARY.md` |
| Whether the meta-analysis can separate animals from independent replicates | No cage/room field exists anywhere in the database or model; only Cohort-level (outcome-sharing) and Study/Strain clustering are modeled | Add a limitations paragraph explicitly stating that primary-study cage/room pseudoreplication, where present, is inherited unmodeled | Optional: a bounded re-analysis restricting to studies flagged "no apparent issue" in §3, as a robustness check (not done here) | §4 above |
| Repeated-measures lnVR interpretation | Only 1 study (40/298 ES) is a repeated-measures/dependent design; SD is cross-sectional at each occasion, not a change score | Replace "inter-individual variability" with a broader term (e.g. "behavioural variability") throughout | None required | §5 above |
| Sex imbalance in depression outcomes | 6/64 (9.4%) depression-like ES are female, from 2/20 studies | Replace "almost no data for females" with the exact figures | None required | §6 above |
| Strain representation and the "<0.01%" variance claim | 6 strains (all standard, non-GM), Strain as unmodified random intercept; exact "<0.01%" phrase not found in repo but consistent with rendered ~10⁻⁷% I2; few/unbalanced levels | Add a caution that near-zero strain variance may reflect few levels, not true absence of strain effects | None required | §7 above |
| Proportional-outcome exclusion from lnVR | 76/298 ES (14/20 studies) excluded, consistently and completely; rationale documented in code | Add the technical rationale (mean-variance boundary confound) to Methods if not already there; state whether this was pre-specified (currently unclear) | None required | §8 above |
| Anxiety vs depression lnVR contrast | Reproduced from the existing model: Anxiety +0.304 [0.012,0.596], Depression −0.320 [−0.737,0.097], contrast −0.624 [−1.059,−0.190], p=0.0051 | Report ± the % interpretation if desired | None required | §9 above |
| Compact moderator-definitions table | Full definitions + n Study_ID/ES_ID per level compiled | Move a condensed version of this into the main text per reviewer request | None required | §10 above; `CRIMEQ/independent_screening/reviewer_audit_codebook_prisma.md` |
| PRISMA counts / "retrival" typo | Only the terminal 20 studies/298 ES is reconstructable from this repo; upstream screening counts and the manuscript supplement are not in this repository; "retrival" not found anywhere in-repo | If the flowchart/Table S4 exist only in the manuscript supplement, no repo-side fix is needed beyond checking arithmetic reconciliation there directly; "retrival" may still exist in manuscript prose outside this repo — check there | None required in-repo | §11 above |
| Sensitivity of overall lnRR/lnVR (and the anxiety/depression contrast) to r | Substantive conclusions unchanged across r = 0–0.9 | State in Methods/Results that a correlation-sensitivity check was performed and conclusions are robust | Completed — see new appendix | §12 above; `book/correlation_sensitivity.qmd`, `docs/correlation_sensitivity.html` |
