# Handoff Contracts

These contracts define the minimum structure of artifacts passed between research stages. They are intentionally smaller than publication-suite schemas: the purpose is reliable research reasoning, not document-production bureaucracy.

Missing required fields must be marked explicitly or trigger `HANDOFF_INCOMPLETE`. Do not invent values to satisfy a contract.

## Contract 1: RQ Brief

Producer: scope stage  
Consumers: extraction, concept mapping, research design

Required fields:

- `research_question`
- `scope.population_or_unit`
- `scope.context`
- `scope.timeframe`
- `scope.in_scope`
- `scope.out_of_scope`
- `key_terms`
- `working_assumptions`

Optional:

- `sub_questions`
- `candidate_theories`
- `candidate_methods`
- `ethical_flags`

## Contract 2: Source Record

Producer: extraction/search  
Consumers: literature matrix, synthesis, evidence audit

Required fields:

- `source_id`
- `citation_or_identifier`
- `source_type`
- `access_status`: `full_text | abstract_only | secondary_report | metadata_only | unavailable`
- `verification_status`: `inspected | partially_inspected | not_inspected`
- `relevance`
- `notes`

When available, also record:

- `doi_or_stable_url`
- `population_or_unit`
- `context`
- `design_or_method`
- `main_findings`
- `limitations`
- `evidence_locators`

## Contract 3: Literature Record

One study or source per record before prose synthesis.

Required fields:

- `source_id`
- `question_or_purpose`
- `framework`
- `unit_context_sample_or_data`
- `design_or_method`
- `measures_or_analysis`
- `main_finding`
- `boundary_or_limitation`
- `relevance_to_rq`
- `evidence_status`

Unknown fields must remain `Unknown`, `Not reported`, or `Requires verification`.

## Contract 4: Claim Record

Producer: evidence-audit stage  
Consumers: integrity gate, synthesis, revision re-audit

Required fields:

- `claim_id`
- `claim_text`
- `claim_kinds`
- `importance`: `high | normal`
- `source_ids`
- `evidence_locators`
- `status`
- `reason`

Closed status vocabulary:

- `VERIFIED`
- `PARTIALLY_SUPPORTED`
- `INFERENCE`
- `UNSUPPORTED`
- `CONTRADICTED`
- `REQUIRES_VERIFICATION`

## Contract 5: Contradiction Record

Required fields:

- `issue_id`
- `claim_or_relationship`
- `supporting_source_ids`
- `contrary_or_null_source_ids`
- `study_differences`
- `plausible_explanations`
- `decisive_test_or_next_question`
- `current_judgment`

## Contract 6: Gap Candidate

A gap is a search-bounded research opportunity, not a rhetorical statement that "no one has studied this."

Required fields:

- `gap_id`
- `gap_type`
- `status`: `candidate_only | supported_within_search`
- `search_boundary`
- `observed_absence_or_limitation`
- `nearest_prior_work`
- `why_it_matters`
- `candidate_question`
- `evidence_or_design_path`
- `confidence`

Use `candidate_only` whenever the search boundary is inadequate, stale, or too narrow to support a bounded absence claim. `supported_within_search` never means globally novel.

## Contract 7: Research Design Brief

Required fields:

- `research_question`
- `design_option`
- `data_or_sampling_logic`
- `measurement_or_coding_plan`
- `analysis_or_interpretive_procedure`
- `validity_threats`
- `ethical_constraints`
- `feasibility_constraints`
- `what_the_design_can_establish`
- `what_the_design_cannot_establish`
- `expected_contribution`

## Contract 8: Research Passport

The canonical machine-readable shape is defined in `schemas/research-passport.schema.json`. The passport is the resumable index of the run; it should point to artifacts and unresolved decisions rather than duplicate every artifact verbatim.
