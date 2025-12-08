"""
Advent of Code 2025 - Day 7: Laboratories.

Utility file for this day's solutions.
"""

from pathlib import Path


def parse(input_path: str | Path) -> list[str]:
    """Parse input file into list of rotation instructions."""
    text: str = Path(input_path).read_text().strip()
    return text.splitlines()
