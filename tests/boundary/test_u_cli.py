"""boundary CLI — UI Track (U-*). Phase: GREEN."""

from boundary.cli import main
from boundary.messages import INVALID_FORMAT, PROMPT


def test_u020_prompts_with_prd_message(monkeypatch):
    """U-020 | REQ-IN-01 | PRD §4

    Track: UI (U-*)
    Layer: boundary
    검증: Insert value for converting (ex: meter:2.5):
    """
    prompts: list[str] = []

    def fake_input(message: str) -> str:
        prompts.append(message)
        return "meter:2.5"

    monkeypatch.setattr("builtins.input", fake_input)
    main()
    assert prompts == [PROMPT]


def test_u021_prints_three_lines_for_meter_input(capsys, monkeypatch):
    """U-021 | REQ-IN-01, REQ-OUT-01 | PRD §4 | SC-1

    Track: UI (U-*)
    Layer: boundary
    검증: meter:2.5 → 3줄 출력 (입력 단위 포함, PRD 예시 반올림)
    """
    monkeypatch.setattr("builtins.input", lambda _: "meter:2.5")
    main()
    output = capsys.readouterr().out.strip().splitlines()
    assert output == [
        "2.5 meter = 2.5 meter",
        "2.5 meter = 8.2 feet",
        "2.5 meter = 2.7 yard",
    ]


def test_u022_invalid_format_exits_without_conversion_output(capsys, monkeypatch):
    """U-022 | REQ-VAL-01 | PRD §4

    Track: UI (U-*)
    Layer: boundary
    검증: 형식 오류 → 오류 메시지 1줄, 변환 출력 없음
    """
    monkeypatch.setattr("builtins.input", lambda _: "meter2.5")
    main()
    output = capsys.readouterr().out.strip()
    assert output == INVALID_FORMAT
    assert "=" not in output
