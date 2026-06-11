"""meter 환산·타 단위 변환 (entity)."""

from entity.registry import SUPPORTED_UNITS, from_meters_multiplier, meters_divisor


def to_meters(unit: str, value: float) -> float:
    if unit not in SUPPORTED_UNITS:
        raise ValueError(f"Unknown unit: {unit}")
    return value / meters_divisor(unit)


def from_meters(unit: str, meters: float) -> float:
    if unit not in SUPPORTED_UNITS:
        raise ValueError(f"Unknown unit: {unit}")
    return meters * from_meters_multiplier(unit)
