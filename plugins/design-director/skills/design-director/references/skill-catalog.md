# Skill catalog

경로는 여기 적지 않는다. 실행 전에 `scripts/inspect-skills.py` 를 돌리고, 그 출력이 기준이다. `[present]` 의 첫 `path` 만 읽고, `skip` 으로 나온 복사본은 열지 않는다.

없는 스킬은 설치하지 않는다. 아래 저장소는 안내 링크다.

| id | 디렉터리 이름 | 설치가 없을 때 |
|---|---|---|
| impeccable | `impeccable` | https://github.com/pbakaus/impeccable |
| ui-ux-pro-max | `ui-ux-pro-max` | https://github.com/nextlevelbuilder/ui-ux-pro-max-skill |
| emil | `emil-design-eng` | https://github.com/emilkowalski/skills |
| web-design-guidelines | `web-design-guidelines` | https://github.com/vercel-labs/web-interface-guidelines |
| taste | `design-taste-frontend` | https://github.com/Leonxlnx/taste-skill |
| hallmark | `hallmark` | https://github.com/nutlope/hallmark |
| huashu | `huashu-design` | https://github.com/alchaincyf/huashu-design |
| open-design | `open-design` | https://github.com/nexu-io/open-design |
| kami | `kami` | https://github.com/tw93/kami |

## 호출

- impeccable: 스킬을 읽고, 필요하면 그 디렉터리의 `scripts/impeccable`. 런처가 엔진을 받을 수 있으므로 확인만 할 때는 실행하지 않는다.
- ui-ux-pro-max: `python3 "<그 디렉터리>/scripts/search.py"`. `--domain`, `--stack` 은 그 스킬의 표를 따른다.
- emil: CLI 없다. focus 가 가리키는 SKILL.md 하나만 읽는다. 관련 파일은 `animate`, `animation-performance`, `choreograph`, `improve-animations`, `review-animations`.
- web-design-guidelines: 로컬 CLI 없다. 네트워크가 될 때 `https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md` 를 가져와 `file:line` 으로 적는다.
- taste: `scripts/start.mjs`, `consistency.mjs`, `shoot.mjs`, `perf.mjs`. shoot 과 consistency 는 브라우저가 필요하다.
- hallmark: `node "<hallmark>/scripts/theme.mjs"`, `sloplint.mjs`. `--render` 는 브라우저가 필요하다. `install-hook.mjs` 와 `lint-hook.mjs` 는 실행하지 않는다.
- huashu: `python3 "$HD/scripts/learn.py"`, `design_lint.py`, `verify.py`. 세 방향 전에는 구현하지 않는다. `SKIP_DESIGN_GATE` 를 넣지 않는다.
- open-design: 앱 동반 문서다. 설치가 데몬을 켜지는 않는다. `od mcp install` 은 사용자가 OpenDesign CLI 를 확인한 뒤에만. `/usr/bin/od` 는 시스템 octal dump 다.
- kami: `python3 "<kami>/scripts/build.py"`. `check-update.sh` 는 네트워크가 없으면 건너뛴다.

## 기본 라우트 밖

스크립트가 찾으면 그때만 읽는다.

- `animate-expo` — Expo 모션일 때 animate 대신.
- `find-animation-opportunities` — 무엇을 움직일지 물을 때. 구현 스킬이 아니다.
- `remove-animations` — 없으면 호출하지 않는다. choreograph 본문이 언급해도 같다.

## 복사본

검사 스크립트는 툴킷 디렉터리, `~/.agents/skills`, `~/.claude/skills`, `~/.codex/skills`, `~/.grok/skills`, `~/.grok/bundled/skills`, `~/.cursor/skills` 순서로 찾고 첫 파일만 고른다. 호스트가 이미 다른 복사본을 대화에 넣었다면 그 주입본을 따르고, 두 번째 본문을 겹쳐 읽지 않는다.
