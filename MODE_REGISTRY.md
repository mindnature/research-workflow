# Mode Registry

Single source of truth for `research-workflow` modes. The goal is to route each request to the smallest sufficient workflow rather than running the full research pipeline by default.

| Mode | Trigger / intent | Required input | Primary output | Evidence requirement | Human oversight |
|---|---|---|---|---|---|
| `landscape` | Map a field, identify schools, methods, debates, or candidate gaps | Topic or provisional question | Research landscape + prioritized gap candidates | Search boundary must be stated; gap claims are search-bounded | Medium |
| `lit-review` | Review and compare a body of literature | Question/topic + papers or search access | Literature matrix + cross-study synthesis | Study-level extraction before narrative synthesis | Medium |
| `concept-map` | Clarify constructs, theories, mechanisms, variables, propositions | Research question or conceptual problem | Concept/relationship map | Definitions and relationships must be tied to sources where available | Medium |
| `contradiction` | Stress-test a claim or reconcile conflicting studies | Claim, draft, or study set | Contradiction map + adversarial review | Supporting and contrary evidence must both be represented | High |
| `evidence-audit` | Verify whether claims are supported by cited evidence | Draft/claims + sources | Claim registry + evidence audit | High-impact claims require source inspection or explicit unresolved status | High |
| `research-design` | Turn a gap/question into an executable study | Research question + evidence summary | Research design brief | Design claims must distinguish what the method can and cannot establish | High |
| `explain` | Teach or translate a complex research concept | Concept/source | Plain-language explanation | Preserve technical meaning; examples are not evidence | Low |
| `full` | End-to-end research reasoning from question to defensible next step | Topic/question + available sources | Passport + landscape/literature structure + audit + synthesis + design options | Mandatory integrity gate before final synthesis | Very High |

## Routing rules

1. Prefer one mode when one mode can satisfy the request.
2. Combine modes explicitly when the requested deliverable genuinely spans multiple tasks.
3. Use `full` only when the user asks for an end-to-end workflow or when several dependent modes are required.
4. `systematic review` is not a synonym for `lit-review`. Do not claim PRISMA-grade comprehensiveness unless a documented search strategy, screening log, eligibility process, and quality appraisal have actually been performed.
5. When a request contains high-impact factual, numerical, causal, comparative, or novelty claims, add `evidence-audit` even if another mode is primary.

## Oversight levels

- `Low`: mechanical or explanatory transformation with limited consequential judgment.
- `Medium`: structured analysis; user should review scope and interpretation.
- `High`: consequential research judgment, criticism, or design selection; surface assumptions and unresolved issues.
- `Very High`: multi-stage workflow with explicit checkpoints at major decisions and integrity gates.
