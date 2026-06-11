"""entity validation — Logic Track (D-*). Phase: GREEN."""

import pytest

from entity.validation import ValidationError, validate


def test_d020_rejects_negative_value():
    """D-020 | REQ-VAL-02 | PRD §4

    Track: Logic (D-*)
    Layer: entity
    검증: 값 < 0 거부
    """
    with pytest.raises(ValidationError):
        validate("meter", -1.0)


def test_d021_rejects_unknown_unit():
    """D-021 | REQ-VAL-04 | PRD §4

    Track: Logic (D-*)
    Layer: entity
    검증: meter/feet/yard 외 단위 거부
    """
    with pytest.raises(ValidationError):
        validate("cubit", 2.5)


def test_d022_accepts_supported_unit_and_non_negative():
    """D-022 | REQ-VAL-02, REQ-VAL-04 | PRD §4

    Track: Logic (D-*)
    Layer: entity
    검증: meter + 2.5 → 통과
    """
    validate("meter", 2.5)
