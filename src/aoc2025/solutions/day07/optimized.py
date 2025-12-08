"""
Advent of Code 2025 - Day 7: Laboratories.

Optimized solution:
- Efficient beam propagation
- Precomputed splitter map for faster branching
- Minimal allocations inside loops
"""

# =============================================================================
# SOLUTION 3: OPTIMIZED / EFFICIENT
# =============================================================================


def _parse_grid(data: list[str]) -> list[list[str]]:
    """Convert input strings to character grid."""
    return [list(row) for row in data]


def part1(data: list[str]) -> int:
    """Fast classical beam simulation with robust boundary handling."""
    grid: list[list[str]] = _parse_grid(data)
    height: int = len(grid)
    width: int = len(grid[0])

    # Precompute splitter locations per row to reduce indexing.
    splitters_per_row: list[set[int]] = [
        {col for col, ch in enumerate(row) if ch == "^"} for row in grid
    ]

    # Starting beam
    start_col: int = grid[0].index("S")
    beam_cols: set[int] = {start_col}

    split_count = 0

    for row in range(1, height):
        new_beam_cols: set[int] = set()
        splitters: set[int] = splitters_per_row[row]

        for col in beam_cols:
            if col in splitters:
                # Split left/right
                if col - 1 >= 0:
                    new_beam_cols.add(col - 1)
                if col + 1 < width:
                    new_beam_cols.add(col + 1)
                split_count += 1
            else:
                new_beam_cols.add(col)

        if not new_beam_cols:
            break

        beam_cols = new_beam_cols

    return split_count


def part2(data: list[str]) -> int:
    """Fast Dynamic Programming for quantum many-worlds timeline splitting."""
    grid: list[list[str]] = _parse_grid(data)
    height: int = len(grid)
    width: int = len(grid[0])

    # Dynamic Programming rows reused in a rolling fashion (memory efficient)
    prev: list[int] = [0] * width
    curr: list[int] = [0] * width

    # Start at S
    start_col: int = grid[0].index("S")
    prev[start_col] = 1

    for row in range(1, height):
        curr = [0] * width  # reset fast

        # Use direct indexing for speed
        grid_row: list[str] = grid[row]

        for col, count in enumerate(prev):
            if count == 0:
                continue

            if grid_row[col] == "^":
                # Split timelines
                left: int = col - 1
                right: int = col + 1

                if left >= 0:
                    curr[left] += count
                if right < width:
                    curr[right] += count

            else:
                curr[col] += count

        prev = curr

    return sum(prev)


# =============================================================================
# MAIN
# =============================================================================
if __name__ == "__main__":
    import time

    from src.aoc2025.solutions.day07.utils import parse

    # Example data
    example: list[str] = parse("src/aoc2025/solutions/day07/example.txt")
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
        data: list[str] = parse("src/aoc2025/solutions/day07/input.txt")
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
