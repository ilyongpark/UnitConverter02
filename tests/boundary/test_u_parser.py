"""boundary parser — UI Track (U-*). Phase: GREEN."""

import pytest

from boundary.messages import INVALID_FORMAT, invalid_number
from boundary.parser import ParseError, parse


def test_u001_rejects_missing_colon():
    """U-001 | REQ-VAL-01 | PRD §4

    Track: UI (U-*)
    Layer: boundary
    검증: 콜론 없음 → Invalid format. Use unit:value (ex: meter:2.5)
    """
    with pytest.raises(ParseError) as exc_info:
        parse("meter2.5")
    assert exc_info.value.message == INVALID_FORMAT


def test_u002_rejects_non_numeric_value():
    """U-002 | REQ-VAL-03 | PRD §4

    Track: UI (U-*)
    Layer: boundary
    검증: meter:abc → Invalid number: abc
    """
    with pytest.raises(ParseError) as exc_info:
        parse("meter:abc")
    assert exc_info.value.message == invalid_number("abc")


def test_u003_parses_valid_unit_value():
    """U-003 | REQ-IN-01 | PRD §4

    Track: UI (U-*)
    Layer: boundary
    검증: meter:2.5 → (unit, value) 파싱 성공
    """
    parsed = parse("meter:2.5")
    assert parsed.unit == "meter"
    assert parsed.value == 2.5
