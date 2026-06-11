"""PRD 출력 한 줄 포맷 (boundary)."""

from entity.rounding import round_display


def format_line(
    source_unit: str,
    source_value: float,
    target_unit: str,
    target_raw_value: float,
) -> str:
    converted = round_display(target_raw_value)
    return f"{source_value} {source_unit} = {converted} {target_unit}"
