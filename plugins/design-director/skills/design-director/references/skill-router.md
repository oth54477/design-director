# Skill router

결정 순서는 `scripts/validate-routing.py` 와 같다. 케이스와 스크립트가 이 문서와 어긋나면 스크립트와 `tests/routing-cases.json` 을 고치고 이 표도 같이 고친다.

설치 집합의 이름: `impeccable`, `ui-ux-pro-max`, `emil`, `web-design-guidelines`, `taste`, `hallmark`, `huashu`, `open-design`, `kami`. `emil` 은 animate, choreograph, animation-performance, improve-animations, review-animations, emil-design-eng 를 묶은 표식이다. `animate-expo` 는 별도다.

스타일 리드: taste, hallmark, huashu, ui-ux-pro-max, kami. 이 집합에서 둘 이상을 고르면 실패다.

## 순서

1. `audit` — web-design-guidelines, 그다음 impeccable 의 audit. 모션 감사면 review-animations 를 더한다. 파일을 고치지 않는다. CLI 를 돌리지 않는다.
2. `document` — 시각 실험 슬라이드가 아니면 kami. 실험 슬라이드·모션 그래픽이면 huashu 만. 웹 UI 스킬을 붙이지 않는다. 리드가 없으면 다른 스킬로 대체하지 않고 문서를 만들지 않는다.
3. `motion` — 하나만 고른다. single 은 animate, group 은 choreograph, jank 는 animation-performance. Expo 이고 animate-expo 가 있으면 그것을 쓰고, 없으면 animate 로 남기며 animate-expo 가 없다고 적는다. impeccable 을 자동으로 붙이지 않는다.
4. 스타일 스킬을 둘 이상 지명하면 아무것도 고르지 않고 질문한다. 코드를 고치지 않는다.
5. `explore` — 지명이 있으면 그 하나, 없으면 huashu. 작업 공간 연동을 요청했을 때만 open-design 을 더한다.
6. `landing` — 지명이 있으면 그것. 디자인 시스템이 있고 지명이 없으면 taste 와 hallmark 를 쓰지 않는다. 새 페이지이고 theme 힌트면 hallmark, art 힌트이거나 힌트가 없으면 taste. 그다음 impeccable polish, web-design-guidelines.
7. `new-product` — 디자인 시스템이 없을 때만 ui-ux-pro-max. 있으면 그것을 빼 impeccable shape 와 guidelines 만 쓴다.
8. `improve` — 지명한 스타일 스킬이 하나면 그것을 앞에 둔다. 없으면 impeccable polish 와 guidelines. 모션이 필요할 때만 emil 스킬 하나를 더한다. 지명이 없으면 ui-ux-pro-max, taste, hallmark, huashu, kami 를 쓰지 않는다.

없는 스킬은 selected 에서 빼고 missing 에 넣는다. 자동 설치하지 않는다. selected 가 비면 파일을 만들지 않는다.

## 실행 전 보고와 시안

Route 결과에 두 값이 더 붙는다. 형식과 승인 절차는 `workflows.md` 의 「실행 전 보고」「시안」.

- `plan_approval` — 파일을 고치는 라우트(`code_edits` 이고 needs_decision 이 아님)면 true. Brief 를 보여 주고 승인 전에는 실행하지 않는다. 감사·needs_decision·리드 없음은 false 지만 Brief(또는 질문)는 보여 준다.
- `mockup` — 위에서부터 먼저 맞는 것.
  1. plan_approval 이 false, 사용자가 시안을 빼라고 함, task 가 document 또는 motion → `none`
  2. huashu 가 selected 에 있음 → `directions` (huashu 의 세 방향이 시안)
  3. 브라우저 있음 → `image`
  4. 그 밖 → `html-only`

브라우저가 없으면 verify 는 static 이다. CLI 를 쓸 수 없으면 cli_execute 는 false 다. 네트워크가 없으면 guidelines URL 을 가져오지 않고 focus 는 `web-design-guidelines:local-only` 다. 외부 모델은 기본 금지다.

## 요청에서 task 로

| 요청 | task |
|---|---|
| 있는 화면을 다듬기, "세련되게" | improve |
| 디자인 시스템이 없는 새 제품·새 앱 골격 | new-product |
| 브랜드·마케팅 랜딩 | landing. 테마·반 AI 패턴을 명시면 theme, 브랜드·프리미엄을 명시면 art |
| 모달 애니메이션만, 전환만 | motion / single |
| 여러 요소가 같이 움직임 | motion / group |
| 버벅임 | motion / jank |
| 서로 다른 시안 | explore |
| PPT, PDF, 보고서 | document. 실험 영상이면 visual_doc |
| 접근성·품질 검사만 | audit |

디자인 시스템이 있는지는 토큰, 테마, 공용 컴포넌트, DESIGN.md, Storybook 으로 판단한다. 파일 이름만으로 없다고 하지 않는다.

## 케이스

| id | selected | 수정 | 검증 |
|---|---|---|---|
| saas-dashboard-improve | impeccable, web-design-guidelines | 함 | browser |
| new-react-no-design-system | ui-ux-pro-max, impeccable, web-design-guidelines | 함 | browser |
| brand-landing | taste, impeccable, web-design-guidelines | 함 | browser |
| themed-new-page | hallmark, impeccable, web-design-guidelines | 함 | browser |
| modal-motion-only | animate | 함 | browser. CLI 없음 |
| enterprise-keep-design-system | impeccable, web-design-guidelines | 함 | browser |
| ppt-report | kami | 함 | artifact |
| a11y-audit-only | web-design-guidelines, impeccable audit | 안 함 | browser |
| missing-impeccable | web-design-guidelines. impeccable 은 missing | 함 | browser |
| conflicting-style-skills | 없음. 사용자에게 질문 | 안 함 | none |
| no-browser-no-cli-no-model | impeccable, web-design-guidelines | 함 | static. fetch 안 함. CLI 안 함 |
| explore-directions | huashu | 함 | browser |
| explore-with-workspace | huashu, open-design | 함 | browser |
| experimental-slides | huashu | 함 | artifact |
| landing-keeps-existing-system | impeccable, web-design-guidelines | 함 | browser |
| new-product-keeps-existing-system | impeccable, web-design-guidelines | 함 | browser |
| improve-with-motion | impeccable, web-design-guidelines, animate | 함 | browser |
| named-hallmark-on-existing-app | hallmark, impeccable, web-design-guidelines | 함 | browser |
| motion-group | choreograph | 함 | browser |
| motion-jank | animation-performance | 함 | browser |
| audit-includes-motion-review | guidelines, impeccable audit, review-animations | 안 함 | browser |
| ppt-without-kami | 없음. kami missing | 안 함 | artifact |
| expo-motion-fallback | animate. animate-expo missing | 함 | browser |
| expo-motion-present | animate-expo | 함 | browser |
| explore-named-taste | taste | 함 | browser. 시안 image |
| improve-skip-mockup | impeccable, web-design-guidelines | 함 | browser. 시안 none(사용자가 뺌) |
| landing-no-browser | taste, impeccable, web-design-guidelines | 함 | static. 시안 html-only |

시안 값: image — improve·landing·new-product 케이스 전부, directions — explore-directions·explore-with-workspace, html-only — no-browser-no-cli-no-model·landing-no-browser, none — 모션·문서·감사·충돌·리드 없음·improve-skip-mockup.

focus 문자열은 테스트 expect 와 같다. 그 하위 문서만 연다.

- impeccable:polish — 기존 화면의 마무리. new-work 로 세계를 갈아엎지 않는다.
- impeccable:shape — 새 표면을 코드 전에 잡는다.
- impeccable:audit — `reference/audit.md`. 수정 없음.
- ui-ux-pro-max:design-system-no-persist — `--design-system` 만. `--persist` 와 `--force` 는 사용자가 파일로 남기라고 할 때만.
- taste:landing, hallmark:new-page — 그 스킬이 스타일을 정한다. impeccable 은 그 결정을 다른 스타일로 바꾸지 않는다.
- huashu:three-directions — 세 방향을 보여주고 고르기 전에는 구현하지 않는다.
- kami:build — 문서 스크립트만.
- animate:implement, choreograph:implement, animation-performance:diagnose, review-animations:review — 해당 SKILL.md 만.
- web-design-guidelines:fetch 또는 local-only.
- open-design:companion-only — 앱이 떠 있을 때만 연결을 논의한다. 데몬을 켜지 않는다.
