"""
Advent of Code 2025 - Day 3: Lobby.

Utility file for this day's solutions.
"""

from pathlib import Path


def parse(input_path: str | Path) -> list[str]:
    text: str = Path(input_path).read_text().strip()
    return text.splitlines()
