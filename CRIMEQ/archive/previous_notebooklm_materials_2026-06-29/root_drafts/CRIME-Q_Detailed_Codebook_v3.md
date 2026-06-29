# CRIME-Q Codebook for Animal Music Studies (20 items)

Study-level appraisal. For each item the SCORE must follow the criteria and DECISION RULES below.

## 1X — Peer Review (QoR)

**Question:** Did the paper undergo peer review before publication?

**Response options:** Yes; No  |  **Level:** Study-level

- **Yes:** Published in a peer-reviewed journal (verify journal is peer-reviewed through indexing in PubMed, Web of Science, or similar databases).
- **No:** Preprint, thesis, conference abstract, or other non-peer-reviewed report.

**Music examples:** Yes: Psychoneuroendocrinology, Journal of Music Therapy, Behavioral Brain Research. No: bioRxiv preprint, dissertation, conference proceedings not published as journal article.

**Pitfalls / decision rule:** DECISION RULE: any article published in a journal (including open-access or lower-tier journals such as EC Neurology or ASEAN J Psychiatry) = Yes; only preprints, theses, and stand-alone conference abstracts = No. Do not downgrade for perceived journal prestige or infer status from author affiliation.

---

## 3X — Animals: Reporting (QoR)

**Question:** Are experimental animals sufficiently described?

**Response options:** Yes; Partly; No  |  **Level:** Study-level

- **Yes:** Report all key descriptors: species, strain/stock, sex, age/stage + body mass or weight range, supplier/source, and identifiable group sizes (n per group).
- **Partly:** Missing 1-2 of the key descriptors listed above.
- **No:** Generic description or seriously insufficient information for replication.

**Music examples:** Yes: "Male C57BL/6 mice (n=12/group), aged 10-12 weeks, 24-26g, from Jackson Lab, housed 4/cage." Partly: "Adult C57BL/6 mice (n=24)" - age range missing. No: "Mice were used".

**Pitfalls / decision rule:** Do not penalize early-life studies where sex cannot be determined. Record "NA - sex undeterminable" if applicable. Supplier often inferred from strain name.

---

## 3Y — Animals: Technical Quality (MQ)

**Question:** Were animal characteristics comparable between groups and appropriate for the music intervention?

**Response options:** Yes; Partly; No  |  **Level:** Study-level

- **Yes:** Clear evidence of group balance or matching/blocking/litter-balancing procedure. Groups appropriate for aims (e.g., animals can perceive/respond to music).
- **Partly:** Likely comparable but incompletely documented. Missing baseline table or limited matching detail.
- **No:** Baseline imbalance shown and unaddressed. OR unsuitable model for stated aim.

**Music examples:** Yes: "Table 1: no significant differences in baseline anxiety (p=0.45), age (p=0.62), weight (p=0.58). All animals had normal hearing." Partly: "Sixty male Wistar rats, 3-5 months, randomized to subgroups" - homogeneous and randomized but NO baseline behavioural comparison reported. No: "Control group significantly less anxious at baseline (p<0.05)" - no adjustment.

**Pitfalls / decision rule:** DECISION RULE: homogeneous animals + randomization but NO baseline data table = Partly (not Yes); Yes requires actual reported balance OR an explicit matching/blocking procedure. Missing baseline table usually = Partly, not No. Judge suitability for music specifically. Do not confuse n imbalance with characteristic imbalance.

---

## 3Z — Selection Bias: Baseline Characteristics (RoB)

**Question:** Were relevant baseline characteristics balanced between music and control groups?

**Response options:** Yes; No; Unclear; NA  |  **Level:** Study-level

- **Yes:** Arm-specific baseline data provided AND balanced, OR explicit matching/blocking/litter-balancing procedure used.
- **No:** Baseline imbalance documented and unaddressed in analysis.
- **Unclear:** No arm-specific baseline data reported, OR no information about balancing procedure.

**Music examples:** Yes: "Table 1: no significant differences (all p>0.05)" OR "Animals matched using block randomization." No: "Anxiety scores differed significantly at baseline (p<0.01), not adjusted." Unclear: "No baseline data provided."

**Pitfalls / decision rule:** Randomization alone does NOT ensure baseline balance. Look for reported baseline data. Baseline balance requires p-values or confidence intervals.

---

## 4Y — Sample-Size Calculation (QoR)

**Question:** Did the study report an appropriate a priori sample-size calculation?

**Response options:** Yes; Partly; No  |  **Level:** Study-level

- **Yes:** Explicit power analysis with: target effect size, desired power (usually 80%+), alpha level (usually 0.05), and appropriate test or design.
- **Partly:** Calculation mentioned but incomplete (e.g., "80% power" without effect size). OR post-hoc or based on prior studies without full justification.
- **No:** No sample-size calculation or justification reported.

**Music examples:** Yes: "G*Power 3.1: effect size f=0.25 (medium), alpha=0.05, power=0.80, 2 groups, n=45/group." Partly: "Based on prior music studies" OR "Powered at 80%..." (no effect size). No: No mention of justification.

**Pitfalls / decision rule:** "Followed prior studies" is NOT a calculation. Code based on REPORTING, not actual sample size (small n can still have reported calculation).

---

## 5X — Music Intervention: Reporting (QoR)

**Question:** Is the music intervention described sufficiently for replication?

**Response options:** Yes; Partly; No  |  **Level:** Study-level

- **Yes:** All core elements reported: music type/genre, delivery method, duration per exposure, frequency, timing relative to outcome, volume/intensity (dB), control condition (specified clearly), individual vs. group.
- **Partly:** One or more core elements missing or vaguely stated.
- **No:** Music-vs-control insufficiently described. Cannot identify music or control condition.

**Music examples:** Yes: "Classical piano (Chopin Nocturnes) via ceiling speakers at 70 dB, 30 min/day for 14 days, starting 1 week post-housing. Control: ambient lab noise at equivalent volume." Partly: "Classical music 30 min/day; control silence" - volume/specific pieces not stated. No: "Mice exposed to music."

**Pitfalls / decision rule:** List EACH core element. Genre must be specific enough to replicate (Mozart < Mozart Sonata K545). Control condition MUST be explicit. Different controls (silence, white noise, other music) are distinct.

---

## 5Y — Music Intervention: Technical Quality (MQ)

**Question:** Does the music intervention design appear technically sound for the stated aim?

**Response options:** Yes; Partly; No  |  **Level:** Study-level

- **Yes:** Plausibly delivers distinct music vs. control with no obvious acoustic cross-contamination, pseudoreplication, dose/volume confound, or fatal timing flaw.
- **Partly:** Plausible but key technical info incomplete (e.g., housing separate but no soundproofing detail), OR cage/litter-level pseudoreplication present but partially mitigated.
- **No:** Clear technical problem: music and silence in same cage; volume/loudness confounded with genre (e.g., each genre played at a different dB); only one cage/litter per group; random music timing; or other uncontrolled confounds.

**Music examples:** Yes: "Separate rooms with doors closed, 15 cm soundproofing. Speakers 30 cm from cages (music group only). Control: silent speakers at equivalent distance." Partly: "5 rats/cage, 2 cages per group; analysis treated each rat as independent" - cage-level pseudoreplication not accounted for. No: "classical at 60 dB, sufi at 30 dB, rock at 120 dB" (loudness confounded with genre) OR "one cage of dams per music group, pups analysed as independent" (litter confound).

**Pitfalls / decision rule:** PSEUDOREPLICATION RULE: if animals share cages/litters and the analysis treats individuals as independent without accounting for cage/dam, that is pseudoreplication = at most Partly; if there is only ONE cage/litter per group it is unavoidable = No. PERINATAL designs randomize the DAM but measure the PUPS - pups from one dam are not independent. DOSE-CONFOUND RULE: if different genres are played at different volumes/durations, genre is confounded with loudness/dose = No. Do NOT judge if music "should work" - assess technical feasibility only.

---

## 5Z(1) — Selection Bias: Sequence Generation (RoB)

**Question:** Was allocation to groups generated by an appropriate random method?

**Response options:** Yes; No; Unclear; NA  |  **Level:** Study-level

- **Yes:** Allocation method is described as random and plausible: RNG, random-number table, drawing lots, or similar preventing foreknowledge.
- **No:** Clearly non-random: alternation, order of arrival, convenience sampling, or assignment based on pre-intervention characteristics.
- **Unclear:** States "randomly assigned" but no method described.

**Music examples:** Yes: "www.random.org to generate assignments." OR "Animals drawn randomly from sealed envelope." No: "Assigned alternately" OR "Odd-numbered animals to music, even to control." Unclear: "Randomly assigned to groups" - no method.

**Pitfalls / decision rule:** "Random" without method = Unclear, not Yes. Randomizing cage positions ≠ randomizing animal allocation. Opaque bag > list.

---

## 5Z(2) — Performance Bias: Random Housing (RoB)

**Question:** Were animals randomly housed or protected from cage/position effects?

**Response options:** Yes; No; Unclear; NA  |  **Level:** Study-level

- **Yes:** Random placement of cages to shelf positions, OR counterbalancing/rotation, OR explicit addressing of positional confounds (light, temperature, airflow, acoustic).
- **No:** Systematic placement confounding treatment: music group top shelf vs control bottom shelf, OR music and control kept in SEPARATE ROOMS with no environmental matching or room-swap described.
- **Unclear:** Housing/cage position not reported sufficiently, OR separate rooms used but explicitly environmentally matched (residual room confound remains).

**Music examples:** Yes: "Cages randomly assigned to shelves; positions rotated weekly" OR "Music and control equally represented on each rack." No: "Music played in one room; the silence room was a different room" with no matching/room-swap. Unclear: "Silence room was identical to the music room except for sound" - matched but still separate (residual confound).

**Pitfalls / decision rule:** SEPARATE-ROOMS RULE (key for music studies): music and control are usually in different rooms for acoustic isolation, which confounds ROOM with treatment. If separate rooms with NO environmental matching and NO counterbalancing/room-swap = No. If rooms explicitly matched on light/temp/humidity but still separate = Unclear (residual confound). Only score Yes if both conditions share the same racks with randomization, or rooms were swapped/counterbalanced across replicates. Consider light, temperature, airflow, acoustic proximity to equipment.

---

## 5Z(3) — Detection Bias: Outcome Assessment (RoB)

**Question:** Were animals assessed by pre-specified, unbiased selection rule?

**Response options:** Yes; No; Unclear; NA  |  **Level:** Study-level

- **Yes:** All allocated animals tested at pre-specified time (e.g., "all tested day 21"), OR pre-specified rule applied (e.g., "first 10/cage to complete testing day 14").
- **No:** Selection based on post-allocation response, survival, behavior, or outcome-dependent criteria (e.g., "only non-depressed animals tested").
- **Unclear:** Selection procedure not reported sufficiently.

**Music examples:** Yes: "All surviving (n=24) tested day 21, 48h post-final music" OR "After 4 weeks of treatment, the rats from each subgroup were tested" (all animals, fixed timepoint). No: "Only weight-gain animals tested" OR "Inclusion criteria: rats demonstrating depressive-like behaviour by SPT were selected into the treatment group" (selection on the outcome). Unclear: "Animals were tested" - which and when unspecified.

**Pitfalls / decision rule:** DECISION RULE: "selected for behavioural studies" usually just means "underwent testing" at a fixed timepoint (= Yes), NOT cherry-picking. BUT in induced-model studies, including animals BECAUSE they show the target phenotype (e.g., CUMS responders selected by low SPT) IS outcome-dependent selection = No. Do not penalize natural attrition (death, escape). Pre-specified timing for ALL animals = Yes.

---

## 6X — Ethical Compliance (QoR)

**Question:** Did the study report compliance with animal-welfare regulations?

**Response options:** Yes; Partly; No  |  **Level:** Study-level

- **Yes:** Ethics/animal-care approval explicitly reported: "IACUC approved, protocol #12345" OR "Approved by animal care committee per [guideline]."
- **Partly:** General welfare statement without specific committee approval or protocol number.
- **No:** No mention of ethical approval or animal welfare compliance.

**Music examples:** Yes: "Approved by University IACUC (protocol #00001234)" OR "Approved by the institutional animal ethics committee." Partly: "Performed in compliance with SBNeC / the NIH Guide for the Care and Use of Laboratory Animals" - names a guideline/society but NO committee approval; OR "conducted ethically and humanely." No: No ethics or welfare statement anywhere.

**Pitfalls / decision rule:** DECISION RULE: Yes requires a stated APPROVAL by an ethics/animal-care committee (named body or protocol number). Naming a guideline or society compliance WITHOUT a committee approval = Partly. Vague "humanely" = Partly. Nothing = No. (Absence does not always mean the work was unethical, but code on what is reported.)

---

## 7X — Blinding: Reporting (QoR)

**Question:** Does the report describe blinding in any phase (intervention delivery, outcome assessment, analysis)?

**Response options:** Yes; Partly; No  |  **Level:** Study-level

- **Yes:** Explicitly states WHO blinded (assessor, analyst), WHEN (intervention, outcome, analysis), and to WHICH condition (music vs. control).
- **Partly:** Blinding mentioned unqualified ("blinded analysis") with limited detail about who, when, or how.
- **No:** No mention of blinding in any phase.

**Music examples:** Yes: "Assessors blinded to group during testing. Analysts blind to treatment during statistics." OR "Automated recording prevented experimenter presence, preventing bias." Partly: "The study was blinded" or "Blinded analysis performed" (no specifics). No: "No blinding" OR no mention.

**Pitfalls / decision rule:** Automated playback ≠ blinding by itself (assessor hears music). Live music delivery may make experimenter blinding infeasible. Prioritize assessor/analyst blinding for subjective outcomes.

---

## 7Z(1) — Performance Bias: Experimenter Blinding (RoB)

**Question:** Were experimenters/handlers delivering music blinded to group assignment?

**Response options:** Yes; No; Unclear; NA  |  **Level:** Study-level

- **Yes:** Procedures prevented handlers knowing assignment: pre-recorded/automated delivery (tech cannot hear), cages A/B only (no labels), or independent personnel delivered stimulus.
- **No:** Experimenter unblinded and could influence outcomes through differential handling, stress, or attention.
- **Unclear:** Not reported whether blinding attempted or achieved.

**Music examples:** Yes: "Pre-recorded music/silence via automated systems; tech unaware which played." OR "Cages labeled A/B only, no treatment visible to handlers." No: "Experimenter selected music daily while observing behavior." Unclear: paper says nothing about who delivered music or whether handling was blinded. NA: authors explicitly state delivery-blinding was infeasible AND an automated system delivered the stimulus with identical handling of both groups.

**Pitfalls / decision rule:** DECISION RULE: if the paper is SILENT on intervention/handler blinding, default to Unclear (not No, not NA). Score No only when an unblinded handler plausibly delivered differential handling/attention. Use NA only when authors explicitly justify infeasibility. Audibility alone does not force NA.

---

## 7Z(2) — Detection Bias: Assessor Blinding (RoB)

**Question:** Were outcome assessors blinded to group assignment?

**Response options:** Yes; No; Unclear; NA  |  **Level:** Study-level

- **Yes:** Assessors/coders/analysts blinded to assignment during assessment. Video-coded with A/B cage labels only (not treatment), or data masked before analysis.
- **No:** Assessor unblinded and outcome is judgment-sensitive (anxiety, depression scoring based on behavioral interpretation).
- **Unclear:** Not reported whether assessors were blinded or how maintained.

**Music examples:** Yes: "Behavior videos coded by independent raters blind to assignment (cages A/B only)." OR "Group labels masked before analysis (Group 1/2 only)." No: "Experimenter scored anxiety knowing group assignment." OR "Behavior rated real-time by present experimenter." Unclear: "Videos coded" - no mention of assessor blinding.

**Pitfalls / decision rule:** Objective outcomes (distance, weight) may not need blinding; judgment-sensitive (anxiety, depression) DO. Automated tracking ≠ blinding unless data masked before analysis. A/B video labeling effectively blinds.

---

## 8X — Methods-Results Alignment (QoR)

**Question:** Are reported methods and results coherent, transparent, and aligned?

**Response options:** Yes; Partly; No  |  **Level:** Study-level

- **Yes:** Outcomes, group labels, n, timing, and statistical analyses match between Methods and Results. Results traceable to Methods. Primary outcomes in Methods appear in Results.
- **Partly:** Minor discrepancies, but primary comparison interpretable. E.g., Methods list anxiety/depression; Results report only anxiety.
- **No:** Major mismatches, outcome switching, unreported contrasts, or untraceable results.

**Music examples:** Yes: "Methods: anxiety/depression via EZM/FST. Results: Table 1 shows both EZM/FST for music vs. control with matching n and timing." Partly: "Methods mention anxiety/depression; Results report only anxiety." No: "Results text says 42 rats but the flow diagram shows 39 included" (internal n contradiction) OR "title says Mozart K488 but Methods say K448" combined with other mismatches.

**Pitfalls / decision rule:** CROSS-CHECK RULE: compare the n in the FLOW DIAGRAM / figures / tables against the n stated in the text - internal numerical contradictions (e.g., 42 vs 39) are a real misalignment. Also check title vs Methods (stimulus code typos). Check outcome switching, unreported groups, timing changes. Minor formatting != No; multiple/contradictory n or dropped outcomes = Partly or No.

---

## 8Z(1) — Attrition Bias: Incomplete Data (RoB)

**Question:** Were outcome data complete, with exclusions/attrition adequately handled?

**Response options:** Yes; No; Unclear  |  **Level:** Study-level

- **Yes:** Numbers allocated, analyzed, excluded/lost reported clearly by group with reasons for attrition. OR all allocated animals contributed data (zero attrition).
- **No:** Missing/excluded animals unequal across groups, outcome-related, or inadequately explained.
- **Unclear:** Denominators and exclusion reasons insufficiently reported.

**Music examples:** Yes: "24 allocated (12 music, 12 control). 1 control died (gavage failure). 23 analyzed." OR "Sixty rats allocated, ten per subgroup; figures show n=10 per group" - allocation n stated and matches analysis n, no exclusions. No: "9 music, 15 control analyzed" (allocation never stated). OR "Anxiety >5 SD excluded; more in control, not justified." Unclear: figure ns shown but total allocated never stated, so completeness cannot be confirmed.

**Pitfalls / decision rule:** DECISION RULE: if allocation n IS stated and matches the analysis n shown in figures/tables with no exclusions mentioned, score Yes (zero attrition implied). If allocation n is NEVER stated so you cannot confirm everyone was analyzed, score Unclear. Natural attrition (death, technical failure) reported equally is NOT bias. Flag outcome-dependent exclusion.

---

## 8Z(2) — Reporting Bias: Selective Outcomes (RoB)

**Question:** Were all pre-specified or expected outcomes fully reported?

**Response options:** Yes; No; Unclear  |  **Level:** Study-level

- **Yes:** Pre-registration available and matches publication. OR Methods lists outcomes, Results reports all with group statistics.
- **No:** Key outcome in Methods missing from Results, OR outcome switching evident, OR selective reporting of favorable results.
- **Unclear:** No pre-registration and Methods does not clearly pre-specify outcomes - cannot verify against Results.

**Music examples:** Yes: "Pre-registered OSF. Methods/Results both report anxiety/depression for all groups." OR "Methods: Primary=anxiety (EZM). Secondary=depression (FST), activity (OFT). Results: all three reported with contrasts." No: "Methods list SPT and FST; Results state FST could not be analysed due to technical problems and report only SPT" (outcome measured but dropped) OR "Methods emphasize anxiety/depression; Results report only anxiety." Unclear: "No pre-registration; Methods does not pre-specify outcomes - cannot verify."

**Pitfalls / decision rule:** DECISION RULE: no pre-registration but Methods explicitly enumerates the outcome measures and Results reports ALL of them with group-level stats = Yes. An outcome that was MEASURED but then dropped/unreported (even with a stated reason like "technical problems") counts against full reporting = No (note the disclosure in the justification). Use Unclear only when Methods does not clearly enumerate outcomes. Absence of pre-registration alone NEVER forces Unclear or No. Non-significant outcomes must be reported as NS, not omitted.

---

## 9X — Discussion: Limitations (QoR)

**Question:** Did authors acknowledge relevant study limitations?

**Response options:** Yes; Partly; No  |  **Level:** Study-level

- **Yes:** Substantive limitations discussed and linked to experiment, model, measures, or design. Examples: single music genre, small n, only males, limited time window.
- **Partly:** Generic or brief statement without substantive connection. E.g., "This study has some limitations."
- **No:** No limitations section or discussion.

**Music examples:** Yes: "Limitations: (1) single genre - may not generalize; (2) small n (12/group) - reduced secondary power; (3) only males; (4) 2-week exposure - chronic effects unknown." Partly: "This study had limitations" OR "Small sample size" (no implications explained). No: Discussion contains only future-directions ("there is a need to conduct more studies") and no acknowledgment of THIS study's weaknesses.

**Pitfalls / decision rule:** DECISION RULE: future-directions statements ("more studies are needed", "further research should...") are NOT limitations - if the Discussion has only these and no specific weakness of the present study, score No. Substantive = linked to this study's design/measures/interpretability. Author humility / calls for replication != genuine limitations.

---

## 10X — Conflict-of-Interest Statement (QoR)

**Question:** Did the paper include a conflict-of-interest/competing-interests declaration?

**Response options:** Yes; No  |  **Level:** Study-level

- **Yes:** Formal statement present: authors declare no conflicts OR disclose specific conflicts.
- **No:** No COI statement in paper or supplementary materials.

**Music examples:** Yes: "The authors declare no competing financial interests." OR "Author A: employed by Music Therapy Inc. Others: no conflicts." No: No COI statement found.

**Pitfalls / decision rule:** "No conflicts" declaration = Yes. Absence of statement ≠ implies conflict, only lack of transparency. Some journals require, others do not. Code based on statement presence.

---

## 10Z — Other Bias: Funder Influence (RoB)

**Question:** Was the study free from inappropriate funder/commercial influence?

**Response options:** Yes; No; Unclear  |  **Level:** Study-level

- **Yes:** No relevant conflict declared AND no evidence that funder/company with interest controlled design, conduct, or reporting. Academic/government funding is NOT a bias signal.
- **No:** Funder/company with interest funded study AND controlled/influenced design, conduct, reporting. OR conflict undeclared.
- **Unclear:** Funding source or funder role insufficiently reported.

**Music examples:** Yes: "Funded by NIH (R01-MH12345). No music companies involved." OR "Funded by university internal funds; no external sponsor role in design/analysis." No: "Funded by MusicalMind Inc. (makes therapy devices). Company provided stimulus and reviewed manuscript." OR "Undeclared: corresponding author is CEO of music therapy startup." Unclear: "Supported by grants" - no agency specified.

**Pitfalls / decision rule:** Academic/public funding (NIH, NSF, university) ≠ bias by itself. Flag only when commercial entity with financial stake appears to control key decisions. Undeclared = No. Industry-sponsored ≠ automatically No, but increased scrutiny warranted.

---

