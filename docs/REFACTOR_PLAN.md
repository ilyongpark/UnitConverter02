# REFACTOR 계획 — UnitConverter_02d

| 항목 | 내용 |
|------|------|
| 선행 조건 | Golden Master 확보 (`tests/golden/`) |
| Phase | REFACTOR |
| 원칙 | 테스트·golden **불변**, 구조만 최소 변경 |
| 금지 | assert 완화, skip, Out of scope 구현 |

---

## 0. Golden Master (확보 완료)

| 자산 | 경로 | 역할 |
|------|------|------|
| pytest 24 | `tests/**/test_d_*.py`, `test_u_*.py` | Dual-Track GREEN |
| CLI 6 | `tests/golden/cli_scenarios.json` | E2E characterization |
| golden 테스트 | `tests/boundary/test_u_golden_cli.py` | JSON ↔ stdout 검증 |
| 검증 스크립트 | `scripts/verify_golden.ps1` | REFACTOR 전후 실행 |
| 문서 | `tests/golden/GOLDEN_MASTER.md` | 기준·목록 |

**검증:** `pytest tests/ -v` → **30 passed**

---

## 1. REFACTOR 목표

| # | 목표 | Mom Test / DoD |
|---|------|----------------|
| R-1 | `UnitConverter.py` → `boundary.cli.main()` 위임 | 레거시 God Function 제거 |
| R-2 | golden master와 **동일 CLI 동작** | SC-1, SC-2 회귀 없음 |
| R-3 | ECB 의존 방향 유지 | REQ-QUAL-02 |
| R-4 | `REQ_TRACE.md` 상태 `REFACTOR`/`완료` 갱신 | SC-3 |

---

## 2. 작업 순서

```
[0] verify_golden.ps1  → 30 passed 확인
[1] UnitConverter.py 얇은 위임
[2] verify_golden.ps1  → 30 passed (회귀 없음)
[3] REQ_TRACE.md 갱신
[4] (선택) .gitignore __pycache__
[5] (선택) README 실행 경로·구조 표 업데이트
```

각 단계 후 **반드시** `pytest tests/ -v` 실행.

---

## 3. R-1 — `UnitConverter.py` 위임 (핵심)

### 현재

- 루트 `UnitConverter.py`: 37줄 God Function, 반올림·음수 미구현
- `src/boundary/cli.py`: golden master 동작

### 변경 (최소 diff)

```python
from boundary.cli import main

if __name__ == "__main__":
    main()
```

### 검증

- `test_u_golden_cli.py` 6건 통과
- `python UnitConverter.py` + `meter:2.5` → PRD 3줄 (수동 smoke, 선택)

---

## 4. 하지 않을 것 (Out of Scope · REFACTOR)

| 항목 | 사유 |
|------|------|
| JSON/YAML 설정 | PRD §3.2 |
| 동적 단위 등록 | PRD §3.2 |
| JSON/CSV 출력 | PRD §3.2 |
| 대규모 Protocol/Factory | PRD §3.2 |
| 기존 24+6 테스트 수정 | golden master 불변 |
| entity API 대규모 rename | 최소 diff |

---

## 5. 리스크 · 완화

| 리스크 | 완화 |
|--------|------|
| `pythonpath` / import 경로 | `pyproject.toml` `pythonpath = ["src"]` 유지; 실행 시 `PYTHONPATH=src` |
| 레거시와 golden 혼동 | golden = ECB만; `GOLDEN_MASTER.md` 명시 |
| REFACTOR 중 테스트 깨짐 | 단계마다 `verify_golden.ps1` |
| Mom Test “데모용 흔적” | 빈 파일·pass·assert 완화 금지 |

---

## 6. 완료 기준 (REFACTOR DoD)

- [ ] `pytest tests/ -v` — **30 passed**
- [ ] `UnitConverter.py` — 5줄 이내 위임
- [ ] `tests/golden/cli_scenarios.json` — 변경 없음
- [ ] `REQ_TRACE.md` — In-scope `완료`, Out of scope 명시
- [ ] (선택) git tag `golden-master-green` — **commit 요청 시**

---

## 7. REFACTOR 후 (범위 외 · 참고)

워크북 8계층 중 미착수 (이번 REFACTOR에 포함 안 함):

- `.cursor/rules/unitconverter-02d.mdc`
- Command 4종 (`/uc-test-loop` 등)
- Skill `unitconverter-prd-trace`
- `scripts/test_loop.ps1` (verify_golden과 별도)

---

*Golden Master 확보 후 REFACTOR 착수. commit·tag는 사용자 요청 시.*
