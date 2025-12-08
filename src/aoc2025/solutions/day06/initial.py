"""
Advent of Code 2025 - Day 6: Trash Compactor.

My initial working solution - first draft before refactoring.
"""

import math


# =============================================================================
# SOLUTION 1: My Initial Solution
# =============================================================================
def part1(data: list[str]) -> int:
    # Example data had 4 rows, puzzle input had 5
    operations_row: int = len(data) - 1

    split_values: list[list[str]] = [x.split() for x in data]

    grand_total = 0
    for col in range(len(split_values[0])):
        if split_values[operations_row][col] == "+":
            column_total: int = 0
            for row in range(operations_row):
                column_total += int(split_values[row][col])

        elif split_values[operations_row][col] == "*":
            column_total = 1
            for row in range(operations_row):
                column_total *= int(split_values[row][col])

        else:
            print(f"Some other Value: {split_values[operations_row][col]}")

        grand_total += column_total

    return grand_total


def part2(data: list[str]) -> int:
    verbose: bool = False

    split_values: list[str] = [x[::-1].ljust(len(data[0]) + 1) for x in data]

    if verbose:
        for i in split_values:
            print(i.replace(" ", "-"))

    column_total: int = 0
    arithmetic_list: list = []
    for col in range(len(split_values[0])):
        col_values: list[str] = [row[col] for row in split_values if row[col] != " "]
        if verbose:
            print(col_values)

        if not col_values:
            if verbose:
                print(arithmetic_list)
            if "+" in arithmetic_list[0] or "+" in arithmetic_list[-2]:
                arithmetic_list[0] = arithmetic_list[0].replace("+", "")
                arithmetic_list[-2] = arithmetic_list[-2].replace("+", "")
                arithmetic_list = [int(x) for x in arithmetic_list]
                column_total += sum(arithmetic_list)
                if verbose:
                    for idx in range(len(arithmetic_list)):
                        print(f"{arithmetic_list[idx]} +", end="")
                    print(f"= {sum(arithmetic_list)}")

            elif "*" in arithmetic_list[0] or "*" in arithmetic_list[-2]:
                arithmetic_list[0] = arithmetic_list[0].replace("*", "")
                arithmetic_list[-2] = arithmetic_list[-2].replace("*", "")
                arithmetic_list = [int(x) for x in arithmetic_list]
                column_total += math.prod(arithmetic_list)
                if verbose:
                    for idx in range(len(arithmetic_list)):
                        print(f"{arithmetic_list[idx]} * ", end="")
                    print(f"= {math.prod(arithmetic_list)}")

            arithmetic_list = []
            if verbose:
                print()
        else:
            arithmetic_list.append("".join(col_values))

    return column_total


# =============================================================================
# MAIN
# =============================================================================
if __name__ == "__main__":
    import time

    from src.aoc2025.solutions.day06.utils import parse

    # Example data
    example: list[str] = parse("src/aoc2025/solutions/day06/example.txt")
    print("Testing with example data:")
    try:
        # Time Part 1
        start: float = time.perf_counter()
        p1_answer: int = part1(example)
        p1_time: float = time.perf_counter() - start

        print(f"Part 1: {p1_answer: 8} ({p1_time * 1000:7.3f}ms)")
    except NameError as e:
        print(f"Warning: Solution 'Initial' missing required function: {e}")

    try:
        # Time Part 2
        start: float = time.perf_counter()
        p2_answer: int = part2(example)
        p2_time: float = time.perf_counter() - start

        print(f"Part 2: {p2_answer: 8} ({p2_time * 1000:7.3f}ms)")
    except NameError as e:
        print(f"Warning: Solution 'Initial' missing required function: {e}  - skipping")

    # Real data
    try:
        data: list[str] = parse("src/aoc2025/solutions/day06/input.txt")
        print("\n\nTesting with real puzzle input:")
        try:
            # Time Part 1
            start: float = time.perf_counter()
            p1_answer: int = part1(data)
            p1_time: float = time.perf_counter() - start

            print(f"Part 1: {p1_answer: 15} ({p1_time * 1000:7.3f}ms)")
        except NameError as e:
            print(f"Warning: Solution 'Initial' missing required function: {e}")

        try:
            # Time Part 2
            start: float = time.perf_counter()
            p2_answer: int = part2(data)
            p2_time: float = time.perf_counter() - start

            print(f"Part 2: {p2_answer: 15} ({p2_time * 1000:7.3f}ms)")
        except NameError as e:
            print(
                f"Warning: Solution 'Initial' missing required function: {e}  - skipping",
            )
    except FileNotFoundError:
        print("\n(Real puzzle input not found - skipping)")
