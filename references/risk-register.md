# Risk Register

This register links known research-AI risks to the controls implemented by `research-workflow`. It is intentionally lightweight: a documented control is not treated as evidence that the control is behaviorally effective until it has been tested.

Status vocabulary:

- `DESIGNED`: protocol exists, not yet behaviorally evaluated.
- `TESTED`: covered by deterministic tests or behaviorally executed example cases.
- `MEASURED`: performance has been measured against an independently authored evaluation set.
- `OPEN`: risk known, no adequate control yet.

| Risk | Failure mode | Current control | Status | Residual gap |
|---|---|---|---|---|
| R1 Citation fabrication | Invented citation, DOI, source, sample, or result | `evidence-audit.md`, `integrity-gates.md`, source records | DESIGNED | No measured hallucination catch rate yet |
| R2 Claim-source mismatch | Real source cited for a claim it does not support | Claim Record + locator requirement + fit check | DESIGNED | Semantic completeness of claim extraction remains unknown |
| R3 Causal overclaim | Correlation or weak design rewritten as causation | Integrity Gate G3 + contradiction review | DESIGNED | Domain-specific causal assumptions still need expert judgment |
| R4 False research gap | "No studies exist" inferred from narrow search | Search-bounded Gap Candidate + novelty rule | DESIGNED | Search coverage may remain incomplete or terminology-dependent |
| R5 Abstract/full-text confusion | Abstract-only access presented as full-paper verification | Source Record access status + abstract-only rule | DESIGNED | Behavioral fixtures exist but have not yet been executed against a model |
| R6 Scope drift | Later synthesis silently broadens population/context/time/construct | RQ Brief + state-machine `SCOPE_DRIFT` path | DESIGNED | No automated semantic scope-drift detector yet |
| R7 Confirmation bias | Workflow searches mainly for supporting evidence | Contradiction mode + mandatory strongest counterargument | DESIGNED | Search itself can still be biased before contradiction stage |
| R8 Source dependence | Multiple reports repeat one original source and appear independent | Source-lineage warning in integrity protocol | DESIGNED | Lineage is not yet machine-normalized |
| R9 Revision claim drift | Revision strengthens claims beyond evidence | Revision re-audit of changed high-impact claims | DESIGNED | No structured diff artifact yet |
| R10 Model behavior drift | A later model version follows protocols differently | Evals + CI skeleton | OPEN | Re-running behavioral evals across models is not automated |
| R11 User over-reliance | Researcher treats a PASS label as proof of truth/reproducibility | Explicit integrity-boundary language and checkpoints | DESIGNED | Human reading and independent verification cannot be enforced |
| R12 Stale evidence | Resumed passport or old search treated as current | Search boundary + `last_searched_at` + resume freshness rule | DESIGNED | No automatic freshness threshold by domain yet |

## Release rule

A control may be described as implemented when its protocol/schema exists. It must not be described as validated, calibrated, reliable, or effective unless there is matching test or measurement evidence.

## Priority for evaluation

The first evaluation set should measure R1-R5 because these risks directly affect the credibility of literature reviews, research gaps, and downstream research design.
