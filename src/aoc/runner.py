import importlib
import sys
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types import ModuleType


def run(year: int, day: int, solution: str | None = None) -> None:
    """
    Run AoC solutions.

    Args:
        year: Year of the puzzle
        day: Day of the puzzle
        solution: Specific solution to run (initial/basic/optimized/elegant)
                 If None, runs comparison of all solutions

    """
    day_str: str = f"day{day:02d}"

    # Import utils for parsing
    utils: ModuleType = importlib.import_module(
        f"src.aoc{year}.solutions.{day_str}.utils",
    )
    data = utils.parse(f"src/aoc{year}/solutions/{day_str}/input.txt")

    if solution:
        # Run specific solution
        solution_module: ModuleType = importlib.import_module(
            f"src.aoc{year}.solutions.{day_str}.{solution}",
        )
        print(f"Running {solution} solution...")
        print(f"Part 1: {solution_module.part1(data)}")
        print(f"Part 2: {solution_module.part2(data)}")
    else:
        # Run comparison of all solutions
        comparison: ModuleType = importlib.import_module(
            f"src.aoc{year}.solutions.{day_str}.compare_solutions",
        )
        results = comparison.compare_solutions(data, runs=100)
        comparison.print_comparison(results)


# Usage: uv run python -m src.aoc.runner YYYY DD [solution]
# Examples:
#   uv run python -m src.aoc.runner 2025 1           # Compare all solutions
#   uv run python -m src.aoc.runner 2025 1 basic     # Run basic only
#   uv run python -m src.aoc.runner 2025 1 optimized # Run optimized only
if __name__ == "__main__":
    year = int(sys.argv[1])
    day = int(sys.argv[2])
    solution: str | None = sys.argv[3] if len(sys.argv) > 3 else None
    run(year, day, solution)
