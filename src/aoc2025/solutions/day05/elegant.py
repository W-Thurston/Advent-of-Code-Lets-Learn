"""
Advent of Code 2025 - Day 5: Cafeteria.

Elegant / Pythonic solution:
- Interval abstraction using @dataclass
- Clean overlap/merge semantics
- Clear functional merging pipeline
"""

from dataclasses import dataclass

# =============================================================================
# SOLUTION 4: ALTERNATIVE / ELEGANT
# =============================================================================


@dataclass(order=True)
class Interval:
    """Represents an inclusive integer interval [lo, hi]."""

    lo: int
    hi: int

    def overlaps(self, other: "Interval") -> bool:
        """
        Return True if this interval overlaps or touches the other.

        Overlap occurs if:
            this.lo <= other.hi + 1
        and
            other.lo <= this.hi + 1

        The +1 permits adjacent intervals to merge (e.g., 3-5 and 6-10).
        """
        return self.lo <= other.hi + 1 and other.lo <= self.hi + 1

    def merge(self, other: "Interval") -> "Interval":
        """Return the minimal interval covering both intervals."""
        return Interval(
            lo=min(self.lo, other.lo),
            hi=max(self.hi, other.hi),
        )

    def size(self) -> int:
        """Return the number of integers contained in this interval."""
        return self.hi - self.lo + 1


def _parse_intervals(data: list[str]) -> list[Interval]:
    """Extract interval objects from the first section of the input."""
    blank: int = data.index("")
    return [Interval(*map(int, line.split("-"))) for line in data[:blank]]


def part1(data: list[str]) -> int:
    """
    Count available ingredients that fall inside any fresh interval.

    Args:
        data: Raw puzzle input.

    Returns:
        Number of available ingredient IDs that are considered fresh.

    """
    blank: int = data.index("")
    intervals: list[Interval] = sorted(_parse_intervals(data))

    available_ids: map[int] = map(int, data[blank + 1 :])

    def is_fresh(x: int) -> bool:
        """Return True if x is contained in any interval."""
        for interval in intervals:
            # Early stop when interval starts beyond x.
            if interval.lo > x:
                return False
            if interval.lo <= x <= interval.hi:
                return True
        return False

    # Apply the freshness test to all available IDs.
    return sum(is_fresh(x) for x in available_ids)


def part2(data: list[str]) -> int:
    """
    Merge all intervals and return total coverage count.

    Args:
        data: Raw puzzle input.

    Returns:
        Count of all integers represented by the merged intervals.

    """
    intervals: list[Interval] = sorted(_parse_intervals(data))

    merged: list[Interval] = []

    # Sequential merge: combine overlapping or adjacent intervals.
    for iv in intervals:
        if not merged:
            merged.append(iv)
            continue

        last: Interval = merged[-1]

        if last.overlaps(iv):
            # Replace last with the merged interval.
            merged[-1] = last.merge(iv)
        else:
            # Disjoint interval — append separately.
            merged.append(iv)

    # Sum the size of each merged interval.
    return sum(iv.size() for iv in merged)


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
