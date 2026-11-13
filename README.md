# design-director

설치된 디자인 스킬 중에서 이번 작업에 필요한 것만 고르고, 그 스킬의 절차로 실행한 뒤 결과를 검증한다. Impeccable, Taste, Hallmark 같은 하위 스킬은 이 저장소에 들어 있지 않다. 받는 사람 컴퓨터에 있는 것만 쓰고, 없으면 저장소 링크만 알린다.

스킬 본문은 [`plugins/design-director/skills/design-director/SKILL.md`](plugins/design-director/skills/design-director/SKILL.md)다.

## 설치

### Grok

```bash
grok plugin marketplace add oth54477/design-director
grok plugin install design-director --trust
```

### Claude Code

```bash
claude plugin marketplace add oth54477/design-director
claude plugin install design-director@design-director
```

### Codex

```bash
codex plugin marketplace add oth54477/design-director
codex plugin add design-director@design-director
```

새 세션에서 `/design-director`로 호출한다.

플러그인을 쓰지 않는 호스트:

```bash
git clone https://github.com/oth54477/design-director.git
ln -s "$PWD/design-director/plugins/design-director/skills/design-director" ~/.claude/skills/design-director
```

## English

design-director routes a UI task to the design skills already installed on that machine. It does not vendor those skills.

Install with one of the command pairs above, start a new session, and run `/design-director`.

## License

MIT. See [LICENSE](LICENSE).
