"""
Advent of Code {year} — Day {day}.

Final Refactored Solution
"""  # noqa: INP001

from pathlib import Path


def parse(path: str | Path) -> list[str]:
    return Path(path).read_text().strip().splitlines()


def solve_part1(data: list[str]) -> None:
    """Explain your refined approach."""


def solve_part2(data: list[str]) -> None:
    """Explain improvements over part 1."""


if __name__ == "__main__":
    data: list[str] = parse("input.txt")
    print("Part 1:", solve_part1(data))
    print("Part 2:", solve_part2(data))
