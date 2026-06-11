"""음수·미지원 단위 도메인 검증 (entity)."""

from entity.registry import SUPPORTED_UNITS


class ValidationError(Exception):
    pass


def validate(unit: str, value: float) -> None:
    if unit not in SUPPORTED_UNITS:
        raise ValidationError(f"Unknown unit: {unit}")
    if value < 0:
        raise ValidationError("Invalid value: negative numbers are not allowed")
