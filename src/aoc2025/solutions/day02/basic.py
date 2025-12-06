"""
Advent of Code 2025 - Day 2: Gift Shop.

Basic / Straightforward Solution
- Clear substring-repeat checking
- Direct numeric iteration
- No optimizations beyond readability
"""


# =============================================================================
# SOLUTION 2: BASIC / STRAIGHTFORWARD
# =============================================================================
def _parse_ranges(data: list[str]) -> list[tuple[int, int]]:
    """
    Parse already-split 'lo-hi' range strings into integer tuples.

    The input parser splits by comma, so each element of `data` is exactly:
        "123-456"
    """
    ranges: list[tuple[int, int]] = []
    for part in data:
        lo_str, hi_str = part.split("-")
        ranges.append((int(lo_str), int(hi_str)))
    return ranges


def _is_repeated_exactly_twice(s: str) -> bool:
    """
    Return True if `s` consists of exactly two identical substrings.

    Examples:
        "55"      -> True
        "6464"    -> True   (64 twice)
        "123123"  -> True
        "111"     -> False  (cannot split evenly)

    """
    n: int = len(s)
    if n % 2 != 0:  # Must divide cleanly into 2 halves
        return False
    half: int = n // 2
    return s[:half] == s[half:]


def _is_repeated_at_least_twice(s: str) -> bool:
    """
    Return True if `s` is X repeated >= 2 times.

    We test all possible substring sizes `size` where size divides len(s).

    Examples:
        "1212"        -> True  ("12" x 2)
        "123123123"   -> True  ("123" x 3)
        "1111111"     -> True  ("1" x 7)
        "1234"        -> False

    """
    n: int = len(s)

    for size in range(1, n // 2 + 1):
        if n % size != 0:
            continue  # Substring cannot tile evenly

        unit: str = s[:size]
        repeats: int = n // size

        # Build or check slices instead of regex
        if all(s[i * size : (i + 1) * size] == unit for i in range(repeats)):
            return True

    return False


def part1(data: list[str]) -> int:
    """Sum all product IDs consisting of a substring repeated *exactly twice*."""
    ranges: list[tuple[int, int]] = _parse_ranges(data)
    total = 0

    for lo, hi in ranges:
        for pid in range(lo, hi + 1):
            if _is_repeated_exactly_twice(str(pid)):
                total += pid

    return total


def part2(data: list[str]) -> int:
    """Sum all product IDs consisting of a substring repeated *>= 2* times."""
    ranges: list[tuple[int, int]] = _parse_ranges(data)
    total = 0

    for lo, hi in ranges:
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
