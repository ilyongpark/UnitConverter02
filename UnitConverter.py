"""CLI 진입점 — boundary.cli.main() 위임."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from boundary.cli import main


if __name__ == "__main__":
    main()
