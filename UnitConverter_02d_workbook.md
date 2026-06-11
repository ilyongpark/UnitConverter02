# UnitConverter_02d 워크북

> **Mom Test 시뮬레이션 기반** · 가상 인터뷰 결과를 프로젝트 스코프로 전환  
> 이번 세션 산출물: **Rule · Command · (Skill) · Test Loop** (8계층 중 4개)

---

## Mom Test 결과 요약

| 항목 | 내용 |
|------|------|
| **페르소나** | 대학 2학년 소프트웨어 공학 실습 수강생. `UnitConverter.py` 단일 파일을 출발점으로, README(PRD)와 테스트로부터 **추적 가능하게** 길이 단위 변환 CLI를 재구현하는 6시간 과제를 받음. |
| **진짜 문제 (한 문장)** | 모호한 PRD를 런타임·계산기로만 확인하고 검증 없이 구조부터 바꾼 뒤, 마감 직전에는 데모에 보이는 요구사항만 문서·슬라이드에 남기고 나머지는 빈 파일·빈 테스트로 채워 발표를 맞추는 순서 문제. |
| **Mom Test 증거 3줄** | ① 첫 30분 `meter:2.5` 실행 시 README 예시(`8.2 feet`)와 실제 출력(`8.2021…`) 불일치 → 반올림 규칙이 PRD에 없어 **계산기로 수동 검증**함. ② 클래스를 테스트보다 먼저 쪼갠 뒤 `feet:10` 넣었을 때 yard 출력이 틀려짐 → **그때서야** meter/feet/yard **변환 확인용 실행 3번**을 따로 적어 둠. ③ 마지막 1시간: `units.json`은 `{}`만 저장하고 닫음, `test_load_units_config.py`는 `pass`만 있는 채 커밋함, 발표 슬라이드 7번 불릿에는 "설정 외부화·동적 등록 **진행 중**"이라고만 적고 **입력 검증 화면 캡처 1장**을 붙임. |

### Mom Test Turn 3 (질문 수정 · 가상)

**인터뷰어:** JSON 설정·동적 단위 요구사항을 결국 구현하지 못한 그날, **마지막 1시간에** 실제로 연 **파일·커밋·발표 슬라이드** 중 어디에 그 항목을 **어떻게** 적었나요?

**페르소나:** 발표가 30분 남았을 때쯤이요. VS Code에 `units.json`이랑 `test_load_units_config.py`가 탭에 남아 있었는데, JSON에는 `{}`만 넣고 저장한 뒤 닫았어요. 테스트 파일은 `def test_load_units_config(): pass` 한 줄만 있고, 커밋 메시지는 "WIP: units config"였습니다. 슬라이드는 PowerPoint 7번 불릿에 "설정 외부화·동적 등록 — 진행 중"이라고만 썼고, 데모 자리에는 `meter:-1` 넣으면 에러 나는 **터미널 캡처**를 크게 붙였어요. JSON이나 cubit 등록은 실행하지 않았습니다.

---

## 1) 주제 (한 문장)

**PRD에서 모호한 출력·변환 규칙을 테스트로 먼저 고정하고, README 요구사항과 코드·테스트를 REQ 단위로 추적 가능하게 만든다.**

*(솔루션 최소화: OCP 리팩터링·JSON·동적 등록·출력 포맷 전체 구현이 아니라, “검증 가능한 스펙 고정 + 추적”에만 집중)*

---

## 2) R-G-I-O

| | 내용 |
|---|------|
| **Role** | 실습 수강생(또는 이를 보조하는 Cursor Agent). PRD를 읽고 기존 `UnitConverter.py`의 동작을 테스트로 고정한 뒤, 요구사항↔테스트↔코드 연결을 유지하며 최소 변경으로 CLI를 정리함. |
| **Goal** | 구조를 바꾸기 **전에** “무엇이 맞는 출력·변환인지”를 테스트로 확정하고, 이후 변경 시 **어느 REQ가 깨졌는지** 바로 알 수 있는 상태를 만든다. |
| **Input** | `README.md`(PRD), `UnitConverter.py`(기존 코드), Mom Test 증거(반올림 모호성·테스트 후행 리팩터링·선택적 추적) |
| **Output** | Rule / Command / (Skill) / Test Loop 아티팩트 + REQ 매핑이 있는 테스트 스위트 + “이번에 하지 않는 것”이 명시된 스코프 문서 |

---

## 3) 성공 기준 3개 (Mom Test 증거 연결)

| # | 성공 기준 | 연결된 Mom Test 증거 |
|---|-----------|----------------------|
| **SC-1** | `meter:2.5` 등 README 예시에 대응하는 **출력·반올림 테스트**가 존재하고, 실패 시 **어느 PRD 문장(또는 REQ ID)** 을 위반했는지 테스트 docstring 또는 trace에서 식별 가능하다. | ① 계산기 수동 검증 — *스펙을 테스트로 선행 고정* |
| **SC-2** | meter / feet / yard 핵심 변환 테스트가 **구조 변경·리팩터링 전에** 작성되어 통과하고, 이후 코드 변경 시 **동일 테스트로 회귀**를 즉시 검출할 수 있다. | ② 테스트 없이 클래스 분리 후 회귀 — *안전망 선행* |
| **SC-3** | 기본·품질 요구사항 각 항목이 **REQ ID ↔ 테스트 파일/이름 ↔ 코드 위치**로 매핑되어 있으며, 미구현 항목은 빈 파일·`pass` 테스트·"진행 중" 슬라이드가 아니라 **“미구현(Out of scope)”** 으로 명시된다. | ③ 마감 1시간 `{}` JSON·`pass` 커밋·슬라이드 "진행 중" — *데모용 흔적과 추적을 분리* |

---

## 4) 표면 문제 — 이번 프로젝트에서 하지 않을 것

Mom Test에서 **증상**으로만 드러났고, **진짜 문제(스펙·순서·추적)** 해결과 무관하거나 이번 세션 스코프를 벗어나는 항목.

| 하지 않을 것 | 이유 (표면 vs 진짜) |
|--------------|---------------------|
| OCP/SRP를 목표로 한 **대규모 클래스·인터페이스 설계** | 표면: “클린 아키텍처 구현” — 진짜: 테스트 없는 구조 변경이 회귀를 유발함. 구조는 테스트 통과 **이후** 최소 범위만. |
| JSON/YAML **설정 외부화** 전체 구현 | 표면: “추가 요구사항 1번” — 진짜: 스켈레톤만 두면 추적이 깨짐. 이번 세션은 **미구현 명시**로 처리. |
| **동적 단위 등록** (`1 cubit = 0.4572 meter`) | 표면: “기능 확장” — 진짜: 기본 변환·검증·출력 규칙이 고정되지 않은 상태에서 확장하면 모호성만 증가. |
| JSON / CSV / **다중 출력 포맷** | 표면: “출력 개선” — 진짜: 반올림·표시 규칙이 PRD에 없어 포맷만 늘리면 검증 부담 증가. |
| **6시간 전체 커리큘럼** 일괄 완료를 성공으로 정의 | 표면: “발표 가능한 달성도” — 진짜: DoD는 **SC-1~3(테스트·추적)** 충족. |
| 계산기·수동 실행으로 **“맞는지” 확인하는 루틴** | 표면: “동작 확인” — 진짜: Test Loop가 그 역할을 대체해야 함. |

---

## 8계층 — 이번 세션에서 만드는 것

> 전체 8계층 중 **Rule · Command · (Skill) · Test Loop** 만 작성. 나머지 계층(Agent, Hook, Automation, MCP 등)은 **이번 세션 범위 외**.

### Rule

**파일:** `.cursor/rules/unitconverter-02d.mdc` (또는 프로젝트 `AGENTS.md`에 동일 내용)

```markdown
# UnitConverter_02d — PRD-테스트-코드 추적 규칙

## 진짜 문제 (Mom Test)
- PRD 모호성을 런타임·수동 검증으로 해결하지 말 것.
- 테스트 없이 구조(OCP/SRP)부터 바꾸지 말 것.
- 미구현 요구사항은 스켈레톤 테스트로 남기지 말고 "Out of scope"로 명시할 것.

## 작업 순서 (강제)
1. README 예시 입력·출력 → 테스트로 고정 (반올림 규칙 README에 없으면 테스트 docstring에 결정 근거 기록)
2. meter/feet/yard 변환 + 입력 검증 테스트 통과
3. 그 다음에만 최소 리팩터링 (기존 테스트 유지)
4. 모든 테스트/코드에 REQ ID 주석 또는 docstring 매핑

## 금지
- JSON 설정, 동적 단위, 다중 출력 포맷 구현 (이번 세션)
- "일단 클래스부터" 리팩터링
- 계산기로 수동 검증 후 테스트 생략
```

---

### Command

**파일:** `.cursor/commands/unitconverter-test-loop.md` (슬래시 커맨드)

| 커맨드 | 용도 |
|--------|------|
| `/uc-req-map` | README 항목을 REQ ID 목록으로 추출하고, 테스트·코드 매핑 테이블 초안 생성 |
| `/uc-spec-test` | README 예시(`meter:2.5` → `8.2 feet` 등)를 실패하는 테스트부터 작성 (RED) |
| `/uc-trace-check` | SC-3 검증: 매핑 누락·스켈레톤-only 항목 목록 출력 |
| `/uc-test-loop` | `pytest` 실행 → 실패 시 해당 REQ ID와 PRD 문장 인용 → 수정 → 재실행 (Test Loop 진입) |

**Command 본문 예시 (`/uc-test-loop`):**

```markdown
UnitConverter_02d Test Loop를 실행한다.

1. `pytest tests/ -v` 실행
2. 실패 시: 실패 테스트의 REQ ID와 README 해당 문장을 인용
3. 반올림/출력 불일치면 PRD에 규칙이 없음을 명시하고, 테스트 docstring에 채택한 규칙(예: 소수 1자리 반올림) 기록
4. 코드 수정은 실패 테스트를 통과시키는 최소 변경만
5. 구조 리팩터링은 모든 SC-1~2 테스트 GREEN 이후에만
6. 다시 pytest until green
```

---

### (Skill) — 선택

**파일:** `.cursor/skills/unitconverter-prd-trace/SKILL.md`

**트리거:** PRD↔테스트 추적, REQ 매핑, Mom Test 기반 스코프 확인 요청 시

**스킬 요약:**

1. README `기본 요구사항` / `품질 요구사항`만 in-scope로 분류
2. `추가 요구사항` 3항목은 `Out of scope` 표로 분리
3. 각 in-scope 항목에 `REQ-{area}-{nn}` 부여
4. 테스트 템플릿 생성 시 docstring에 `REQ-`, `PRD:` 줄 번호 포함
5. SC-1~3 체크리스트로 완료 여부 보고

*(Skill은 Rule·Command만으로 부족할 때 보조. 이번 세션 필수는 Rule + Command + Test Loop.)*

---

### Test Loop

**파일:** `tests/` + `scripts/test_loop.ps1` (또는 `Makefile` target `test-loop`)

#### 루프 정의

```
[READ PRD 예시] → [RED: 예시 출력 테스트 작성] → [GREEN: UnitConverter 최소 수정]
       ↑                                                    |
       |              [REFACTOR: 테스트 유지, 최소 구조 정리]  |
       +-------- [pytest 전체] ← 실패 시 REQ ID로 되돌아감 ---+
```

#### 최소 테스트 구조 (이번 세션)

| 파일 | REQ | Mom Test 연결 |
|------|-----|---------------|
| `tests/test_output_format.py` | REQ-OUT-01 | SC-1: README 예시 출력·반올림 |
| `tests/test_conversion.py` | REQ-CONV-01~03 | SC-2: meter/feet/yard 변환 |
| `tests/test_input_validation.py` | REQ-VAL-01~03 | SC-3: 음수·형식·unknown unit |
| `tests/REQ_TRACE.md` | — | SC-3: REQ ↔ 테스트 ↔ 코드 매핑 테이블 |

#### Test Loop 실행

```powershell
# scripts/test_loop.ps1
pytest tests/ -v --tb=short
if ($LASTEXITCODE -ne 0) {
    Write-Host "FAIL: Fix failing REQ before refactor. See test docstrings."
    exit $LASTEXITCODE
}
Write-Host "GREEN: Safe to proceed with minimal refactor only."
```

#### RED 예시 (SC-1)

```python
# tests/test_output_format.py
"""REQ-OUT-01 | PRD: README 기본 요구사항 예시 (meter:2.5 → 8.2 feet, 2.7 yard)"""

def test_meter_2_5_matches_prd_example(capsys):
    # 채택 규칙: PRD 예시와 일치하도록 소수 1자리 반올림 (docstring에 근거 기록)
    ...
```

---

## 세션 체크리스트

- [ ] Mom Test 진짜 문제가 Rule에 반영됨
- [ ] `/uc-test-loop` 또는 동등 Command 동작
- [ ] SC-1: README 예시 테스트 + 반올림 근거 docstring
- [ ] SC-2: 변환 테스트가 리팩터링 **전** 존재
- [ ] SC-3: `REQ_TRACE.md`에 미구현 항목 **Out of scope** 명시
- [ ] 표면 문제 항목(JSON·동적 단위·다중 포맷·대규모 OCP) **미착수**

---

*워크북 버전: UnitConverter_02d · Mom Test 가상 인터뷰 기반 · 세션 산출: Rule, Command, (Skill), Test Loop*
