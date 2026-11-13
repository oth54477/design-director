---
name: design-director
description: "Analyze the current project and user intent, select the most appropriate installed design skills, orchestrate design execution, and verify UI quality without conflicting design systems. Use for UI polish, redesign, landing pages, design systems, motion, accessibility audits, and PPT/PDF. 화면을 다듬거나 디자인·랜딩·감사·PPT를 요청할 때 사용한다."
user-invocable: true
---

# design-director

상위 오케스트레이터다. 디자인 규칙을 새로 발명하지 않고, 설치된 스킬 중 필요한 것만 고른 뒤 그 스킬의 절차로 실행하고 검증한다.

이 파일을 읽은 뒤 관련 없는 참조와 하위 스킬은 읽지 않는다.

## 먼저

1. `python3 <이 스킬 디렉터리>/scripts/inspect-skills.py` 를 실행한다. 경로·누락은 이 출력이 기준이다. `references/skill-catalog.md` 의 스냅샷과 다르면 스크립트를 따른다.
2. 저장소와 요청을 `references/context-analysis.md` 기준으로 나눈다. 브라우저나 스크린샷이 없으면 정적 분석만 했다고 적고, 화면을 본 것처럼 쓰지 않는다.
3. `references/skill-router.md` 로 스킬을 고른다. 회귀 케이스는 `tests/routing-cases.json` 이고, `python3 <이 스킬 디렉터리>/scripts/validate-routing.py` 가 그 규칙을 검사한다.
4. 고른 스킬의 카탈로그 행만 읽고, 그 스킬의 `SKILL.md` 만 연다. focus 가 가리키는 하위 문서만 이어서 읽는다.

## 고정 규칙

- 스타일을 정하는 스킬은 한 번에 하나다. taste, hallmark, huashu, ui-ux-pro-max, kami 중 둘 이상을 같이 적용하지 않는다.
- 핵심 스킬은 1~2개, 필요하면 QA 스킬을 하나 더한다. 아홉 개를 모두 실행하지 않는다.
- 이미 있는 디자인 시스템·토큰·컴포넌트가 외부 스킬의 취향보다 우선한다. 자세한 금지 항목은 `references/design-policies.md`.
- 감사만 요청받으면 파일을 고치지 않는다.
- 스킬을 읽는 것과 CLI 를 실행하는 것을 구분한다. 카탈로그에 없는 명령은 실행하지 않는다.
- 외부 모델, 유료 API, 훅 설치, live 모드, OpenDesign 데몬은 사용자가 그 실행을 말하기 전에는 켜지 않는다. `references/security.md`.
- 없는 스킬은 설치하지 않는다. 빠진 이름과 업스트림 저장소만 알린다.
- 검증되지 않은 시각 결과를 성공으로 보고하지 않는다. 수정 후 재검증은 두 번까지. `references/quality-gates.md`.
- 하위 스킬을 실행하기 전에 고른 스킬·Route·Plan 결과를 사용자에게 먼저 보고한다(Brief). 파일을 고치는 라우트는 승인 전에 실행하지 않는다.
- 코드를 쓰기 전에 시안 이미지를 보여 주고 승인을 받는다. 시안 여부는 라우터의 `mockup` 값을 따른다.

## 실행

`references/workflows.md` 의 Inspect → Classify → Route → Plan → Brief → Mockup → Execute → Render → Audit → Repair → Verify → Report 순서를 따른다. Brief 와 Mockup 의 형식·승인 규칙도 그 문서에 있다.

코드를 고치기 전에 `design-policies.md`, `quality-gates.md`, `security.md` 를 읽는다. 감사만이면 policies 의 변경 금지가 적용되고, Execute 는 하지 않는다.

## 보고

기본 보고는 `workflows.md` 의 Design Analysis, Skill Selection, Design Direction, Execution Results, Quality Report 다.

한 컴포넌트의 작은 수정이면 고른 스킬, 바꾼 파일, 확인한 것, 확인하지 못한 것만 남긴다. 이때도 실행 전 Brief 와 시안은 건너뛰지 않는다(사용자가 빼라고 했을 때만 뺀다).
