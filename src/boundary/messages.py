"""오류 메시지 상수 (boundary)."""

PROMPT = "Insert value for converting (ex: meter:2.5): "
INVALID_FORMAT = "Invalid format. Use unit:value (ex: meter:2.5)"


def invalid_number(value_str: str) -> str:
    return f"Invalid number: {value_str}"
