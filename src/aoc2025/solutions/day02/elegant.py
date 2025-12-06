"""
Advent of Code 2025 - Day 2: Gift Shop.

Alternative/Elegant Solution
- Declarative style
- Clean helpers
- Expressive and easy to test
"""

from collections.abc import Iterable
from dataclasses import dataclass


# =============================================================================
# SOLUTION 4: ALTERNATIVE / ELEGANT
# =============================================================================
@dataclass(frozen=True)
class Range:
    """Represents a closed integer interval [lo, hi]."""

    lo: int
    hi: int

    def ids(self) -> Iterable[int]:
        """Yield all product IDs in this range."""
        return range(self.lo, self.hi + 1)


def parse_ranges(data: list[str]) -> list[Range]:
    """Convert pre-split range strings into Range objects."""
    return [Range(int(lo), int(hi)) for lo, hi in (part.split("-") for part in data)]


def repeated_exactly_twice(s: str) -> bool:
    """Return True if s = X + X."""
    n: int = len(s)
    if n % 2 != 0:
        return False
    half: int = n // 2
    return s[:half] == s[half:]


def repeated_at_least_twice(s: str) -> bool:
    """Return True if s = X repeated >= 2 times."""
    n: int = len(s)
    for size in range(1, n // 2 + 1):
        if n % size != 0:
            continue
        unit: str = s[:size]
        reps: int = n // size
        # Functional slicing check
        if all(s[i * size : (i + 1) * size] == unit for i in range(reps)):
            return True
    return False


def part1(data: list[str]) -> int:
    """Sum IDs with exactly-two repetition pattern."""
    ranges: list[Range] = parse_ranges(data)
    return sum(
        pid for r in ranges for pid in r.ids() if repeated_exactly_twice(str(pid))
    )


def part2(data: list[str]) -> int:
    """Sum IDs with repeated-at-least-twice pattern."""
    ranges: list[Range] = parse_ranges(data)
    return sum(
        pid for r in ranges for pid in r.ids() if repeated_at_least_twice(str(pid))
    )


# =============================================================================
# MAIN
# =============================================================================
if __name__ == "__main__":
    import time

    from src.aoc2025.solutions.day02.utils import parse

    # Example data
    example: list[str] = parse("src/aoc2025/solutions/day02/example.txt")
    print("Testing with example data:")
    try:
        # Time Part 1
        start: float = time.perf_counter()
        p1_answer: int = part1(example)
        p1_time: float = time.perf_counter() - start

        print(f"Part 1: {p1_answer: 12} ({p1_time * 1000:7.3f}ms)")
    except NameError as e:
        print(f"Warning: Solution 'Initial' missing required function: {e}")

    try:
        # Time Part 2
        start: float = time.perf_counter()
        p2_answer: int = part2(example)
        p2_time: float = time.perf_counter() - start

        print(f"Part 2: {p2_answer: 12} ({p2_time * 1000:7.3f}ms)")
    except NameError as e:
        print(f"Warning: Solution 'Initial' missing required function: {e}  - skipping")

    # Real data
    try:
        data: list[str] = parse("src/aoc2025/solutions/day02/input.txt")
        print("\n\nTesting with real puzzle input:")
        try:
            # Time Part 1
            start: float = time.perf_counter()
            p1_answer: int = part1(data)
            p1_time: float = time.perf_counter() - start

            print(f"Part 1: {p1_answer: 12} ({p1_time * 1000:7.3f}ms)")
        except NameError as e:
            print(f"Warning: Solution 'Initial' missing required function: {e}")

        try:
            # Time Part 2
            start: float = time.perf_counter()
            p2_answer: int = part2(data)
            p2_time: float = time.perf_counter() - start

            print(f"Part 2: {p2_answer: 12} ({p2_time * 1000:7.3f}ms)")
        except NameError as e:
            print(
                f"Warning: Solution 'Initial' missing required function: {e}  - skipping",
            )
    except FileNotFoundError:
        print("\n(Real puzzle input not found - skipping)")
