#!/usr/bin/env python3
"""Resolve design skills this orchestrator can route to on this machine.

Read-only. Does not install, enable, or edit skills. The first existing
SKILL.md wins. Later copies are listed and must not be opened.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

HOME = Path.home()
ROOTS = (
    HOME / ".local/share/ai-design-toolkit/plugins/design/skills",
    HOME / ".agents/skills",
    HOME / ".claude/skills",
    HOME / ".codex/skills",
    HOME / ".grok/skills",
    HOME / ".grok/bundled/skills",
    HOME / ".cursor/skills",
)

CANONICAL = [
    ("impeccable", ("impeccable",), "한 번에 하나의 스타일 스킬만 연다."),
    ("ui-ux-pro-max", ("ui-ux-pro-max",), "검색은 고른 디렉터리의 scripts/search.py."),
    (
        "emil",
        ("emil-design-eng",),
        "animate, animation-performance, choreograph, improve-animations, review-animations 는 related 로 따로 찾는다.",
    ),
    ("web-design-guidelines", ("web-design-guidelines",), "로컬 CLI 없음. 네트워크가 될 때만 guidelines URL 을 가져온다."),
    ("taste", ("design-taste-frontend",), "정식 디렉터리 이름은 design-taste-frontend. 복사본은 하나만 읽는다."),
    ("hallmark", ("hallmark",), "기존 화면에는 사용자가 Hallmark 를 지명할 때만 쓴다."),
    ("huashu", ("huashu-design",), "새 방향은 세 안을 먼저 보여주고 고른 뒤 구현한다."),
    ("open-design", ("open-design",), "앱 동반 스킬. macOS /usr/bin/od 는 OpenDesign 이 아니다."),
    ("kami", ("kami",), "PDF, PPT, 문서. 제품 UI 수정에 쓰지 않는다."),
]

EXTRA = (
    "animate",
    "animation-performance",
    "choreograph",
    "improve-animations",
    "review-animations",
    "find-animation-opportunities",
    "animate-expo",
    "remove-animations",
)


def frontmatter(path: Path) -> dict[str, str]:
    if not path.is_file():
        return {}
    text = path.read_text(errors="replace")
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    block = text[3:end] if end != -1 else text[:800]
    found: dict[str, str] = {}
    for line in block.splitlines():
        if ":" not in line or line.startswith(" "):
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        if key in {"name", "version"}:
            found[key] = value.strip().strip('"').strip("'")
    return found


def candidates(name: str) -> list[Path]:
    found: list[Path] = []
    seen: set[Path] = set()
    for root in ROOTS:
        path = root / name / "SKILL.md"
        if not path.is_file():
            continue
        identity = path.resolve()
        if identity in seen:
            continue
        seen.add(identity)
        found.append(path)
    return found


def main() -> int:
    print("design-director skill inspection")
    print(f"os={os.uname().sysname} {os.uname().machine}")
    missing = 0
    for skill_id, names, note in CANONICAL:
        found: list[Path] = []
        for name in names:
            found.extend(candidates(name))
        if not found:
            missing += 1
            print(f"[absent] {skill_id}")
            print(f"  note={note}")
            continue
        chosen = found[0]
        meta = frontmatter(chosen)
        print(f"[present] {skill_id} name={meta.get('name', '-')} version={meta.get('version', '-')}")
        print(f"  path={chosen}")
        print(f"  note={note}")
        for extra in found[1:]:
            print(f"  skip={extra}")
    print("related")
    for name in EXTRA:
        found = candidates(name)
        if not found:
            print(f"[absent] {name}")
            continue
        print(f"[present] {name} {found[0]}")
        for extra in found[1:]:
            print(f"  skip={extra}")
    od = Path("/usr/bin/od")
    print("od=system octal dump, not OpenDesign" if od.exists() else "od=absent")
    print(f"canonical_missing={missing}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
