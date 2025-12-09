"""
Advent of Code 2025 - Day 6: Trash Compactor.

Optimized solution:
Same behavior as the BASIC version, but with more efficient column handling,
faster splitting, and reduced branching inside loops.
"""

# =============================================================================
# SOLUTION 3: OPTIMIZED / EFFICIENT
# =============================================================================

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Generator


def multiply(values: list[int]) -> int:
    result = 1
    for v in values:
        result *= v
    return result


def part1(data: list[str]) -> int:
    """Optimized evaluation of column-wise problems."""
    if not data:
        return 0

    rows: list[list[str]] = [row.split() for row in data]
    operators: list[str] = rows[-1]
    num_cols: int = len(operators)
    num_rows: int = len(rows) - 1

    total = 0
    for col in range(num_cols):
        op: str = operators[col]
        # Extract integer values from column
        col_vals: list[int] = [int(rows[r][col]) for r in range(num_rows)]

        if op == "+":
            total += sum(col_vals)
        else:
            total += multiply(col_vals)

    return total


def part2(data: list[str]) -> int:
    """Optimized block-based parsing for reversed worksheet."""
    if not data:
        return 0

    # Reverse rows and pad
    max_width: int = max(len(line) for line in data) + 1
    rev: list[str] = [line[::-1].ljust(max_width) for line in data]

    h: int = len(rev)
    w: int = max_width

    total = 0
    current_block: list[str] = []

    def evaluate_block(block: list[str]) -> int:
        if not block:
            return 0
        has_plus: bool = any("+" in s for s in block)
        op_plus: bool = has_plus

        cleaned: Generator[str] = (s.replace("+", "").replace("*", "") for s in block)
        nums: list[int] = [int(x) for x in cleaned if x.strip()]

        return sum(nums) if op_plus else multiply(nums)

    for c in range(w):
        chars: list[str] = [rev[r][c] for r in range(h) if rev[r][c] != " "]

        if not chars:
            if current_block:
                total += evaluate_block(current_block)
                current_block = []
        else:
            current_block.append("".join(chars))

    if current_block:
        total += evaluate_block(current_block)

    return total


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
        data: list[str] = parse("src/aoc2025/solutions/day06/input.txt")
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
