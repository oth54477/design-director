#!/usr/bin/env python3
"""Routing regression for design-director.

The decision order here is the one described in references/skill-router.md.
If a case fails, fix the rule and the markdown together.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "tests" / "routing-cases.json"

BASE_INSTALLED = [
    "impeccable",
    "ui-ux-pro-max",
    "emil",
    "web-design-guidelines",
    "taste",
    "hallmark",
    "huashu",
    "open-design",
    "kami",
]

STYLE = ("taste", "hallmark", "huashu", "ui-ux-pro-max", "kami")
CLI_SKILLS = {"impeccable", "ui-ux-pro-max", "taste", "hallmark", "huashu", "kami"}
MOTION = {
    "single": "animate",
    "group": "choreograph",
    "jank": "animation-performance",
}
EMIL_MEMBERS = {
    "animate",
    "choreograph",
    "animation-performance",
    "improve-animations",
    "review-animations",
    "emil-design-eng",
}


def expand_installed(spec) -> list[str]:
    if spec == "all":
        return list(BASE_INSTALLED)
    if isinstance(spec, str) and spec.startswith("all-"):
        drop = set(spec[4:].split(","))
        return [item for item in BASE_INSTALLED if item not in drop]
    if isinstance(spec, str) and spec.startswith("all+"):
        extra = [item for item in spec[4:].split(",") if item]
        return list(BASE_INSTALLED) + extra
    if isinstance(spec, list):
        return list(spec)
    raise TypeError(f"installed spec not understood: {spec!r}")


def named_styles(case) -> list[str]:
    raw = case.get("named") or []
    if isinstance(raw, str):
        raw = [raw]
    return [item for item in raw if item in STYLE]


def route(case: dict) -> dict:
    installed = set(expand_installed(case["installed"]))
    task = case["task"]
    styles = named_styles(case)
    has_ds = bool(case.get("has_design_system", False))
    motion = bool(case.get("motion", False))
    motion_kind = case.get("motion_kind", "single")
    brand_hint = case.get("brand_hint")
    visual_doc = bool(case.get("visual_doc", False))
    workspace = bool(case.get("workspace", False))
    platform = case.get("platform", "web")
    browser = bool(case.get("browser", True))
    cli_ok = bool(case.get("cli", True))
    network = bool(case.get("network", True))
    external_model = bool(case.get("external_model", False))
    skip_mockup = bool(case.get("skip_mockup", False))

    selected: list[str] = []
    missing: list[str] = []
    focus: list[str] = []
    needs_decision = False
    code_edits = task != "audit"

    def add(skill: str, focus_token: str) -> None:
        if skill in selected:
            return
        gate = skill
        if skill in EMIL_MEMBERS:
            gate = "emil"
        if gate not in installed and skill not in installed:
            if skill not in missing:
                missing.append(skill)
            return
        selected.append(skill)
        focus.append(focus_token)

    def add_motion() -> None:
        if motion_kind not in MOTION:
            raise ValueError(f"unknown motion_kind {motion_kind}")
        skill = MOTION[motion_kind]
        if platform == "expo" and motion_kind == "single":
            if "animate-expo" in installed:
                add("animate-expo", "animate-expo:implement")
                return
            missing.append("animate-expo")
        token = {
            "animate": "animate:implement",
            "choreograph": "choreograph:implement",
            "animation-performance": "animation-performance:diagnose",
        }[skill]
        add(skill, token)

    if task == "audit":
        code_edits = False
        fetch_token = "web-design-guidelines:fetch" if network else "web-design-guidelines:local-only"
        add("web-design-guidelines", fetch_token)
        add("impeccable", "impeccable:audit")
        if motion:
            add("review-animations", "review-animations:review")
    elif task == "document":
        if visual_doc:
            add("huashu", "huashu:three-directions")
        else:
            add("kami", "kami:build")
    elif task == "motion":
        add_motion()
    elif len(styles) > 1:
        needs_decision = True
        code_edits = False
    elif task == "explore":
        lead = styles[0] if styles else "huashu"
        add(lead, f"{lead}:three-directions" if lead == "huashu" else f"{lead}:new-page")
        if workspace:
            add("open-design", "open-design:companion-only")
    elif task == "landing":
        if styles:
            lead = styles[0]
        elif has_ds:
            lead = None
        elif brand_hint == "theme":
            lead = "hallmark"
        else:
            lead = "taste"
        if lead == "taste":
            add("taste", "taste:landing")
        elif lead == "hallmark":
            add("hallmark", "hallmark:new-page")
        elif lead == "huashu":
            add("huashu", "huashu:three-directions")
        elif lead:
            add(lead, f"{lead}:lead")
        add("impeccable", "impeccable:polish")
        fetch_token = "web-design-guidelines:fetch" if network else "web-design-guidelines:local-only"
        add("web-design-guidelines", fetch_token)
    elif task == "new-product":
        if not has_ds:
            add("ui-ux-pro-max", "ui-ux-pro-max:design-system-no-persist")
        add("impeccable", "impeccable:shape")
        fetch_token = "web-design-guidelines:fetch" if network else "web-design-guidelines:local-only"
        add("web-design-guidelines", fetch_token)
    elif task == "improve":
        if len(styles) == 1:
            lead = styles[0]
            token = {
                "taste": "taste:landing",
                "hallmark": "hallmark:new-page",
                "huashu": "huashu:three-directions",
                "kami": "kami:build",
                "ui-ux-pro-max": "ui-ux-pro-max:design-system-no-persist",
            }[lead]
            add(lead, token)
        add("impeccable", "impeccable:polish")
        fetch_token = "web-design-guidelines:fetch" if network else "web-design-guidelines:local-only"
        add("web-design-guidelines", fetch_token)
        if motion:
            add_motion()
    else:
        raise ValueError(f"unknown task {task}")

    if not selected and not needs_decision:
        code_edits = False

    if needs_decision:
        verify_mode = "none"
    elif task == "document":
        verify_mode = "artifact"
    elif browser:
        verify_mode = "browser"
    else:
        verify_mode = "static"

    cli_execute = bool(
        cli_ok and code_edits and not needs_decision and any(skill in CLI_SKILLS for skill in selected)
    )
    fetch_guidelines = "web-design-guidelines" in selected and network

    # Brief 는 모든 라우트에서 보여 준다. 승인 대기는 파일을 고치는 라우트만.
    plan_approval = bool(code_edits and not needs_decision)
    if not plan_approval or skip_mockup or task in ("document", "motion"):
        mockup = "none"
    elif "huashu" in selected:
        mockup = "directions"
    elif browser:
        mockup = "image"
    else:
        mockup = "html-only"

    return {
        "selected": selected,
        "missing": missing,
        "focus": focus,
        "needs_decision": needs_decision,
        "code_edits": code_edits,
        "verify_mode": verify_mode,
        "cli_execute": cli_execute,
        "fetch_guidelines": fetch_guidelines,
        "allow_external_model": external_model,
        "plan_approval": plan_approval,
        "mockup": mockup,
    }


def assert_invariants(case_id: str, result: dict) -> list[str]:
    errors = []
    styles = [skill for skill in result["selected"] if skill in STYLE]
    if len(styles) > 1:
        errors.append(f"{case_id}: more than one style lead {styles}")
    if len(result["selected"]) > 4:
        errors.append(f"{case_id}: selected {len(result['selected'])} skills")
    if result["needs_decision"] and result["selected"]:
        errors.append(f"{case_id}: decision pending but skills were selected")
    if result["needs_decision"] and result["code_edits"]:
        errors.append(f"{case_id}: decision pending but edits are allowed")
    if result["code_edits"] and not result["needs_decision"] and not result["plan_approval"]:
        errors.append(f"{case_id}: edits without plan approval")
    if result["mockup"] != "none" and not result["plan_approval"]:
        errors.append(f"{case_id}: mockup without plan approval")
    if result["mockup"] == "image" and result["verify_mode"] != "browser":
        errors.append(f"{case_id}: image mockup without browser")
    overlap = set(result["selected"]) & set(result["missing"])
    if overlap:
        errors.append(f"{case_id}: selected and missing overlap {sorted(overlap)}")
    return errors


def main() -> int:
    cases = json.loads(CASES.read_text())
    seen = set()
    failures = []
    for case in cases:
        case_id = case["id"]
        if case_id in seen:
            failures.append(f"duplicate id {case_id}")
            continue
        seen.add(case_id)
        got = route(case)
        failures.extend(assert_invariants(case_id, got))
        expect = case["expect"]
        for key, expected in expect.items():
            actual = got[key]
            if actual != expected:
                failures.append(f"{case_id}.{key}: expected {expected!r} got {actual!r}")
    if failures:
        print(f"FAIL {len(failures)}")
        for line in failures:
            print(line)
        return 1
    print(f"PASS {len(cases)} routing cases")
    return 0


if __name__ == "__main__":
    sys.exit(main())
