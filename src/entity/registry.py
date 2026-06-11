"""지원 단위·변환율 레지스트리 (entity)."""

METER = "meter"
FEET = "feet"
YARD = "yard"

SUPPORTED_UNITS: tuple[str, ...] = (METER, FEET, YARD)

FEET_PER_METER = 3.28084
YARDS_PER_METER = 1.09361

_TO_METERS_DIVISOR: dict[str, float] = {
    METER: 1.0,
    FEET: FEET_PER_METER,
    YARD: YARDS_PER_METER,
}

_FROM_METERS_MULTIPLIER: dict[str, float] = {
    METER: 1.0,
    FEET: FEET_PER_METER,
    YARD: YARDS_PER_METER,
}


def meters_divisor(unit: str) -> float:
    return _TO_METERS_DIVISOR[unit]


def from_meters_multiplier(unit: str) -> float:
    return _FROM_METERS_MULTIPLIER[unit]
