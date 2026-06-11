"""meter 환산·타 단위 변환 (entity)."""

from entity.rates import FEET_PER_METER, YARDS_PER_METER
from entity.unit import FEET, METER, YARD


def to_meters(unit: str, value: float) -> float:
    if unit == METER:
        return value
    if unit == FEET:
        return value / FEET_PER_METER
    if unit == YARD:
        return value / YARDS_PER_METER
    raise ValueError(f"Unknown unit: {unit}")


def from_meters(unit: str, meters: float) -> float:
    if unit == METER:
        return meters
    if unit == FEET:
        return meters * FEET_PER_METER
    if unit == YARD:
        return meters * YARDS_PER_METER
    raise ValueError(f"Unknown unit: {unit}")
