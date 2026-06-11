"""출력용 소수 1자리 반올림 (entity)."""

from decimal import ROUND_HALF_UP, Decimal


def round_display(value: float) -> float:
    """소수 1자리 round half up."""
    return float(Decimal(str(value)).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP))
