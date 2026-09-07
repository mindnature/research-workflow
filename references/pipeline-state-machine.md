# Research Pipeline State Machine

This state machine turns the existing research reasoning sequence into an explicit, resumable workflow. It is intentionally lightweight: the Skill remains domain-agnostic and does not require a large multi-agent architecture.

## States

`S0 INTAKE -> S1 SCOPE -> S2 EXTRACT -> S3 STRUCTURE -> S4 COMPARE -> S5 CHALLENGE -> S6 AUDIT -> S7 SYNTHESIZE -> S8 DESIGN/NEXT STEP`

A request may enter at any state when the user already has suitable upstream artifacts. Narrow requests should enter only the state they need.

## State contracts

| State | Purpose | Required input | Required artifact | Exit condition |
|---|---|---|---|---|
| S0 INTAKE | Determine intent and smallest sufficient mode | User request | Mode selection | Mode and working assumptions are explicit |
| S1 SCOPE | Define question and evidence boundary | Topic/question | RQ Brief | Population/unit/context/time/key terms are sufficiently bounded |
| S2 EXTRACT | Gather study/source-level evidence | RQ Brief + sources/search | Source Records / Literature Records | Important evidence is represented without invented fields |
| S3 STRUCTURE | Build reusable comparison structure | Extracted records | Literature Matrix / Concept Map | Repeated fields are normalized enough to compare |
| S4 COMPARE | Identify patterns, differences, contradictions | Structured records | Comparative Synthesis | Agreements and meaningful differences are explicit |
| S5 CHALLENGE | Attack the emerging interpretation | Comparative Synthesis | Adversarial Review | Strongest counterargument and rival explanations are represented |
| S6 AUDIT | Verify consequential claims | Draft claims + sources | Claim Registry + Integrity Report | Blocking claims are PASS or explicitly unresolved/failed |
| S7 SYNTHESIZE | Produce the most defensible conclusion | Audited evidence | Defensible Synthesis | Claim strength matches the inspected evidence |
| S8 DESIGN/NEXT STEP | Convert findings into research action | Synthesis + gap candidates | Research Design Brief / Next Actions | Feasibility, validity threats, ethics, and evidence path are explicit |

## Checkpoint policy

Human checkpoints are required when a decision materially changes the research direction:

1. After S1 when alternative scopes would produce materially different literatures or methods.
2. After S5 when the leading interpretation is substantially weakened or competing interpretations remain viable.
3. At S6 whenever a blocking integrity finding is `FAIL` or `UNRESOLVED`.
4. Before committing to one design at S8 when multiple feasible designs support meaningfully different inferences.

Routine formatting or low-consequence extraction does not require a checkpoint.

## Revision loop

When a synthesis, proposal, or draft is revised after challenge/audit:

`S5 CHALLENGE -> revision plan -> revise -> S6 RE-AUDIT CHANGED CLAIMS -> S7 FINAL SYNTHESIS`

Only changed or newly introduced consequential claims require re-audit unless the revision changes scope, evidence base, or core interpretation, in which case rerun the affected upstream states.

## Failure paths

- `HANDOFF_INCOMPLETE`: required fields are missing. Return to the producing state; do not silently infer missing values.
- `SOURCE_UNAVAILABLE`: preserve the claim as unresolved; do not upgrade from memory or secondary paraphrase.
- `INTEGRITY_FAIL`: revise, remove, narrow, or explicitly quarantine the affected claim before final synthesis.
- `SCOPE_DRIFT`: return to S1 when a later stage silently broadens population, context, time, construct meaning, or inference level.

## Resume semantics

A run can resume from a valid `research_passport` by reading `current_stage`, `artifacts`, `unresolved`, and `next_action`. Resumption is a convenience, not proof that prior claims remain current. Re-check freshness when the topic is time-sensitive or the evidence boundary has changed.
