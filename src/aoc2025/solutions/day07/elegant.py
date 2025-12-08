"""
Advent of Code 2025 - Day 7: Laboratories.

Elegant / Pythonic solution:
- Declarative helpers
- Clean abstractions
- Robust and readable
"""

from dataclasses import dataclass

# =============================================================================
# SOLUTION 4: ALTERNATIVE / ELEGANT
# =============================================================================


@dataclass(frozen=True)
class Grid:
    cells: list[list[str]]

    @property
    def height(self) -> int:
        return len(self.cells)

    @property
    def width(self) -> int:
        return len(self.cells[0])

    def cell(self, row: int, col: int) -> str:
        return self.cells[row][col]

    @classmethod
    def from_lines(cls, lines: list[str]) -> "Grid":
        return cls([list(row) for row in lines])


def part1(data: list[str]) -> int:
    """Elegant version of classical beam splitting."""
    grid: Grid = Grid.from_lines(data)

    # Locate S
    start_col: int = grid.cells[0].index("S")
    active: set[int] = {start_col}

    split_count = 0

    for row in range(1, grid.height):
        next_active: set[int] = set()

        for col in active:
            cell: str = grid.cell(row, col)

            if cell == "^":
                # Split left & right safely
                if col - 1 >= 0:
                    next_active.add(col - 1)
                if col + 1 < grid.width:
                    next_active.add(col + 1)
                split_count += 1
            else:
                next_active.add(col)

        active = next_active

        if not active:
            break

    return split_count


def part2(data: list[str]) -> int:
    """Elegant Dynamic Programming formulation of timeline branching."""
    grid: Grid = Grid.from_lines(data)

    # Dynamic Programming arrays
    prev: list[int] = [0] * grid.width
    curr: list[int] = [0] * grid.width

    start_col: int = grid.cells[0].index("S")
    prev[start_col] = 1

    for row in range(1, grid.height):
        curr = [0] * grid.width
        for col, count in enumerate(prev):
            if count == 0:
                continue

            if grid.cell(row, col) == "^":
                # Split
                if col - 1 >= 0:
                    curr[col - 1] += count
                if col + 1 < grid.width:
                    curr[col + 1] += count
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
