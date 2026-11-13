# design-director

설치된 디자인 스킬 중 필요한 것만 골라 UI 작업을 진행하고 검증한다. 스타일 스킬을 한 번에 여러 개 적용하지 않는다.

경로와 설치 여부는 `python3 <이 디렉터리>/scripts/inspect-skills.py` 가 출력한다. 이 스킬은 하위 스킬을 설치하지 않는다.

라우팅 검사는 `python3 <이 디렉터리>/scripts/validate-routing.py` 다.
