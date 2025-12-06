"""
Advent of Code 2025 - Day 2: Gift Shop.

Optimized/Efficient Solution
- Efficient divisor-based repeated-pattern detection
- Minimal repeated slicing
- Fast for large numeric ranges
"""


# =============================================================================
# SOLUTION 3: OPTIMIZED / EFFICIENT
# =============================================================================
def _parse_ranges(data: list[str]) -> list[tuple[int, int]]:
    """Parse comma-split 'lo-hi' strings into integer tuples."""
    return [tuple(map(int, part.split("-"))) for part in data]


def _is_repeated_exactly_twice(s: str) -> bool:
    """Optimized check for exact two-block repetition."""
    n: int = len(s)
    if n % 2 != 0:
        return False
    half: int = n // 2
    # Compare string halves once
    return s[:half] == s[half:]


def _is_repeated_at_least_twice(s: str) -> bool:
    """
    Optimized check for substring repeated >= 2 times.

    Key optimization:
        - Only substring lengths that divide len(s) are tested.
        - Stops as soon as a match is found.
        - Avoids constructing large intermediary strings.
    """
    n: int = len(s)
    # Test substring sizes that divide n
    for size in range(1, (n // 2) + 1):
        if n % size != 0:
            continue

        unit: str = s[:size]
        # Instead of full tile reconstruction: slice-check repeated blocks
        okay = True
        for i in range(1, n // size):
            if s[i * size : (i + 1) * size] != unit:
                okay = False
                break
        if okay:
            return True

    return False


def part1(data: list[str]) -> int:
    """Sum IDs consisting of exactly two identical halves."""
    total: int = 0
    for lo, hi in _parse_ranges(data):
        for pid in range(lo, hi + 1):
            if _is_repeated_exactly_twice(str(pid)):
                total += pid
    return total


def part2(data: list[str]) -> int:
    """Sum IDs consisting of a substring repeated >= 2 times."""
    total: int = 0
    for lo, hi in _parse_ranges(data):
        for pid in range(lo, hi + 1):
            if _is_repeated_at_least_twice(str(pid)):
                total += pid
    return total


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
