#!/usr/bin/env python3
"""Lightweight structural validation for research-workflow.

This script intentionally performs deterministic repository checks only. It does
not claim to measure LLM behavior. Behavioral evals in evals/ are fixtures for
separate model runs.
"""

from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "MODE_REGISTRY.md",
    "references/research-modes.md",
    "references/evidence-audit.md",
    "references/output-templates.md",
    "references/pipeline-state-machine.md",
    "references/handoff-contracts.md",
    "references/integrity-gates.md",
    "references/risk-register.md",
    "schemas/research-passport.schema.json",
    "schemas/source-record.schema.json",
    "schemas/claim-record.schema.json",
    "evals/research-integrity-cases.json",
    "evals/routing-cases.json",
]

MODES = {
    "landscape",
    "lit-review",
    "concept-map",
    "contradiction",
    "evidence-audit",
    "research-design",
    "explain",
    "full",
}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_json(relative: str):
    path = ROOT / relative
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"invalid JSON in {relative}: {exc}")


def validate_required_files() -> None:
    missing = [p for p in REQUIRED_FILES if not (ROOT / p).is_file()]
    if missing:
        fail("missing required files: " + ", ".join(missing))


def validate_registry() -> None:
    text = (ROOT / "MODE_REGISTRY.md").read_text(encoding="utf-8")
    missing = sorted(mode for mode in MODES if f"`{mode}`" not in text)
    if missing:
        fail("MODE_REGISTRY missing modes: " + ", ".join(missing))


def validate_schemas() -> None:
    passport = load_json("schemas/research-passport.schema.json")
    source = load_json("schemas/source-record.schema.json")
    claim = load_json("schemas/claim-record.schema.json")
    if passport.get("title") != "Research Passport":
        fail("unexpected passport schema title")
    if source.get("title") != "Source Record":
        fail("unexpected source schema title")
    if claim.get("title") != "Claim Record":
        fail("unexpected claim schema title")


def validate_eval_cases() -> None:
    integrity = load_json("evals/research-integrity-cases.json")
    cases = integrity.get("cases", [])
    if len(cases) < 15:
        fail("research integrity eval set must contain at least 15 cases")
    ids = [case.get("id") for case in cases]
    if len(ids) != len(set(ids)):
        fail("duplicate integrity eval ids")
    for case in cases:
        if not case.get("risk") or not case.get("input") or not case.get("expected"):
            fail(f"incomplete integrity eval case: {case.get('id')}")

    routing = load_json("evals/routing-cases.json")
    routing_cases = routing.get("cases", [])
    if len(routing_cases) < 8:
        fail("routing eval set must contain at least 8 cases")
    for case in routing_cases:
        mode = case.get("expected_primary_mode")
        if mode and mode not in MODES:
            fail(f"unknown mode in routing eval {case.get('id')}: {mode}")


def validate_skill_links() -> None:
    text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    expected = [
        "MODE_REGISTRY.md",
        "pipeline-state-machine.md",
        "handoff-contracts.md",
        "integrity-gates.md",
    ]
    missing = [name for name in expected if name not in text]
    if missing:
        fail("SKILL.md does not reference: " + ", ".join(missing))


def main() -> None:
    validate_required_files()
    validate_registry()
    validate_schemas()
    validate_eval_cases()
    validate_skill_links()
    print("research-workflow structural validation: PASS")
    print("Note: behavioral eval fixtures are not executed by this structural validator.")


if __name__ == "__main__":
    main()
