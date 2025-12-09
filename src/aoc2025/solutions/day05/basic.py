"""
Advent of Code 2025 - Day 5: Cafeteria.

Basic / Straightforward solution:
- Clear, explicit parsing
- Direct membership checking
- Simple interval merging
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Generator

# =============================================================================
# SOLUTION 2: BASIC / STRAIGHTFORWARD
# =============================================================================


def part1(data: list[str]) -> int:
    """
    Return number of available ingredient IDs that are fresh.

    Args:
        data: Raw puzzle input, containing:
            - A block of "lo-hi" inclusive ranges
            - A blank line
            - A block of ingredient IDs to test

    Returns:
        Count of available IDs that fall inside **any** fresh range.

    """
    # Find the empty line that separates the two sections of input.
    blank_index: int = data.index("")

    # Parse the range lines into list of (lo, hi) integer tuples.
    ranges: list[tuple[int, int]] = [
        tuple(map(int, line.split("-"))) for line in data[:blank_index]
    ]

    # Parse the available ingredient IDs after the blank line.
    available_ids: Generator[int] = (int(x) for x in data[blank_index + 1 :])

    fresh_count = 0

    # For each ingredient ID, check whether it falls into ANY of the ranges.
    for ingredient_id in available_ids:
        for lo, hi in ranges:
            # If inside this range, the ingredient is fresh.
            if lo <= ingredient_id <= hi:
                fresh_count += 1
                break  # No need to check further ranges.

    return fresh_count


def part2(data: list[str]) -> int:
    """
    Return total count of all IDs considered fresh by the ranges alone.

    Part 2 ignores the available ingredient list entirely; instead, it
    merges overlapping ranges and sums the lengths of each merged interval.

    Args:
        data: Raw puzzle input.

    Returns:
        Total number of unique integer IDs described by the ranges.

    """
    blank_index: int = data.index("")

    # Convert ranges into sortable integer pairs.
    ranges: list[tuple[int, int]] = [
        tuple(map(int, line.split("-"))) for line in data[:blank_index]
    ]

    # Sort ranges in ascending order (required for merging).
    ranges.sort()

    merged: list[list[int]] = []  # stores intervals as [lo, hi]

    # Merge overlapping or adjacent ranges.
    for lo, hi in ranges:
        if not merged:
            merged.append([lo, hi])
            continue

        _last_lo, last_hi = merged[-1]

        # If current range touches or overlaps the last merged range:
        if lo <= last_hi + 1:
            # Expand the last range's upper bound if needed.
            merged[-1][1] = max(last_hi, hi)
        else:
            # Otherwise, start a new disjoint interval.
            merged.append([lo, hi])

    # After merging, count total IDs inside each interval.
    total: int = sum((hi - lo + 1) for lo, hi in merged)

    return total


# =============================================================================
# MAIN
# =============================================================================
if __name__ == "__main__":
    import time

    from src.aoc2025.solutions.day05.utils import parse

    # Example data
    example: list[str] = parse("src/aoc2025/solutions/day05/example.txt")
    print("Testing with example data:")
    try:
        # Time Part 1
        start: float = time.perf_counter()
        p1_answer: int = part1(example)
        p1_time: float = time.perf_counter() - start

        print(f"Part 1: {p1_answer:6} ({p1_time * 1000:7.3f}ms)")
    except NameError as e:
        print(f"Warning: Solution 'Basic' missing required function: {e}")

    try:
        # Time Part 2
        start: float = time.perf_counter()
        p2_answer: int = part2(example)
        p2_time: float = time.perf_counter() - start

        print(f"Part 2: {p2_answer:6} ({p2_time * 1000:7.3f}ms)")
    except NameError as e:
        print(f"Warning: Solution 'Basic' missing required function: {e}  - skipping")

    # Real data
    try:
        data: list[str] = parse("src/aoc2025/solutions/day05/input.txt")
        print("\n\nTesting with real puzzle input:")
        try:
            # Time Part 1
            start: float = time.perf_counter()
            p1_answer: int = part1(data)
            p1_time: float = time.perf_counter() - start

            print(f"Part 1: {p1_answer:6} ({p1_time * 1000:7.3f}ms)")
        except NameError as e:
            print(f"Warning: Solution 'Initial' missing required function: {e}")

        try:
            # Time Part 2
            start: float = time.perf_counter()
            p2_answer: int = part2(data)
            p2_time: float = time.perf_counter() - start

            print(f"Part 2: {p2_answer:6} ({p2_time * 1000:7.3f}ms)")
        except NameError as e:
            print(
                f"Warning: Solution 'Initial' missing required function: {e}  - skipping",
            )
    except FileNotFoundError:
        print("\n(Real puzzle input not found - skipping)")
