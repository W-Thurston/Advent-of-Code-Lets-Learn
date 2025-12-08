"""
Advent of Code 2025 - Day 3: Lobby.

My initial working solution - first draft before refactoring.
"""


# =============================================================================
# SOLUTION 1: My Initial Solution
# =============================================================================


def find_largest_subsequence(s: str, n: int) -> int:
    """
    Find the largest n-digit subsequence using a greddy algorithm.

    Strategy: At each step, pick the largest digit that still leaves enough digits
    remaining to complete the subsequence.

    Args:
        s (str): Starting string of integers
        n (int): Length of the required subsequence

    Returns:
        int: n-digit subsequence

    """
    if n > len(s) or n <= 0:
        return None

    result: list[str] = []
    start_search: int = 0

    for i in range(n):
        # How many more digits do we need after this one?
        remaining_needed: int = n - i - 1

        # Latest position we can pick a digit from
        # (must leave enough digits for the rest)
        latest_position: int = len(s) - remaining_needed - 1

        # Find the maximum digit in the valid range
        max_digit: str = "0"
        max_position: int = start_search
        for j in range(start_search, latest_position + 1):
            if s[j] > max_digit:
                max_digit = s[j]
                max_position = j

        # Add this digit to the result
        result.append(max_digit)

        # Next search starts after this position
        start_search = max_position + 1

    return int("".join(result))


def part1(data: list[str]) -> int:
    total_output_joltage: int = 0

    for battery_bank in data:
        total_output_joltage += find_largest_subsequence(battery_bank, 2)

    return total_output_joltage


def part2(data: list[str]) -> int:
    total_output_joltage: int = 0

    for battery_bank in data:
        total_output_joltage += find_largest_subsequence(battery_bank, 12)

    return total_output_joltage


# =============================================================================
# MAIN
# =============================================================================
if __name__ == "__main__":
    import time

    from src.aoc2025.solutions.day03.utils import parse

    # Example data
    example: list[str] = parse("src/aoc2025/solutions/day03/example.txt")
    print("Testing with example data:")
    try:
        # Time Part 1
        start: float = time.perf_counter()
        p1_answer: int = part1(example)
        p1_time: float = time.perf_counter() - start

        print(f"Part 1: {p1_answer: 16} ({p1_time * 1000:7.3f}ms)")
    except NameError as e:
        print(f"Warning: Solution 'Initial' missing required function: {e}")

    try:
        # Time Part 2
        start: float = time.perf_counter()
        p2_answer: int = part2(example)
        p2_time: float = time.perf_counter() - start

        print(f"Part 2: {p2_answer: 16} ({p2_time * 1000:7.3f}ms)")
    except NameError as e:
        print(f"Warning: Solution 'Initial' missing required function: {e}  - skipping")

    # Real data
    try:
        data: list[str] = parse("src/aoc2025/solutions/day03/input.txt")
        print("\n\nTesting with real puzzle input:")
        try:
            # Time Part 1
            start: float = time.perf_counter()
            p1_answer: int = part1(data)
            p1_time: float = time.perf_counter() - start

            print(f"Part 1: {p1_answer: 16} ({p1_time * 1000:7.3f}ms)")
        except NameError as e:
            print(f"Warning: Solution 'Initial' missing required function: {e}")

        try:
            # Time Part 2
            start: float = time.perf_counter()
            p2_answer: int = part2(data)
            p2_time: float = time.perf_counter() - start

            print(f"Part 2: {p2_answer: 16} ({p2_time * 1000:7.3f}ms)")
        except NameError as e:
            print(
                f"Warning: Solution 'Initial' missing required function: {e}  - skipping",
            )
    except FileNotFoundError:
        print("\n(Real puzzle input not found - skipping)")
