"""단위:값 문자열 파싱 (boundary)."""

from dataclasses import dataclass

from boundary.messages import INVALID_FORMAT, invalid_number


class ParseError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


@dataclass(frozen=True)
class ParsedInput:
    unit: str
    value: float


def parse(input_str: str) -> ParsedInput:
    if ":" not in input_str:
        raise ParseError(INVALID_FORMAT)

    unit, value_str = input_str.split(":", 1)

    try:
        value = float(value_str)
    except ValueError:
        raise ParseError(invalid_number(value_str)) from None

    return ParsedInput(unit=unit, value=value)
