"""boundary formatter — UI Track (U-*). Phase: GREEN."""

from entity.rates import FEET_PER_METER, YARDS_PER_METER
from boundary.formatter import format_line


def test_u010_formats_meter_to_feet_line():
    """U-010 | REQ-OUT-01 | PRD §4.2 | SC-1

    Track: UI (U-*)
    Layer: boundary
    검증: 2.5 meter = 8.2 feet (원본값 반올림 없음, 변환값 1자리)
    """
    line = format_line("meter", 2.5, "feet", 2.5 * FEET_PER_METER)
    assert line == "2.5 meter = 8.2 feet"


def test_u011_formats_meter_to_yard_line():
    """U-011 | REQ-OUT-01 | PRD §4.2 | SC-1

    Track: UI (U-*)
    Layer: boundary
    검증: 2.5 meter = 2.7 yard
    """
    line = format_line("meter", 2.5, "yard", 2.5 * YARDS_PER_METER)
    assert line == "2.5 meter = 2.7 yard"


def test_u012_preserves_original_value_without_rounding():
    """U-012 | REQ-OUT-01 | PRD §4.2

    Track: UI (U-*)
    Layer: boundary
    검증: {원본값}은 사용자 입력 파싱값 그대로 (반올림 없음)
    """
    line = format_line("meter", 2.5, "meter", 2.5)
    assert line.startswith("2.5 meter =")
