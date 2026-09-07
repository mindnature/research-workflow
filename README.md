# Research Workflow

`research-workflow` is a general-purpose Codex Skill for evidence-aware research. It is designed for researchers in any discipline and supports early-stage exploration, literature synthesis, critical review, evidence verification, and study planning.

The core reasoning path is:

`scope → extract → structure → compare → challenge → audit → synthesize`

Version 2 keeps that compact research core but adds the missing engineering layer: explicit modes, state transitions, artifact contracts, a resumable Research Passport, integrity gates, revision re-audit, risk tracking, and a minimal evaluation/CI scaffold.

## What it can do

- map an unfamiliar research field;
- review and compare papers or reports;
- identify theoretical, data, method, context, time, or practice gaps;
- build a conceptual framework or hypotheses;
- detect contradictions and rival explanations;
- stress-test technical or academic claims;
- check whether citations actually support a draft;
- distinguish full-text, abstract-only, secondary, and unverified access;
- turn a gap into research questions and feasible design options;
- preserve research state across a longer workflow through a Research Passport.

## Architecture

```text
User request
   ↓
MODE_REGISTRY
   ↓
INTAKE → SCOPE → EXTRACT → STRUCTURE → COMPARE → CHALLENGE → AUDIT → SYNTHESIZE → DESIGN
                 ↘ narrow requests may enter/exit at the required state ↗

Research Passport = resumable state index
Artifact Contracts = stage-to-stage data contracts
Integrity Gate = claim → source → locator → fit → verdict
Revision loop = challenge → revise → re-audit changed claims
```

The Skill deliberately does not use a large multi-agent team by default. Its design goal is a small, composable research reasoning engine that other research, writing, review, or proposal systems can build on top of.

## Modes

`MODE_REGISTRY.md` is the single source of truth for routing:

- `landscape`
- `lit-review`
- `concept-map`
- `contradiction`
- `evidence-audit`
- `research-design`
- `explain`
- `full`

The Skill should choose the smallest sufficient mode. `full` is reserved for genuinely end-to-end work.

## Research Passport

For multi-stage work, the Skill can maintain a machine-readable Research Passport containing:

- research question and scope;
- search boundary and freshness information;
- source records and access status;
- claim records and evidence status;
- contradictions and gap candidates;
- assumptions and unresolved issues;
- produced artifacts;
- current stage and next action.

Schema: `schemas/research-passport.schema.json`.

The passport makes a workflow resumable, but it is not proof that old evidence is still current. Time-sensitive claims must be refreshed when appropriate.

## Integrity model

High-impact claims—especially numerical, causal, comparative, novelty, method-critical, and conclusion-critical claims—enter an explicit integrity gate:

`register → trace source → locate evidence → check fit → PASS / WARN / FAIL / UNRESOLVED`

A clean gate means the inspected evidence supports the permitted wording within the recorded boundary. It does not certify raw-data authenticity, reproducibility, actual research execution, or global novelty.

## Repository structure

```text
research-workflow/
├── SKILL.md
├── README.md
├── MODE_REGISTRY.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── research-modes.md
│   ├── evidence-audit.md
│   ├── output-templates.md
│   ├── pipeline-state-machine.md
│   ├── handoff-contracts.md
│   ├── integrity-gates.md
│   └── risk-register.md
├── schemas/
│   ├── research-passport.schema.json
│   ├── source-record.schema.json
│   └── claim-record.schema.json
├── evals/
│   ├── research-integrity-cases.json
│   └── routing-cases.json
├── scripts/
│   └── validate_repo.py
└── .github/workflows/
    └── validate.yml
```

## Design principles

- Domain-agnostic: adapt to the discipline and research tradition instead of imposing one method.
- Evidence-first: distinguish verified findings, inferences, proposals, and unknowns.
- Adversarial: actively look for counter-evidence, rival explanations, and boundary conditions.
- Search-bounded: do not turn "not found" into "does not exist."
- Stateful when useful: substantial workflows can resume from a structured passport.
- Smallest sufficient mode: avoid full-pipeline overhead for narrow requests.
- Honest about validation: a designed control is not automatically a measured control.
- Honest about speed: a rapid research map is not automatically a systematic review or publication-ready evidence base.

## Validation

Run:

```bash
python scripts/validate_repo.py
```

The validator checks repository structure, schema syntax, mode registration, and evaluation fixture structure. GitHub Actions runs the same structural validation on pushes and pull requests.

Behavioral fixtures in `evals/` are not executed by this structural validator. They are intended for later model-level evaluation; no behavioral accuracy claim should be made until those cases are actually run and measured.
