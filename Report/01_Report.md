# UnitConverter_02d 세션 보고서

| 항목 | 내용 |
|------|------|
| 프로젝트 | UnitConverter02 |
| 세션 ID | UnitConverter_02d |
| 작성일 | 2026-06-11 |
| 유형 | Mom Test 시뮬레이션 → 워크북 → 채점 → 질문 개선 |
| 라벨 | **가상 인터뷰 기반** (실제 수강생·강사 경험과 무관) |

---

## 1. 세션 요약

본 세션은 `UnitConverter02` README(PRD)와 `UnitConverter.py`를 맥락으로, **Mom Test 역할 분리 인터뷰**를 수행하고 그 결과를 **UnitConverter_02d 워크북**으로 전환한 뒤, Mom Test 품질을 채점·개선한 작업이다.

| 단계 | 산출물 |
|------|--------|
| Mom Test 3턴 시뮬레이션 | 가상 인터뷰 (인터뷰어 / 페르소나) |
| 워크북 작성 | `UnitConverter_02d_workbook.md` |
| Mom Test 채점 | 8/10, 개선 질문 1개 제안 |
| 질문 개선 재진행 | Turn 3 수정 · 증거 ③·진짜 문제 갱신 |

---

## 2. Mom Test 결과 (최종)

### 페르소나

대학 2학년 소프트웨어 공학 실습 수강생. `UnitConverter.py` 단일 파일을 출발점으로, README(PRD)와 테스트로부터 **추적 가능하게** 길이 단위 변환 CLI를 재구현하는 6시간 과제를 받음.

### 진짜 문제 (한 문장)

모호한 PRD를 런타임·계산기로만 확인하고 검증 없이 구조부터 바꾼 뒤, 마감 직전에는 데모에 보이는 요구사항만 문서·슬라이드에 남기고 나머지는 빈 파일·빈 테스트로 채워 발표를 맞추는 **순서 문제**.

### Mom Test 증거 3줄

1. **첫 30분** — `meter:2.5` 실행 시 README 예시(`8.2 feet`)와 실제 출력(`8.2021…`) 불일치 → 반올림 규칙이 PRD에 없어 **계산기로 수동 검증**함.
2. **중반** — 클래스를 테스트보다 먼저 쪼갠 뒤 `feet:10` 입력 시 yard 출력 회귀 → **그때서야** meter/feet/yard **변환 확인용 실행 3번**을 따로 적어 둠.
3. **마지막 1시간** — `units.json`은 `{}`만 저장, `test_load_units_config.py`는 `pass`만 커밋(`WIP: units config`), 슬라이드 7번 불릿에 "진행 중"만 기재하고 **입력 검증 터미널 캡처**만 데모에 사용.

### 표면 문제 vs 진짜 문제

| 구분 | 내용 |
|------|------|
| **표면** | 출력 소수점 불일치, 클린 아키텍처 난항, 추가 요구사항(JSON·동적 등록·출력 포맷) 미완 |
| **진짜** | PRD 모호성을 런타임에서만 발견, 검증 없이 구조 변경, 마감 직전 데모용 흔적(WIP·"진행 중")과 실제 추적 혼동 |

---

## 3. 워크북 핵심 (UnitConverter_02d)

### 주제 (한 문장)

PRD에서 모호한 출력·변환 규칙을 테스트로 먼저 고정하고, README 요구사항과 코드·테스트를 REQ 단위로 추적 가능하게 만든다.

### R-G-I-O

| | 내용 |
|---|------|
| **Role** | 실습 수강생(또는 보조 Agent) |
| **Goal** | 구조 변경 전 출력·변환 규칙 확정, REQ 단위 회귀 검출 |
| **Input** | README, UnitConverter.py, Mom Test 증거 |
| **Output** | Rule / Command / (Skill) / Test Loop + REQ 매핑 테스트 스위트 |

### 성공 기준

| ID | 기준 | Mom Test 연결 |
|----|------|---------------|
| SC-1 | README 예시 출력·반올림 테스트 + PRD/REQ 식별 | ① 수동 검증 |
| SC-2 | 변환 테스트가 리팩터링 **전** 존재, 회귀 검출 | ② 순서 실수 |
| SC-3 | 미구현은 Out of scope 명시 (빈 파일·pass·"진행 중" 금지) | ③ 마감 행동 |

### 이번 세션에서 하지 않을 것

- 대규모 OCP/SRP 클래스 설계
- JSON/YAML 설정 외부화 전체 구현
- 동적 단위 등록, 다중 출력 포맷
- 6시간 전체 완료를 DoD로 정의
- 계산기·수동 실행 검증 루틴

### 8계층 (이번 세션 범위)

| 계층 | 산출물 |
|------|--------|
| Rule | `.cursor/rules/unitconverter-02d.mdc` |
| Command | `/uc-req-map`, `/uc-spec-test`, `/uc-trace-check`, `/uc-test-loop` |
| (Skill) | `unitconverter-prd-trace` (선택) |
| Test Loop | `tests/` + `scripts/test_loop.ps1` |

---

## 4. Mom Test 채점 결과

**점수: 8 / 10** (초기 워크북 기준, 수정 전)

| 체크 항목 | 판정 |
|-----------|------|
| 미래 가정 없음 | 통과 |
| 과거 행동·시간·실수 구체성 | 부분 통과 |
| 진짜 문제에 솔루션名 없음 | 부분 통과 |
| 표면/진짜 분리 | 통과 |

**개선 질문 (적용 완료):**

> JSON 설정·동적 단위 요구사항을 결국 구현하지 못한 그날, 마지막 1시간에 실제로 연 파일·커밋·발표 슬라이드 중 어디에 그 항목을 어떻게 적었나요?

**개선 효과:** 증거 ③이 산출물명(`InputValidator`, `REQ-validate`)에서 **구체적 마감 행동**(`{}` JSON, `pass` 커밋, 슬라이드 7번)으로 교체됨. 예상 재채점: **9/10**.

---

## 5. 산출물 목록

| 경로 | 설명 |
|------|------|
| `UnitConverter_02d_workbook.md` | Mom Test 기반 워크북 (전체) |
| `Report/01_Report.md` | 본 보고서 |
| `Prompting/01_Exported_Transcript.md` | 세션 Transcript Export |
| `Prompting/01_Exported_Transcript.jsonl` | 원본 대화 로그 (JSONL) |

---

## 6. 다음 단계 (미착수)

워크북에 정의되었으나 **아직 구현되지 않은** 항목:

- [ ] `.cursor/rules/unitconverter-02d.mdc` 생성
- [ ] Command 4종 생성
- [ ] `tests/` 디렉터리 및 SC-1~3 테스트 작성
- [ ] `scripts/test_loop.ps1` 작성
- [ ] `tests/REQ_TRACE.md` 매핑 테이블 작성

---

*본 보고서는 Mom Test 가상 시뮬레이션 세션의 기록이며, 실제 프로젝트 참여자 경험과 무관합니다.*
