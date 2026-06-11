# REQ 추적 매트릭스

> REQ ID ↔ 테스트 ↔ 코드 위치.

| REQ ID | PRD 절 | 테스트 (파일::함수) | 코드 위치 | 상태 |
|--------|--------|---------------------|-----------|------|
| REQ-IN-01 | §4 | test_u_cli.py::test_u020, test_u003 | `src/boundary/cli.py`, `parser.py` | GREEN |
| REQ-OUT-01 | §4 | test_d_rounding.py::test_d001~002, test_u_formatter.py::test_u010~011, test_u_cli.py::test_u021 | `src/entity/rounding.py`, `boundary/formatter.py` | GREEN |
| REQ-CONV-01 | §4 | test_d_conversion.py::test_d010, test_d013 | `src/entity/conversion.py` | GREEN |
| REQ-CONV-02 | §4 | test_d_conversion.py::test_d011, test_d015 | `src/entity/conversion.py` | GREEN |
| REQ-CONV-03 | §4 | test_d_conversion.py::test_d012, test_d014 | `src/entity/conversion.py` | GREEN |
| REQ-VAL-01 | §4 | test_u_parser.py::test_u001, test_u_cli.py::test_u022 | `src/boundary/parser.py` | GREEN |
| REQ-VAL-02 | §4 | test_d_validation.py::test_d020, test_d031 | `src/entity/validation.py` | GREEN |
| REQ-VAL-03 | §4 | test_u_parser.py::test_u002 | `src/boundary/parser.py` | GREEN |
| REQ-VAL-04 | §4 | test_d_validation.py::test_d021, test_d032 | `src/entity/validation.py` | GREEN |
| REQ-QUAL-01 | §5 | `tests/` 24 passed | `tests/` | GREEN |
| REQ-QUAL-02 | §5 | — | `src/` ECB 구조 | GREEN |
| REQ-TRACE-01 | §5 | — | 본 문서 | 진행 중 |

## Out of Scope (미구현 명시)

| 항목 | 사유 |
|------|------|
| JSON/YAML 설정 외부화 | PRD §3.2 |
| 동적 단위 등록 | PRD §3.2 |
| JSON / CSV / 다중 출력 포맷 | PRD §3.2 |
