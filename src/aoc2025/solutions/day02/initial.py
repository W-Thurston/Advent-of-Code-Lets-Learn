"""
Advent of Code 2025 - Day 2: Gift Shop.

My initial working solution - first draft before refactoring.
"""

import re


# =============================================================================
# SOLUTION 1: My Initial Solution
# =============================================================================
def part1(data: list[str]) -> int:
    """Sum all IDs that consist of a substring repeated exactly twice."""
    total = 0
    repeated_number_pattern = r"^(\d+)\1$"
    for product_range in data:
        bounds: list[str] = product_range.split("-")
        lower_bound: int = int(bounds[0])
        upper_bound: int = int(bounds[1]) + 1
        for product_id in range(lower_bound, upper_bound):
            matches: list[str] = re.findall(repeated_number_pattern, str(product_id))

            if matches:
                total += product_id

    return total


def part2(data: list[str]) -> int:
    """Sum all IDs that consist of a substring repeated >= 2 times."""
    total = 0
    repeated_number_pattern = r"^(\d+)\1+$"
    for product_range in data:
        bounds: list[str] = product_range.split("-")
        lower_bound: int = int(bounds[0])
        upper_bound: int = int(bounds[1]) + 1
        for product_id in range(lower_bound, upper_bound):
            matches: list[str] = re.findall(repeated_number_pattern, str(product_id))

            if matches:
                total += product_id

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
