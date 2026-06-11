"""entity rounding — Logic Track (D-*). Phase: GREEN."""

from entity.rates import FEET_PER_METER, YARDS_PER_METER
from entity.rounding import round_display


def test_d001_meter_2_5_feet_rounds_to_8_2():
    """D-001 | REQ-OUT-01 | PRD §4.3 | SC-1

    Track: Logic (D-*)
    Layer: entity
    검증: 내부값 8.2021… → 소수 1자리 round half up → 8.2
    """
    raw = 2.5 * FEET_PER_METER
    assert round_display(raw) == 8.2


def test_d002_meter_2_5_yard_rounds_to_2_7():
    """D-002 | REQ-OUT-01 | PRD §4.3 | SC-1

    Track: Logic (D-*)
    Layer: entity
    검증: 내부값 2.734025… → 소수 1자리 round half up → 2.7
    """
    raw = 2.5 * YARDS_PER_METER
    assert round_display(raw) == 2.7


def test_d003_round_half_up_at_boundary():
    """D-003 | REQ-OUT-01 | PRD §4.3

    Track: Logic (D-*)
    Layer: entity
    검증: round half up 경계값 (예: 2.25 → 2.3)
    """
    assert round_display(2.25) == 2.3
