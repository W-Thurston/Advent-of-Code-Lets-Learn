"""
Advent of Code 2025 - Day 4: Printing Department.

Basic/Straightforward Solution - clear and readable approach.
- brute-force neighbor scanning and repeated grid updates.
"""


# =============================================================================
# SOLUTION 2: BASIC / STRAIGHTFORWARD
# =============================================================================

# 8 directions
D8: list[tuple[int, int]] = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]


def count_adjacent(grid: list[list[str]], r: int, c: int) -> int:
    """Count how many of the 8 neighbors are '@'."""
    h: int = len(grid)
    w: int = len(grid[0])
    cnt = 0
    for dr, dc in D8:
        rr, cc = r + dr, c + dc
        if 0 <= rr < h and 0 <= cc < w and grid[rr][cc] == "@":
            cnt += 1
    return cnt


def part1(data: list[str]) -> int:
    """Count rolls with <4 adjacent rolls."""
    grid: list[list[str]] = [list(row.rstrip()) for row in data]
    h: int = len(grid)
    w: int = len(grid[0])
    adjacent_roll_threshold: int = 4
    total = 0

    for r in range(h):
        for c in range(w):
            if (
                grid[r][c] == "@"
                and count_adjacent(grid, r, c) < adjacent_roll_threshold
            ):
                total += 1
    return total


def part2(data: list[str]) -> int:
    """
    Repeatedly remove all accessible rolls until no more are accessible.

    Return total number removed.
    """
    grid: list[list[str]] = [list(row.rstrip()) for row in data]
    h: int = len(grid)
    w: int = len(grid[0])
    adjacent_roll_threshold: int = 4
    removed_total = 0

    while True:
        to_remove: list[tuple[int, int]] = []

        for r in range(h):
            for c in range(w):
                if (
                    grid[r][c] == "@"
                    and count_adjacent(grid, r, c) < adjacent_roll_threshold
                ):
                    to_remove.append((r, c))

        if not to_remove:
            break

        removed_total += len(to_remove)
        for r, c in to_remove:
            grid[r][c] = "."  # remove it

    return removed_total


# =============================================================================
# MAIN
# =============================================================================
if __name__ == "__main__":
    import time

    from src.aoc2025.solutions.day04.utils import parse

    # Example data
    example: list[str] = parse("src/aoc2025/solutions/day04/example.txt")
    print("Testing with example data:")
    try:
        # Time Part 1
        start: float = time.perf_counter()
        p1_answer: int = part1(example)
        p1_time: float = time.perf_counter() - start

        print(f"Part 1: {p1_answer: 4} ({p1_time * 1000:7.3f}ms)")
    except NameError as e:
        print(f"Warning: Solution 'Initial' missing required function: {e}")

    try:
        # Time Part 2
        start: float = time.perf_counter()
        p2_answer: int = part2(example)
        p2_time: float = time.perf_counter() - start

        print(f"Part 2: {p2_answer: 4} ({p2_time * 1000:7.3f}ms)")
    except NameError as e:
        print(f"Warning: Solution 'Initial' missing required function: {e}  - skipping")

    # Real data
    try:
        data: list[str] = parse("src/aoc2025/solutions/day04/input.txt")
        print("\n\nTesting with real puzzle input:")
        try:
            # Time Part 1
            start: float = time.perf_counter()
            p1_answer: int = part1(data)
            p1_time: float = time.perf_counter() - start

            print(f"Part 1: {p1_answer: 4} ({p1_time * 1000:7.3f}ms)")
        except NameError as e:
            print(f"Warning: Solution 'Initial' missing required function: {e}")

        try:
            # Time Part 2
            start: float = time.perf_counter()
            p2_answer: int = part2(data)
            p2_time: float = time.perf_counter() - start

            print(f"Part 2: {p2_answer: 4} ({p2_time * 1000:7.3f}ms)")
        except NameError as e:
            print(
                f"Warning: Solution 'Initial' missing required function: {e}  - skipping",
            )
    except FileNotFoundError:
        print("\n(Real puzzle input not found - skipping)")
