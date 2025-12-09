"""
Advent of Code 2025 - Day 4: Printing Department.

Optimized/Efficient Solution - mathematical approach for performance.
- Efficient peeling using a queue of potentially-accessible cells.
"""

from collections import deque

# =============================================================================
# SOLUTION 3: OPTIMIZED / EFFICIENT
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


def compute_initial_counts(grid: list[list[str]]) -> list[list[int]]:
    """Precompute adjacency counts for all cells."""
    h: int = len(grid)
    w: int = len(grid[0])
    adj: list[list[int]] = [[0] * w for _ in range(h)]
    for r in range(h):
        for c in range(w):
            if grid[r][c] == "@":
                cnt = 0
                for dr, dc in D8:
                    rr, cc = r + dr, c + dc
                    if 0 <= rr < h and 0 <= cc < w and grid[rr][cc] == "@":
                        cnt += 1
                adj[r][c] = cnt
    return adj


def part1(data: list[str]) -> int:
    grid: list[list[str]] = [list(row.rstrip()) for row in data]
    adj: list[list[int]] = compute_initial_counts(grid)

    adjacent_roll_threshold: int = 4

    total = 0
    h: int = len(grid)
    w: int = len(grid[0])
    for r in range(h):
        for c in range(w):
            if grid[r][c] == "@" and adj[r][c] < adjacent_roll_threshold:
                total += 1
    return total


def part2(data: list[str]) -> int:
    """
    Use a queue to peel off accessible rolls.

    Each time a roll is removed, update adjacency counts of neighbors.
    If any neighbor now becomes accessible, enqueue it.
    """
    grid: list[list[str]] = [list(row.rstrip()) for row in data]
    h: int = len(grid)
    w: int = len(grid[0])

    adjacent_roll_threshold: int = 4

    adj: list[list[int]] = compute_initial_counts(grid)
    q: deque[tuple[int, int]] = deque()

    # Initialize queue with all accessible rolls
    for r in range(h):
        for c in range(w):
            if grid[r][c] == "@" and adj[r][c] < adjacent_roll_threshold:
                q.append((r, c))

    removed = 0

    while q:
        r, c = q.popleft()
        if grid[r][c] != "@":
            continue  # might already be removed

        # Remove this roll
        grid[r][c] = "."
        removed += 1

        # Update adjacency of neighbors
        for dr, dc in D8:
            rr, cc = r + dr, c + dc
            if 0 <= rr < h and 0 <= cc < w and grid[rr][cc] == "@":
                adj[rr][cc] -= 1
                if adj[rr][cc] < adjacent_roll_threshold:
                    q.append((rr, cc))

    return removed


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
