"""CLI 진입점·stdin/stdout (boundary)."""

from boundary.formatter import format_line
from boundary.messages import PROMPT
from boundary.parser import ParseError, parse
from control.convert_use_case import ValidationError, convert_all


def main() -> None:
    input_str = input(PROMPT)

    try:
        parsed = parse(input_str)
        results = convert_all(parsed.unit, parsed.value)
    except ParseError as exc:
        print(exc.message)
        return
    except ValidationError as exc:
        print(str(exc))
        return

    for result in results:
        print(
            format_line(
                parsed.unit,
                parsed.value,
                result.target_unit,
                result.raw_value,
            )
        )
