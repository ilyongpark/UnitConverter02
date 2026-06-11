# Golden Master — GREEN baseline

> REFACTOR 시작 **전** 동작 기준. 테스트·CLI 스냅샷 변경 없이 구조만 바꾼다.

| 항목 | 값 |
|------|-----|
| Phase | GREEN (pre-REFACTOR) |
| 확보일 | 2026-06-11 |
| 검증 명령 | `pytest tests/ -v` |
| 기대 결과 | **24 passed** (+ golden 6 passed) |
| 진짜 master | `src/boundary/cli.py` 경유 ECB (레거시 `UnitConverter.py` **아님**) |

---

## 1. pytest Golden Master (24 tests)

### Logic Track (D-*) — 15 tests

| ID | 파일::함수 | REQ |
|----|------------|-----|
| D-001 | test_d_rounding.py::test_d001_meter_2_5_feet_rounds_to_8_2 | REQ-OUT-01 |
| D-002 | test_d_rounding.py::test_d002_meter_2_5_yard_rounds_to_2_7 | REQ-OUT-01 |
| D-003 | test_d_rounding.py::test_d003_round_half_up_at_boundary | REQ-OUT-01 |
| D-010 | test_d_conversion.py::test_d010_meter_to_meters_identity | REQ-CONV-01 |
| D-011 | test_d_conversion.py::test_d011_feet_to_meters | REQ-CONV-02 |
| D-012 | test_d_conversion.py::test_d012_yard_to_meters | REQ-CONV-03 |
| D-013 | test_d_conversion.py::test_d013_meters_to_feet_raw_precision | REQ-CONV |
| D-014 | test_d_conversion.py::test_d014_meters_to_yard_raw_precision | REQ-CONV |
| D-015 | test_d_conversion.py::test_d015_feet_to_yard_via_meters | REQ-CONV-02 |
| D-020 | test_d_validation.py::test_d020_rejects_negative_value | REQ-VAL-02 |
| D-021 | test_d_validation.py::test_d021_rejects_unknown_unit | REQ-VAL-04 |
| D-022 | test_d_validation.py::test_d022_accepts_supported_unit_and_non_negative | REQ-VAL |
| D-030 | test_d_convert_use_case.py::test_d030_converts_meter_input_to_all_units | REQ-CONV |
| D-031 | test_d_convert_use_case.py::test_d031_propagates_negative_validation_error | REQ-VAL-02 |
| D-032 | test_d_convert_use_case.py::test_d032_propagates_unknown_unit_validation_error | REQ-VAL-04 |

### UI Track (U-*) — 9 tests

| ID | 파일::함수 | REQ |
|----|------------|-----|
| U-001 | test_u_parser.py::test_u001_rejects_missing_colon | REQ-VAL-01 |
| U-002 | test_u_parser.py::test_u002_rejects_non_numeric_value | REQ-VAL-03 |
| U-003 | test_u_parser.py::test_u003_parses_valid_unit_value | REQ-IN-01 |
| U-010 | test_u_formatter.py::test_u010_formats_meter_to_feet_line | REQ-OUT-01 |
| U-011 | test_u_formatter.py::test_u011_formats_meter_to_yard_line | REQ-OUT-01 |
| U-012 | test_u_formatter.py::test_u012_preserves_original_value_without_rounding | REQ-OUT-01 |
| U-020 | test_u_cli.py::test_u020_prompts_with_prd_message | REQ-IN-01 |
| U-021 | test_u_cli.py::test_u021_prints_three_lines_for_meter_input | REQ-OUT-01, SC-1 |
| U-022 | test_u_cli.py::test_u022_invalid_format_exits_without_conversion_output | REQ-VAL-01 |

---

## 2. CLI Golden Master (6 scenarios)

정의: [`cli_scenarios.json`](cli_scenarios.json)  
검증: [`test_u_golden_cli.py`](../boundary/test_u_golden_cli.py)

| ID | 입력 | 핵심 기대 |
|----|------|-----------|
| GM-001 | `meter:2.5` | `8.2 feet`, `2.7 yard` (PRD SC-1) |
| GM-002 | `feet:10` | 3줄 반올림 출력 |
| GM-003 | `meter2.5` | 형식 오류 1줄, `=` 없음 |
| GM-004 | `meter:abc` | `Invalid number: abc` |
| GM-005 | `meter:-1` | 음수 거부 |
| GM-006 | `cubit:1` | `Unknown unit: cubit` |

---

## 3. 레거시와의 차이 (REFACTOR 목표)

| 항목 | `UnitConverter.py` (레거시) | Golden (ECB) |
|------|----------------------------|--------------|
| 반올림 | 없음 (`8.2021…`) | 1자리 round half up |
| 음수 | 통과 | 거부 |
| 구조 | God Function | ECB 3계층 |

REFACTOR 후 `UnitConverter.py`는 **golden master(ECB)와 동일 동작**해야 한다.

---

## 4. REFACTOR 전 검증 절차

```powershell
# 전체 (24 + golden 6)
pytest tests/ -v

# 또는
.\scripts\verify_golden.ps1
```

**통과 기준:** 30 passed, 0 failed. 실패 시 REFACTOR 중단 → 구현 수정 (assert 완화 금지).

---

## 5. git tag (선택 — commit 요청 시)

```bash
git tag golden-master-green -m "GREEN 24+6 tests, pre-REFACTOR"
```

커밋·태그는 **사용자 요청 시에만** 수행.
