# Integrity Gates

The integrity gate converts evidence discipline from a prose preference into an explicit research checkpoint. It does not certify truth, reproducibility, or scientific validity; it only checks whether consequential claims are supported to the level asserted by the evidence available to the run.

## Claims that must enter the gate

Treat the following as high-impact by default:

1. numerical claims: counts, percentages, effect sizes, statistical values, rankings, dates that carry argumentative weight;
2. causal claims: causes, leads to, results in, improves, reduces, drives;
3. comparative or superlative claims: better, worse, largest, fastest, strongest, more effective;
4. novelty or absence claims: first, no prior research, unexplored, no studies have examined;
5. method-critical claims: statements about identification, validity, measurement quality, sample representativeness, reproducibility, or benchmark superiority;
6. claims that directly support the main conclusion, policy recommendation, or proposed research gap.

## Gate procedure

### G1 Register

Create one `claim-record` for each detected high-impact claim. Semantic extraction may be incomplete, so never describe the registry as proof that every substantive claim was found.

### G2 Trace

For each registered high-impact claim, identify:

- source ID(s);
- source access status;
- exact evidence locator where available: page, section, paragraph, table, figure, timestamp, dataset field, or official clause;
- whether the original/primary source was actually inspected.

### G3 Fit

Check whether the evidence matches the claim on:

- population or unit;
- context/geography;
- timeframe;
- construct/measure;
- design or analytical method;
- direction and magnitude;
- uncertainty;
- level of inference.

### G4 Verdict

Use only these verdicts:

- `PASS`: inspected evidence directly supports the claim within its stated scope.
- `WARN`: evidence supports a narrower or less certain version; revision is required before treating it as fully verified.
- `FAIL`: inspected evidence contradicts the claim or materially fails to support it.
- `UNRESOLVED`: source/evidence could not be inspected or the available evidence is insufficient to adjudicate.

`UNRESOLVED` is not a soft `PASS`.

## Special rules

### Novelty claims

A statement such as "no prior studies" cannot be globally verified by finding nothing. It may only pass in search-bounded form, for example: "Within searches of [databases/sources] covering [dates], we did not identify...". Absolute novelty language remains `UNRESOLVED` unless independently justified.

### Correlation vs causation

Observational association does not authorize causal language unless the design and assumptions support causal identification. When not justified, downgrade the wording or return `WARN/FAIL`.

### Abstract-only access

An abstract can support what the abstract itself reports, but it does not justify claiming that the full methodology, robustness checks, limitations, or exact table values were verified. Record the access boundary.

### Secondary repetition

Multiple articles repeating one original source are not independent corroboration. Track source lineage where it materially affects confidence.

## Blocking behavior

For ordinary exploratory work, `WARN` and `UNRESOLVED` may remain visible in the output.

Before a `full` workflow emits a final defensible synthesis or before the system endorses a consequential research gap/design decision:

- no central claim may remain `FAIL`;
- central `WARN` claims must be narrowed, revised, or explicitly carried as limitations;
- central `UNRESOLVED` claims must be labelled unresolved and cannot be used as if verified.

## Revision re-audit

After revision, re-audit changed or newly introduced high-impact claims. If the revision changes scope, evidence base, or main conclusion, rerun all affected claims rather than only the textual diff.

## Integrity Report

Minimum output:

| Claim ID | Claim | Evidence locator | Access | Fit | Verdict | Required action |
|---|---|---|---|---|---|---|

End with:

- blocking failures;
- unresolved high-impact claims;
- narrowed claims;
- remaining evidence limitations;
- gate status: `PASS_WITH_LIMITATIONS | BLOCKED`.
