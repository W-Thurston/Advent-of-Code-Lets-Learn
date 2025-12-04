"""
Advent of Code {year} — Day {day} (First Draft).

This file contains my initial working solution before refactoring.
"""  # noqa: INP001

from pathlib import Path


def parse(input_path: str | Path) -> list[str]:
    text: str = Path(input_path).read_text().strip()
    return text.splitlines()


def part1(data: list[str]) -> None:
    # TODO: first-draft logic
    pass


def part2(data: list[str]) -> None:
    # TODO: first-draft logic
    pass


if __name__ == "__main__":
    test_data_path: str = "../solutions/day{day:02d}/example.txt"
    data_path: str = "../solutions/day{day:02d}/input.txt"

    data: list[str] = parse(data_path)
    print("Part 1:", part1(data))
    print()
    print("Part 2:", part2(data))
