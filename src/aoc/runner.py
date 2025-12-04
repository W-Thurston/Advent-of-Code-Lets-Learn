import importlib
import sys
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types import ModuleType


def run(year: int, day: int) -> None:
    module: ModuleType = importlib.import_module(
        f"src.aoc{year}.solutions.day{day:02d}.solution"
    )
    data = module.parse(f"src/aoc{year}/solutions/day{day:02d}/input.txt")
    print("Part 1:", module.part1(data))
    print()
    print("Part 2:", module.part2(data))


# uv run python -m src.aoc.runner yyyy dd
if __name__ == "__main__":
    year = int(sys.argv[1])
    day = int(sys.argv[2])
    run(year, day)
