"""entity conversion — Logic Track (D-*). Phase: GREEN."""

import pytest

from entity.conversion import from_meters, to_meters
from entity.rates import FEET_PER_METER, YARDS_PER_METER


def test_d010_meter_to_meters_identity():
    """D-010 | REQ-CONV-01 | PRD §4 | SC-2

    Track: Logic (D-*)
    Layer: entity
    검증: meter 2.5 → meter 기준 2.5 (전체 정밀도)
    """
    assert to_meters("meter", 2.5) == 2.5


def test_d011_feet_to_meters():
    """D-011 | REQ-CONV-02 | PRD §4 | SC-2

    Track: Logic (D-*)
    Layer: entity
    검증: feet 10 → meter (1 meter = 3.28084 feet, meter 경유)
    """
    assert to_meters("feet", 10) == pytest.approx(10 / FEET_PER_METER)


def test_d012_yard_to_meters():
    """D-012 | REQ-CONV-03 | PRD §4 | SC-2

    Track: Logic (D-*)
    Layer: entity
    검증: yard 3 → meter (1 meter = 1.09361 yard, meter 경유)
    """
    assert to_meters("yard", 3) == pytest.approx(3 / YARDS_PER_METER)


def test_d013_meters_to_feet_raw_precision():
    """D-013 | REQ-CONV-01~03 | PRD §4 | SC-2

    Track: Logic (D-*)
    Layer: entity
    검증: meter 2.5 → feet raw (반올림 전, 전체 정밀도)
    """
    assert from_meters("feet", 2.5) == pytest.approx(2.5 * FEET_PER_METER)


def test_d014_meters_to_yard_raw_precision():
    """D-014 | REQ-CONV-01~03 | PRD §4 | SC-2

    Track: Logic (D-*)
    Layer: entity
    검증: meter 2.5 → yard raw (반올림 전, 전체 정밀도)
    """
    assert from_meters("yard", 2.5) == pytest.approx(2.5 * YARDS_PER_METER)


def test_d015_feet_to_yard_via_meters():
    """D-015 | REQ-CONV-02 | PRD §4 | SC-2

    Track: Logic (D-*)
    Layer: entity
    검증: feet ↔ yard는 meter 기준 환산 (직접 비율 사용 금지)
    """
    meters = to_meters("feet", 10)
    yards = from_meters("yard", meters)
    assert yards == pytest.approx((10 / FEET_PER_METER) * YARDS_PER_METER)
