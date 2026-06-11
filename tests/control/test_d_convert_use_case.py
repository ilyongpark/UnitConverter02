"""control convert use case — Logic Track (D-*). Phase: GREEN."""

import pytest

from control.convert_use_case import ValidationError, convert_all
from entity.rates import FEET_PER_METER, YARDS_PER_METER


def test_d030_converts_meter_input_to_all_units():
    """D-030 | REQ-CONV-01, REQ-OUT-01 | PRD §4 | SC-2

    Track: Logic (D-*)
    Layer: control
    검증: (meter, 2.5) → 3단위 변환 결과 목록 (I/O 없음, entity 실호출)
    """
    results = convert_all("meter", 2.5)
    assert len(results) == 3
    by_unit = {r.target_unit: r.raw_value for r in results}
    assert by_unit["meter"] == pytest.approx(2.5)
    assert by_unit["feet"] == pytest.approx(2.5 * FEET_PER_METER)
    assert by_unit["yard"] == pytest.approx(2.5 * YARDS_PER_METER)


def test_d031_propagates_negative_validation_error():
    """D-031 | REQ-VAL-02 | PRD §4

    Track: Logic (D-*)
    Layer: control
    검증: 음수 입력 → validation 실패 전파
    """
    with pytest.raises(ValidationError):
        convert_all("meter", -1.0)


def test_d032_propagates_unknown_unit_validation_error():
    """D-032 | REQ-VAL-04 | PRD §4

    Track: Logic (D-*)
    Layer: control
    검증: 미지원 단위 → validation 실패 전파
    """
    with pytest.raises(ValidationError):
        convert_all("cubit", 2.5)
