---
name: research-workflow
description: "Use a domain-agnostic, evidence-aware and stateful workflow to explore research topics, review literature, compare studies, map concepts and variables, detect contradictions and gaps, challenge claims, audit sources, and turn findings into defensible research questions or designs. Applies across disciplines and research stages when analysis is needed beyond a simple factual lookup or prose rewrite."
---

# Research Workflow

Use this skill for research work in any discipline: natural sciences, engineering,
medicine, social sciences, humanities, education, business, arts, and
interdisciplinary research. Do not assume a particular epistemology, method,
country, population, or publication tradition. Adapt the workflow to
quantitative, qualitative, mixed-methods, theoretical, computational, or
practice-based work.

The goal is not merely to summarize sources. Produce a traceable path from a
research question to evidence, comparison, criticism, verification, and a
defensible next step.

## Route to the smallest sufficient mode

Use [MODE_REGISTRY.md](MODE_REGISTRY.md) as the canonical mode registry. The
available primary modes are:

- `landscape`;
- `lit-review`;
- `concept-map`;
- `contradiction`;
- `evidence-audit`;
- `research-design`;
- `explain`;
- `full`.

Detailed research behavior remains in
[research-modes.md](references/research-modes.md). Prefer one mode when one mode
is sufficient. Combine modes explicitly when the requested deliverable spans
multiple tasks. Do not run `full` for a narrow request.

If a request contains consequential factual, numerical, causal, comparative,
novelty, or method-critical claims, add the `evidence-audit` behavior even when
another mode is primary.

## Stateful research pipeline

For complex work, follow the explicit state model in
[pipeline-state-machine.md](references/pipeline-state-machine.md):

`intake → scope → extract → structure → compare → challenge → audit → synthesize → design/next step`

A request may enter in the middle when the user already has suitable upstream
artifacts. Do not repeat stages merely for ceremony.

For substantial multi-stage work, maintain a `research_passport` conforming to
[research-passport.schema.json](schemas/research-passport.schema.json). The
passport is a resumable index of the research state. It records the research
question, scope, search boundary, source and claim records, contradictions,
gap candidates, assumptions, unresolved issues, produced artifacts,
`current_stage`, and `next_action`.

On resume, treat the passport as recorded state, not as proof that evidence is
still current. Refresh time-sensitive searches or claims when freshness matters.

## Artifact contracts

Use [handoff-contracts.md](references/handoff-contracts.md) for artifacts passed
between stages. Required contracts include:

- RQ Brief;
- Source Record;
- Literature Record;
- Claim Record;
- Contradiction Record;
- Gap Candidate;
- Research Design Brief;
- Research Passport.

Missing required fields must remain explicitly unknown or trigger
`HANDOFF_INCOMPLETE`. Never infer a value solely to satisfy a schema or fill a
table.

## Non-negotiable research behavior

1. Define the question before searching or drafting. Make the population,
   unit of analysis, context, time window, comparison, outcome, and meaning of
   key terms explicit when they matter.
2. Separate what a source reports from what you infer and what you propose.
   Use clear labels such as `Verified`, `Inference`, `Proposal`, and `Unknown`
   when the distinction could be missed.
3. Build a comparison structure before writing a long literature narrative.
   For each study, capture its question, theory or framework, context and
   sample/data, design and method, measures or analytical approach, principal
   finding, boundary condition, and limitation. Use the schemas in
   [output-templates.md](references/output-templates.md).
4. Treat disagreement as information. Record supporting and contrary evidence,
   then test whether the difference is explained by theory, construct
   definition, measurement, sample, context, time, design, or analysis.
5. Search for the strongest counterargument to the emerging conclusion. Check
   alternative explanations, selection and survivorship bias, reverse
   causality, confounding, common-method bias, weak measurement, overclaiming,
   external-validity limits, and ethical or practical constraints as relevant
   to the field.
6. Identify gaps in at least the dimensions that fit the question: theoretical,
   empirical/data, methodological, contextual/external-validity,
   temporal/technological, and practice or policy relevance. A gap is useful
   only when it can be converted into a specific question or test.
7. Audit important claims against the actual source. Prefer original studies,
   primary data, official documents, standards, and authoritative repositories;
   distinguish independent corroboration from multiple reports repeating one
   source. Follow [evidence-audit.md](references/evidence-audit.md).
8. Never invent a citation, DOI, sample size, result, quotation, page number,
   dataset, or statistical value. If the source was not inspected, say so.
   Do not present a plausible interpretation as an established finding.

## Integrity gate

For high-impact claims, follow
[integrity-gates.md](references/integrity-gates.md). At minimum:

1. register the claim;
2. trace it to source IDs and exact evidence locators when available;
3. test fit across population/unit, context, timeframe, construct, method,
   direction/magnitude, uncertainty, and inference level;
4. return `PASS`, `WARN`, `FAIL`, or `UNRESOLVED` at gate level while preserving
   the more detailed Claim Record evidence status.

Before a `full` workflow emits a final defensible synthesis, no central claim
may remain `FAIL`. Central `WARN` claims must be narrowed or retained as explicit
limitations. Central `UNRESOLVED` claims cannot be used as if verified.

A clean integrity gate does not certify raw-data authenticity, actual research
execution, reproducibility, global novelty, or scientific truth. It only bounds
what can be said from the evidence inspected in the run.

## Revision and re-audit

When a synthesis, proposal, or draft changes after adversarial review, use the
small revision loop:

`challenge → revision plan → revise → re-audit changed high-impact claims → final synthesis`

If revision changes the scope, evidence base, or central interpretation, rerun
the affected upstream stages instead of auditing only the textual diff.

## Source and tool discipline

Use the user's supplied files and links as the primary evidence base. When
current, niche, or source-specific information is required and web access is
available, retrieve the original source and cite claims close to the evidence.
For a local paper or report, inspect the file itself rather than relying on its
filename or an abstract copied elsewhere. Record incomplete access as a
limitation, not as permission to fill the gap from memory.

Do not promise that a short research sprint is a publication-grade systematic
review. A rapid pass can produce a research map, priority gaps, and a plan for
verification; comprehensive review still requires a documented search strategy,
screening decisions, full-text assessment, and field-appropriate quality
appraisal.

## Default output standard

Unless the user requests another format, organize substantive outputs as:

1. research question and scope;
2. assumptions and search/evidence boundary;
3. structured findings or literature matrix;
4. agreements, contradictions, and anomalies;
5. prioritized research gaps;
6. strongest objections and unresolved uncertainties;
7. integrity findings for consequential claims;
8. defensible synthesis;
9. concrete research questions, design options, or next actions.

Use tables for repeated fields and comparisons. Keep a claim's confidence
proportional to the evidence. If the user asks for a paper section, proposal,
lecture, or public-facing explanation, retain the same evidence discipline while
adapting the presentation to that deliverable.

## Engineering and evaluation boundary

Known risks and current controls are indexed in
[risk-register.md](references/risk-register.md). Structural repository checks
live in `scripts/validate_repo.py`; behavioral fixtures live in `evals/`.
Passing structural validation does not mean model behavior has been measured.
Do not describe a control as calibrated, reliable, or effective until there is
separate evaluation evidence supporting that claim.
