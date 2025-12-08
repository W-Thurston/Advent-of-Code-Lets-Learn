"""
Advent of Code 2025 - Day 1: Secret Entrance.

Comparison framework for evaluating different solution approaches.
"""

import importlib
import time
from dataclasses import dataclass
from pathlib import Path
from types import ModuleType


# =============================================================================
# COMPARISON FRAMEWORK
# =============================================================================
@dataclass
class SolutionResult:
    """Results from running a solution."""

    name: str
    part1_answer: int | None
    part1_time: float | None
    part2_answer: int | None
    part2_time: float | None
    error: str | None = None

    def __str__(self) -> str:
        if self.error:
            return f"{self.name:20} | ❌ {self.error}"

        p1_str: str = (
            f"{self.part1_answer:5}" if self.part1_answer is not None else "  N/A"
        )
        p1_time_str: str = (
            f"{self.part1_time * 1000:7.3f}ms"
            if self.part1_time is not None
            else "    N/A"
        )
        p2_str: str = (
            f"{self.part2_answer:5}" if self.part2_answer is not None else "  N/A"
        )
        p2_time_str: str = (
            f"{self.part2_time * 1000:7.3f}ms"
            if self.part2_time is not None
            else "    N/A"
        )

        return (
            f"{self.name:20} | "
            f"Part 1: {p1_str} ({p1_time_str}) | "
            f"Part 2: {p2_str} ({p2_time_str})"
        )


def load_solution(solution_name: str, year: int = 2025, day: int = 1) -> ModuleType:
    """
    Dynamically load a solution module.

    Args:
        solution_name: Name of solution file (e.g., 'initial', 'basic')
        year: Year of the puzzle
        day: Day of the puzzle

    Returns:
        Module object with part1 and part2 functions

    """
    module_path: str = f"src.aoc{year}.solutions.day{day:02d}.{solution_name}"
    return importlib.import_module(module_path)


def compare_solutions(
    data: list[str],
    solutions: list[str] | None = None,
    runs: int = 100,
) -> list[SolutionResult]:
    """
    Compare multiple solutions for correctness and performance.

    Args:
        data: Parsed puzzle input
        solutions: List of solution names to compare (defaults to all)
        runs: Number of times to run each solution for timing

    Returns:
        List of SolutionResult objects with timing data

    """
    if solutions is None:
        solutions = ["initial", "basic", "optimized", "elegant"]

    results: list[SolutionResult] = []

    for solution_name in solutions:
        try:
            # Load the solution module
            module: ModuleType = load_solution(solution_name)

            # Time Part 1
            start: float = time.perf_counter()
            for _ in range(runs):
                p1_answer = module.part1(data)
            p1_time: float = (time.perf_counter() - start) / runs

            # Time Part 2
            start = time.perf_counter()
            for _ in range(runs):
                p2_answer = module.part2(data)
            p2_time: float = (time.perf_counter() - start) / runs

            results.append(
                SolutionResult(
                    name=solution_name.capitalize(),
                    part1_answer=p1_answer,
                    part1_time=p1_time,
                    part2_answer=p2_answer,
                    part2_time=p2_time,
                ),
            )
        except (ImportError, AttributeError) as e:
            # Solution not implemented yet
            results.append(
                SolutionResult(
                    name=solution_name.capitalize(),
                    part1_answer=None,
                    part1_time=None,
                    part2_answer=None,
                    part2_time=None,
                    error=f"Not implemented ({type(e).__name__})",
                ),
            )

    return results


def print_comparison(results: list[SolutionResult]) -> None:
    """Pretty print the comparison results."""
    line_length = 80
    print("\n" + "=" * line_length)
    print("SOLUTION COMPARISON")
    print("=" * line_length)

    for result in results:
        print(result)

    print("=" * line_length)

    # Filter out failed solutions for comparison
    valid_results: list[SolutionResult] = [r for r in results if r.error is None]

    if len(valid_results) == 0:
        print("❌ No solutions successfully ran")
        return

    # Verify all valid solutions agree
    if len(valid_results) > 1:
        answers_match: bool = all(
            r.part1_answer == valid_results[0].part1_answer
            and r.part2_answer == valid_results[0].part2_answer
            for r in valid_results
        )

        if answers_match:
            print("✅ All solutions produce identical answers")
        else:
            print("❌ WARNING: Solutions produce different answers!")

    # Find fastest (only among valid results)
    if valid_results:
        fastest_p1: SolutionResult = min(valid_results, key=lambda r: r.part1_time)
        fastest_p2: SolutionResult = min(valid_results, key=lambda r: r.part2_time)

        print(f"\n🏆 Fastest Part 1: {fastest_p1.name}")
        print(f"🏆 Fastest Part 2: {fastest_p2.name}")


# =============================================================================
# MAIN
# =============================================================================
if __name__ == "__main__":
    from src.aoc2025.solutions.day01.utils import parse

    # Example data
    example: list[str] = parse("src/aoc2025/solutions/day01/example.txt")
    print("Testing with example data:")
    results: list[SolutionResult] = compare_solutions(example, runs=1000)
    print_comparison(results)

    # Real data
    try:
        data: list[str] = parse("src/aoc2025/solutions/day01/input.txt")
        print("\n\nTesting with real puzzle input:")
        results = compare_solutions(data, runs=100)
        print_comparison(results)
    except FileNotFoundError:
        print("\n(Real puzzle input not found - skipping)")
