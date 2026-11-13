# Context analysis

라우팅 전에 저장소와 요청에서 아래를 채운다. 추측한 항목은 추측이라고 적는다. 브라우저나 스크린샷이 없으면 Current State 의 렌더 칸에 "정적 분석만" 이라고 쓴다.

## Project

- 목적, 사용자, 제품 종류(SaaS, dashboard, landing, mobile, docs, document)
- 스택: `package.json`, `pubspec.yaml`, Swift 패키지, CSS 진입점. 스택이 안 보이면 가정하지 않는다.
- 공용 컴포넌트, 토큰, DESIGN.md / PRODUCT.md, Storybook, 라이트·다크, 반응형 브레이크포인트

디자인 시스템이 있다는 증거는 토큰 파일, 테마 객체, 공용 UI 패키지, DESIGN.md, 반복되는 컴포넌트 API 중 하나다. 이것만 보고 새 토큰 체계를 제안하지 않는다.

## Task

improve, new-product, landing, motion, explore, document, audit 중 하나. 사용자가 감사만 말했으면 audit 이고, 이때 다른 task 로 올리지 않는다.

모션이면 single, group, jank 중 하나. 플랫폼이 Expo 이면 `animate-expo` 를 먼저 찾는다.

## Design

- 기존 스타일을 유지하는지, 브랜드가 고정인지
- 정보 밀도, 작업 효율, 새로움, 인터랙션, 접근성, 성능 예산
- 마케팅 페이지의 brand_hint: theme (테마, 반 AI 패턴, Hallmark 지명) 또는 art (브랜드, 프리미엄, Taste 지명). 힌트가 없으면 art 쪽 기본값인 taste 다. 디자인 시스템이 있으면 이 힌트만으로 리드를 바꾸지 않는다.

## Current State

- 구현이 어디까지 와 있는지
- 지금 화면의 문제
- 유지할 동작과 카피
- 고쳐도 되는 파일과 건드리면 안 되는 파일

스크린샷, Storybook, 실행 중인 앱, aside-browser, Playwright, Chrome DevTools 중 실제로 열린 것만 렌더 근거로 쓴다. 도구 이름이 환경에 있다는 이유만으로 그 도구를 썼다고 하지 않는다.
