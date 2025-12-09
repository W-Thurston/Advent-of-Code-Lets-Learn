"""
Advent of Code 2025 - Day 5: Cafeteria.

Optimized solution:
- Minimizes redundant comparisons
- Efficient interval merging
- Early-stopping membership check
"""

# =============================================================================
# SOLUTION 3: OPTIMIZED / EFFICIENT
# =============================================================================


def _parse_ranges_and_ids(data: list[str]) -> tuple[list[tuple[int, int]], list[int]]:
    """
    Parse the input into ranges and available IDs.

    Args:
        data: Raw puzzle input.

    Returns:
        A tuple of:
            - ranges: list of (lo, hi) pairs
            - available: list of ingredient IDs

    """
    blank: int = data.index("")

    ranges: list[tuple[int, ...]] = [
        tuple(map(int, line.split("-"))) for line in data[:blank]
    ]

    available: list[int] = [int(x) for x in data[blank + 1 :]]

    return ranges, available


def part1(data: list[str]) -> int:
    """
    Optimized membership check using sorted ranges and early stopping.

    Args:
        data: Raw puzzle input.

    Returns:
        Count of fresh available ingredient IDs.

    """
    ranges, available = _parse_ranges_and_ids(data)

    # Sort ranges upfront. This allows early stopping when lo > x.
    ranges.sort()

    fresh_count: int = 0

    for ingredient_id in available:
        for lo, hi in ranges:
            # If the current range begins past the ingredient,
            # no later range can possibly contain it.
            if lo > ingredient_id:
                break

            # Fresh if inside this interval.
            if lo <= ingredient_id <= hi:
                fresh_count += 1
                break

    return fresh_count


def part2(data: list[str]) -> int:
    """
    Optimized interval merging to compute total fresh ID count.

    Args:
        data: Raw puzzle input.

    Returns:
        The count of all IDs represented by the merged ranges.

    """
    blank: int = data.index("")
    ranges: list[tuple[int, ...]] = [
        tuple(map(int, line.split("-"))) for line in data[:blank]
    ]

    # Sort ranges by their starting value.
    ranges.sort()

    # Initialize with the first interval.
    merged_lo, merged_hi = ranges[0]
    total_ids = 0

    # Sweep all remaining intervals.
    for lo, hi in ranges[1:]:
        # If overlapping or adjacent, merge into the running interval.
        if lo <= merged_hi + 1:
            merged_hi: int = max(merged_hi, hi)
        else:
            # If disjoint, finalize the previous interval.
            total_ids += merged_hi - merged_lo + 1

            # Start a new merge window.
            merged_lo, merged_hi = lo, hi

    # Count final interval.
    total_ids += merged_hi - merged_lo + 1

    return total_ids


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
        print(f"Warning: Solution 'Initial' missing required function: {e}")

    try:
        # Time Part 2
        start: float = time.perf_counter()
        p2_answer: int = part2(example)
        p2_time: float = time.perf_counter() - start

        print(f"Part 2: {p2_answer:6} ({p2_time * 1000:7.3f}ms)")
    except NameError as e:
        print(f"Warning: Solution 'Initial' missing required function: {e}  - skipping")

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
