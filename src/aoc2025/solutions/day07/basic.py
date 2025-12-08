"""
Advent of Code 2025 - Day 7: Laboratories.

Basic / Straightforward solution:
- Clean beam simulation (Part 1)
- Simple dynamic-programming timeline accumulation (Part 2)
- Robust boundary checking
"""


# =============================================================================
# SOLUTION 2: BASIC / STRAIGHTFORWARD
# =============================================================================


def _parse_grid(data: list[str]) -> list[list[str]]:
    """Convert list of raw strings into grid of characters."""
    return [list(row) for row in data]


def part1(data: list[str]) -> int:
    """
    Simulate classical tachyon beams.

    A single beam begins at the 'S' position and travels downward.
    Rules:
      - Empty cell '.' → continue downward.
      - Splitter '^'  → beam stops; two new beams spawn left/right.
      - Beams that move off-grid are discarded.
      - If multiple beams enter the same cell, deduplicate.

    Returns:
        Total number of times a splitter is encountered.

    """
    grid: list[list[str]] = _parse_grid(data)
    height: int = len(grid)
    width: int = len(grid[0])

    # Find starting column in top row.
    start_col: int = grid[0].index("S")

    # set-based tracking of active beam columns in current row.
    beam_cols: set[int] = {start_col}

    split_count = 0

    # Process row by row, starting below the 'S'.
    for row in range(1, height):
        new_beam_cols: set[int] = set()

        for col in beam_cols:
            cell: str = grid[row][col]

            if cell == "^":
                # Beam splits: spawn left and right beams (if in-bounds).
                left: int = col - 1
                right: int = col + 1

                if 0 <= left < width:
                    new_beam_cols.add(left)
                if 0 <= right < width:
                    new_beam_cols.add(right)

                split_count += 1

            else:
                # Empty space: beam continues downward.
                new_beam_cols.add(col)

        beam_cols = new_beam_cols

        if not beam_cols:  # All beams vanished early
            break

    return split_count


def part2(data: list[str]) -> int:
    """
    Simulate quantum tachyon manifold with many-worlds splitting.

    Each *timeline* follows all possible branches.
    Timeline counts accumulate in a Dynamic Programming manner:
        timeline_grid[row][col] = number of timelines arriving at that cell.

    At splitters:
        timelines split left and right.
    Off-grid branches are discarded.

    Returns:
        Total number of timelines reaching the bottom row.

    """
    grid: list[list[str]] = _parse_grid(data)
    height: int = len(grid)
    width: int = len(grid[0])

    # Dynamic Programming grid: integer counts of timelines at each position.
    timeline_grid: list[list[int]] = [[0] * width for _ in range(height)]

    # Start at 'S' with exactly one timeline.
    start_col: int = grid[0].index("S")
    timeline_grid[0][start_col] = 1

    # Fill timeline_grid row by row.
    for row in range(1, height):
        prev_row: list[int] = timeline_grid[row - 1]
        curr_row: list[int] = timeline_grid[row]

        for col, count in enumerate(prev_row):
            if count == 0:
                continue

            cell: str = grid[row][col]

            if cell == "^":
                # Split timelines left and right
                left: int = col - 1
                right: int = col + 1

                if 0 <= left < width:
                    curr_row[left] += count
                if 0 <= right < width:
                    curr_row[right] += count

            else:
                # Continue downward
                curr_row[col] += count

    return sum(timeline_grid[-1])


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
        print(f"Warning: Solution 'Basic' missing required function: {e}")

    try:
        # Time Part 2
        start: float = time.perf_counter()
        p2_answer: int = part2(example)
        p2_time: float = time.perf_counter() - start

        print(f"Part 2: {p2_answer: 4} ({p2_time * 1000:7.3f}ms)")
    except NameError as e:
        print(f"Warning: Solution 'Basic' missing required function: {e}  - skipping")

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
