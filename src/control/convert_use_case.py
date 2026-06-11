"""변환 유스케이스 조율 (control)."""

from dataclasses import dataclass

from entity.conversion import from_meters, to_meters
from entity.registry import SUPPORTED_UNITS
from entity.validation import ValidationError, validate


@dataclass(frozen=True)
class ConversionResult:
    target_unit: str
    raw_value: float


def convert_all(source_unit: str, value: float) -> list[ConversionResult]:
    validate(source_unit, value)
    meters = to_meters(source_unit, value)
    return [
        ConversionResult(unit, from_meters(unit, meters))
        for unit in SUPPORTED_UNITS
    ]


__all__ = ["ConversionResult", "ValidationError", "convert_all"]
