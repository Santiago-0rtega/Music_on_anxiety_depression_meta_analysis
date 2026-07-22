# CRIME-Q NotebookLM Calibration Rules

These rules clarify how to apply the CRIME-Q codebook in NotebookLM extractions.
They do not provide study answers. Apply them to every target paper.

## Behavioral/Acoustic Scope Rule

This CRIME-Q adaptation is scoped to the behavioral assays and the in vivo
music/acoustic exposure. Score items using evidence about:

- animals/groups that contribute to behavioral outcomes,
- acoustic/music delivery and acoustic/control exposure,
- behavioral testing, scoring, analysis, attrition, and reporting, and
- study limitations that affect behavioral interpretation or acoustic exposure.

Do not give credit for details reported only for unrelated molecular,
biochemical, histological, physiological, or other non-behavioral procedures
unless those details directly determine the behavioral assay, the animals
included in it, or the interpretation of the acoustic/music exposure.

## Verbatim Evidence Rule

The `VERBATIM` cell must contain:

1. an exact quote copied from the target paper, and
2. a location tag such as `[p.2, Methods]`, `[Table 1]`, `[Fig 1]`, `[Ethics]`,
   `[Funding]`, or `[COI]`.

Invalid `VERBATIM` examples:

- `[p.403, Header]`
- `[p.2, Methods]`
- `See Table 1`
- `NOT REPORTED IN PROVIDED SOURCE CONTEXT`

Valid structure:

- `[p.2, Methods] "A total of 60 male Wistar rats..."`

If NotebookLM cannot provide exact quoted words from the target paper, write
exactly:

`NOT REPORTED IN PAPER`

Do not use `NOT REPORTED IN PROVIDED SOURCE CONTEXT`.

## Item-Meaning Rule

Score each item according to the CRIME-Q item meaning, not according to nearby
generic concepts. For example:

- `1X` is peer review/publication status, not the study aim.
- `3X` is animal reporting, not sample-size calculation.
- `4Y` is sample-size/power calculation, not group size reporting.
- `6X` is ethics/welfare reporting, not conflict of interest.
- `10X` is conflict-of-interest statement presence, not funding.
- `10Z` is funder/commercial influence, not whether any funding exists.
- For blinding, attrition, outcome reporting, limitations, and methods-results
  alignment, evidence from non-behavioral assays does not substitute for
  evidence about the behavioral assays unless it directly affects behavioral
  interpretation.

## High-Risk Decision Rules

### 1X Peer Review

Journal article = `Yes`. Do not require explicit words such as "peer reviewed"
inside the article.

### 3Y vs 3Z

- Homogeneous animals plus randomization but no baseline balance/matching data:
  `3Y = Partly`.
- Randomization alone does not prove baseline balance:
  `3Z = Unclear`.
- Explicit matching, blocking, weight-balancing, or litter-balancing can support
  `3Z = Yes`.
- Baseline balance means balance for animals/groups entering the behavioral
  music/control comparison. Baseline measures from unrelated assays do not
  establish balance unless they apply to those same behavioral groups.

### 4Y Sample-Size Calculation

Group size reporting is not a sample-size calculation. If no a priori
power/sample-size calculation or justification is reported, score `No`.

### 5Z(2) Random Housing

- Separate music/control rooms with no environmental matching or room swap:
  `No`.
- Separate rooms explicitly matched on environment but not counterbalanced:
  `Unclear`.
- Same room without cage-position randomization/counterbalancing:
  `Unclear`.
- Consider acoustic exposure room, sound source position, cage/rack/shelf
  position, and behavioral testing position. The question is whether non-music
  environmental or positional differences could be confounded with the
  behavioral outcome.

### 5Z(3) Outcome Assessment Selection

`5Z(3)` is about whether animals/groups were selected for outcome assessment in
a way that could bias results. It is not an assessor-blinding item. Do not use
`5Z(3)` to score whether outcome assessors were blinded; assessor blinding is
covered by `7Z(2)`.

- Score `5Z(3) = Yes` when the paper describes planned outcome assessment for
  the allocated animals/groups at fixed or pre-specified timepoints, with no
  indication that animals were selected, excluded, or routed to assessment based
  on interim outcomes, response, health status, or investigator judgment.
- Score `5Z(3) = Unclear` when it is not possible to tell whether all allocated
  animals/groups were eligible for the planned outcome assessment, or when
  assessment timing/subset selection is not described well enough to judge.
- Score `5Z(3) = No` when animals are explicitly selected into outcome
  assessment after allocation based on post-allocation behavior, response,
  phenotype, survival, successful model induction, or other outcome-related
  information, unless this was a pre-specified design feature that is handled
  without bias.
- Fixed statements such as `after 4 weeks the animals were tested`,
  `behavioral testing started 8 days after implantation`, or `tests were
  performed after the last intervention` generally support `Yes` if no
  outcome-dependent selection or exclusion is reported.
- Selection rules for molecular or histological assays do not determine
  `5Z(3)` unless they also determine which animals entered the behavioral
  outcome assessment.

### 6X Ethics

- Named ethics committee approval or protocol number: `Yes`.
- General guideline/society compliance only, without committee approval or
  protocol number: `Partly`.
- No ethics/welfare statement: `No`.

### 7X, 7Z(1), 7Z(2) Blinding

Before scoring blinding, search the target paper for terms such as `blind`,
`blinded`, `mask`, `masked`, `observer`, `rater`, `coder`, `scorer`, `analyst`,
`recorded`, `video`, and `number coded`.

- `7X` asks whether relevant blinding is reported for acoustic exposure,
  behavioral testing, behavioral scoring/coding, or another phase that can
  affect behavioral outcomes.
- `7Z(1)` asks about handlers/experimenters delivering acoustic/music exposure
  or behavioral testing.
- `7Z(2)` asks about behavioral outcome assessor/coder/analyst blinding.
- If any observer, assessor, coder, analyst, or sample reader is explicitly
  blinded for at least one behavioral task, behavioral outcome, or acoustic
  exposure phase, `7X` is at least `Partly`.
- If blinding is reported only for non-behavioral assays, `7X` remains `No`
  unless those assays determine behavioral interpretation and the behavioral
  phase is also masked.
- If blinding is reported for only one behavioral outcome, task, or phase, score
  `7X = Partly` unless the paper clearly states that blinding applied to all
  relevant behavioral outcomes.
- Blinding reported for one outcome does not automatically apply to all
  behavioral outcomes.
- "Blind to genotype" does not prove blind to music/control condition.
- If handler or assessor blinding is not reported, score `Unclear` for the
  corresponding risk-of-bias item, not `No`.
- For judgment-sensitive behavioral outcomes such as anxiety-like,
  depression-like, fear, or memory scoring, score `7Z(2) = No` only when the
  paper explicitly describes live/manual scoring, counting, rating, or
  observation by an observer/experimenter who appears able to know the treatment
  condition and does not report masking/blinding.
- If the paper describes behavioral testing, video recording, tracking, or
  manual tests but does not say who scored the outcome or whether the scorer
  could know the treatment condition, score `7Z(2) = Unclear`, not `No`.
- Automated or video-recorded measurement does not prove assessor blinding
  unless masking/blinding is stated.
- Score `7Z(1) = NA` only when the paper explicitly justifies handler/exposure
  blinding as infeasible and the acoustic delivery, handling, and behavioral
  testing are otherwise identical or automated. Do not infer `NA` from silence.

### 8Z(1) Attrition

Before scoring attrition, compare the number allocated with the number analyzed
for each relevant behavioral group and behavioral outcome. Look in Methods,
Results, figure legends, tables, flow diagrams, and statistical degrees of
freedom.

- Score `8Z(1) = Yes` only when allocation numbers and analysis denominators are
  clear enough to conclude that all allocated animals contributed behavioral
  data, or when behavioral exclusions/losses are reported with reasons and are
  unlikely to bias results.
- Use `Yes` only when the allocation-to-analysis path is reconciled across the
  relevant behavioral experiment. This usually requires exact starting group
  sizes and exact analyzed denominators for all main behavioral outcomes, or an
  explicit statement that all allocated animals were analyzed.
- Do not infer `Yes` from a single matching denominator, one figure legend, one
  representative outcome, or a general methods statement such as `n = X per
  group` if other behavioral outcomes, experiments, figures, sexes, or subgroups
  are not reconciled.
- A range such as `n = 9-18`, approximate group sizes, varying degrees of
  freedom, or denominators that differ across figures/tables is a warning sign.
  If the paper does not explain these differences, score `Unclear` unless the
  missing/excluded animals create clear likely bias, in which case score `No`.
- If allocation n is stated and exact analysis n matches it across every main
  relevant outcome, and no exclusions are reported, zero attrition is implied:
  `Yes`.
- If denominators vary across behavioral figures/tables, experiments, sexes, or
  outcomes and no explanation is given, score `Unclear` or `No` depending on
  severity and likely bias.
- If animals were excluded, lost, selected, or omitted after allocation and the
  reasons are not reported, score `Unclear` or `No`; do not assume zero
  attrition.
- Denominator variation limited to molecular, histological, or biochemical
  subsets should not lower `8Z(1)` unless it also affects behavioral outcome
  data or makes the behavioral allocation-to-analysis path unclear.

### 9X Limitations

Before scoring limitations, search the Discussion and Conclusion for terms and
phrases such as `limitation`, `limited`, `caution`, `however`, `unknown`, `not
known`, `not tested`, `not investigated`, `remains to be`, `could not`,
`discrepancy`, `may be due to`, `cannot determine`, and `future studies`.

- Score the authors' acknowledgement of current-study caveats relevant to
  behavioral assays, acoustic/music delivery, control exposure, animal model,
  behavioral measures, or behavioral interpretation. Do not score the mere
  presence of a formal `Limitations` heading.
- `Yes`: the authors identify two or more concrete current-study weaknesses,
  unresolved design issues, discrepancies, measurement/model constraints, or
  interpretation caveats in the behavioral/acoustic scope.
- `Partly`: the authors identify one concrete current-study caveat in the
  behavioral/acoustic scope, even if brief or embedded in ordinary Discussion
  text.
- `No`: the Discussion/Conclusion gives no concrete caveat about the current
  study's behavioral assays, acoustic/music exposure, control condition, animal
  model, or behavioral interpretation. General future research language alone is
  not enough.
- A caveat about behavioral measurement, animal model limitations,
  hearing/perception issue, acoustic stimulus, exposure timing,
  generalizability of behavioral outcomes, unexplained behavioral discrepancy,
  repeated behavioral testing, or uncertainty in what acoustic feature caused
  the behavioral effect can count as a study-specific limitation.
- A caveat only about an untested molecular mechanism, hormone level,
  histology, biochemical pathway, or other non-behavioral endpoint does not
  count unless the authors link it directly to interpreting the behavioral
  outcome or acoustic exposure.
- A negative/null finding accompanied by a specific explanation of why the
  current study may not have shown an effect can count as a caveat if the
  explanation concerns this study's behavioral design, measurement, model,
  acoustic/music intervention, or behavioral interpretation.
- Do not score `No` merely because there is no formal `Limitations` heading or
  because the caveat is phrased as an uncertainty, discrepancy, possible
  explanation, or unresolved question.
- Do not score `Partly` when the authors discuss several concrete weaknesses,
  discrepancies, or unresolved design/interpretation problems; that is usually
  `Yes`.
- Future-directions language alone, such as "more studies are needed", is not a
  study limitation and should be `No` unless it names a specific weakness of the
  current study.

### 10X and 10Z

- `10X = Yes` only when a formal conflict-of-interest or competing-interest
  statement is present.
- No COI statement = `10X = No`.
- Academic/government funding, when reported, is normally `10Z = Yes` unless
  funder influence is reported.
- No funding statement or unclear funder role = `10Z = Unclear`.

## Final Self-Check

Before finalizing each row, check:

- Every `SCORE` is one of `Yes`, `No`, `Partly`, `Unclear`, or `NA`.
- Score columns are named with the item ID only, such as `1X` or `5Z(1)`, not
  `1X_SCORE`, `ITEM_1X_SCORE`, or `5Z1_SCORE`.
- Every `VERBATIM` contains quoted words plus a location tag, or exactly
  `NOT REPORTED IN PAPER`.
- No `VERBATIM` cell contains only a page/table/figure location.
- No cell says `NOT REPORTED IN PROVIDED SOURCE CONTEXT`.
- Item scores match the item meanings above.
