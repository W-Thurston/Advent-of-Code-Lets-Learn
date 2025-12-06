"""
Advent of Code 2025 - Day 1: Secret Entrance.

Utility file for this day's solutions.
"""

from pathlib import Path


def parse(input_path: str | Path) -> list[str]:
    raw_data: str = Path(input_path).read_text().strip()
    text: list[str] = raw_data.split(",")
    return text
