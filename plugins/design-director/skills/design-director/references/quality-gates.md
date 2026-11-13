# Quality gates

점수는 1에서 5다. 각 점수 옆에 근거를 적고, 그 근거가 측정인지 판단인지 표시한다.

| 항목 | 측정 예 | 판단 예 |
|---|---|---|
| Visual Hierarchy | 제목 단계, 대비 | 어디가 먼저 읽히는지 |
| Design Consistency | 토큰 이탈 개수 | 톤이 맞는지 |
| Information Architecture | 이름과 경로 | 작업 순서가 맞는지 |
| Usability | 레이블, 에러 위치 | 흐름이 짧은지 |
| Accessibility | 키보드 함정, alt, 명도 도구 수치 | 읽기 쉬운지 |
| Responsive Quality | 넘침, 확인한 폭 | 좁은 화면의 밀도 |
| Motion & Performance | 레이아웃 속성 애니메이션, reduced-motion | 움직임이 과한지 |

점수가 높아도 WCAG 준수라고 쓰지 않는다. 준수는 가이드라인 항목과 대비·키보드 같이 확인한 항목만 말한다.

심각도:

- P0 — 사용 불가, 데이터 손실, 키보드로 도달 불가
- P1 — 핵심 과업이 어렵거나 기존 토큰과 어긋남
- P2 — 완성도를 떨어뜨림
- P3 — 취향과 미세 조정

자동 수정은 P0 와 P1 부터, 최대 두 번이다. 두 번 뒤에도 남으면 남은 문제를 보고하고 멈춘다. 감사 전용 라우트에서는 고치지 않는다.

Render 를 하지 못했으면 Visual Hierarchy, Responsive Quality, Motion 은 "미확인"으로 두고 점수를 주지 않는다. 정적 분석으로 본 항목만 점수를 준다.

브라우저 도구는 이 세션에서 실제로 붙은 것만 쓴다. Playwright, Chrome DevTools, Storybook, 프로젝트 테스트가 연결되지 않았으면 연결됐다고 쓰지 않는다.

에이전트가 직접 화면을 열 때의 도구 순서는 전역 CLAUDE.md 를 따른다: `aside-browser` 스킬이 기본이다. claude-in-chrome·chrome-devtools·playwright MCP·ego-browser·gstack 은 사용자가 지정했거나 aside-browser 가 2~3회 연속 실패할 때만 쓰고, 바꿨다는 사실을 보고에 적는다. 하위 스킬 스크립트가 자체로 띄우는 브라우저(taste `shoot.mjs`, hallmark `--render`, huashu Playwright)는 이 순서와 별개이며 카탈로그·security 규칙을 따른다.
