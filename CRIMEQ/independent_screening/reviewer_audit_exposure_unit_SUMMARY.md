# Reviewer Audit Summary: Music-Exposure Unit and Pseudoreplication Risk

Audit of all 20 primary studies in the music/anxiety-depression meta-analysis, based on
extracted PDF text (CRIMEQ/independent_screening/pdf_text/*.json). Full details, quotes,
and page numbers for every classification are in reviewer_audit_exposure_unit.csv.

## Pseudoreplication flag counts (20 studies)

- Potential cage-level pseudoreplication: 5 (Chikahisa2007, Escribano2014, Cheng2024,
  Flores2018, Freitas2020)
- Potential room-level pseudoreplication: 6 (Camargo2013, Chen2019, Milbratz2017,
  Krishnamurthy2025, Fu2025, Rizzolo2021)
- Potential cage-level AND room-level (or litter-level) pseudoreplication: 4
  (Li2010 [cage], Niehues2011 [room], Papadakakis2019 [cage+litter],
  Pangemanan2024 [cage+room])
- Potential cage-level pseudoreplication (severe, single shared cage per condition):
  1 (Terzioglu2020)
- Potential room-level pseudoreplication (attenuated by individual housing): 1 (Fu2023)
- Unclear (insufficient reporting to judge): 2 (Ren2024, Saghari2021)
- No apparent issue: 0 studies were judged unambiguously free of pseudoreplication risk.

In short, 18 of 20 studies (90%) showed at least a plausible cage- or room-level
pseudoreplication concern based on explicit or reasonably inferable housing/exposure
details, and 2 studies (10%) could not be classified due to insufficient reporting of
housing/delivery methods (Ren2024, Saghari2021). No study explicitly reported both (a)
independently randomized/replicated cages or rooms per condition and (b) a statistical
model accounting for that clustering (e.g., mixed model with cage as random effect,
or cage/litter as the unit of analysis). Every study that could be classified used
individual animals as the statistical unit (one-way/two-way/three-way ANOVA, Kruskal-
Wallis, or t-tests), regardless of whether music was demonstrably delivered at the
cage or room level to multiple animals simultaneously.

The single most severe case identified was Terzioglu2020, in which an entire dose
condition's dams and pooled litters were housed in one shared cage (only 4 cages
total for the whole study, one per music condition), fully confounding cage and
condition, yet offspring were analyzed as independent statistical replicates.

## Studies that could not be fully classified

- Ren2024: unclear whether the 10 mice per condition were housed/exposed together in
  one chamber or individually; text is ambiguous ("Each of them was placed in
  identical chambers").
- Saghari2021: no housing details (cage occupancy, sound delivery mechanism) are
  reported at all, and it is unclear whether the 12h/day music exposure window
  overlapped with the behavioral testing window.

No study's source text was entirely unavailable; all 20 JSON/text files were present
and readable, so no row required the "source text unavailable" fallback.

## Working hypothesis check

Hypothesis: "music was delivered while animals were in their home cages in most
studies, whereas concurrent exposure during behavioral testing was generally
delivered while individual animals were being tested."

This hypothesis PARTIALLY HELD, with an important refinement. Studies split into
two clear patterns:

1. Chronic home-cage/room exposure with NO concurrent testing exposure (this pattern
   held for Camargo2013, Cheng2024 [partial], Fu2023, Fu2025 [partial], Li2010,
   Milbratz2017, Niehues2011 [internally contradictory - flagged unclear],
   Papadakakis2019, Rizzolo2021, Sampaio2017, Terzioglu2020, Krishnamurthy2025
   [partial], Pangemanan2024 [partial]) — this is the majority pattern and matches
   the hypothesis's first clause.
2. Concurrent exposure delivered while individual animals were being tested
   (Chikahisa2007, Escribano2014, Flores2018 for its acute-FST-exposure factor) —
   this matches the hypothesis's second clause exactly.

Two studies contradicted or complicated the hypothesis: Chen2019's exposure was
delivered in a dedicated soundproof room rather than the home cage; and Niehues2011
contains an internal inconsistency (text states exposure continued "during the
tests" while separately stating testing occurred in "a sound-isolated room").
Overall, the hypothesis holds as a reasonable generalization but the "home cage"
label is often a simplification — in most studies, the actual exposure unit was a
shared ROOM (or a small number of cages within a room) rather than a fully
independent per-cage or per-animal assignment.

## Bottom line

Across the 20 rodent studies, essentially none reported an analysis that matched
their exposure delivery level: music/sound was consistently delivered at the cage or
room level (i.e., to multiple animals sharing a proximate acoustic environment), while
statistical analyses almost universally treated individual animals as fully
independent replicates. This is a systematic, cross-study pattern rather than an
isolated problem in one or two papers, and should be flagged prominently in any
meta-analytic sensitivity discussion of effective sample size.
