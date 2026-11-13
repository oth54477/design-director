# Security

하위 스킬과 그 스크립트는 신뢰하지 않는 코드다. 카탈로그에 적힌 명령만, 읽은 뒤에 실행한다.

## 기본 금지

- 권한 검사를 우회하는 플래그. `--dangerously-bypass-approvals-and-sandbox`, `--dangerously-skip-permissions` 를 붙이지 않는다.
- 전역 패키지 설치. `npm install -g`, `npx playwright install`, 엔진 다운로드를 사용자가 승인하기 전에 하지 않는다. impeccable 런처는 엔진을 받을 수 있으므로, context 실행 전에 그 사실을 말한다.
- 승인 없는 외부·유료 모델. Hallmark 의 이미지 API, Huashu 의 음성·영상, OpenDesign 의 모델 호출이 여기 해당한다.
- 비밀, 토큰, 저장소 밖 사용자 데이터를 쿼리나 프롬프트에 넣기
- 프로덕션 페이지에 편집용 스크립트를 주입
- 사용자 데이터 디렉터리의 대량 수정

## Live 와 훅

impeccable 의 `live`, `generate`, `scripts/live-browser.js` 는 기본 경로에서 빼 둔다. 사용자가 live 를 명시하고, 대상이 로컬 개발 서버이며, 프로덕션 세션이 아닐 때만 `reference/live.md` 를 읽고 실행한다. 그 전에도 주입 스크립트를 먼저 읽고, 비밀 입력 칸에는 쓰지 않는다.

실행하지 않는 설치형 훅:

- impeccable `hooks`
- hallmark `scripts/install-hook.mjs`, `scripts/lint-hook.mjs`
- huashu `scripts/design-gate-hook.sh`
- `SKIP_DESIGN_GATE=1`

## OpenDesign

`/usr/bin/od` 는 OpenDesign 이 아니다. `od mcp install`, 데몬 기동, MCP 설정 변경은 사용자가 그 명령을 요청하고 OpenDesign CLI 경로를 확인한 뒤에만 검토한다.

## 검색과 업데이트

ui-ux-pro-max 검색어에 비공개 제품 데이터를 넣지 않는다. `--persist` 는 프로젝트 안에 파일을 만든다. 기본 focus 는 no-persist 다.

kami `check-update.sh` 는 릴리스 확인이며 문서 본문을 보내지 않는다고 그 스킬이 적는다. 네트워크가 막혀 있으면 건너뛴다. 문서 파일 경로를 그 스크립트의 인자로 넘기지 않는다.
