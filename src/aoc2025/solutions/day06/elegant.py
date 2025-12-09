"""
Advent of Code 2025 - Day 6: Trash Compactor.

Elegant / Pythonic solution:
Production-grade structure with small abstractions
while preserving your exact puzzle logic.
"""


# =============================================================================
# SOLUTION 4: ALTERNATIVE / ELEGANT
# =============================================================================

from dataclasses import dataclass


def multiply(values: list[int]) -> int:
    result = 1
    for v in values:
        result *= v
    return result


@dataclass
class Worksheet:
    """Represents a rectangular reversed worksheet (for Part 2)."""

    rows: list[str]

    @classmethod
    def from_reversed(cls, original: list[str]) -> "Worksheet":
        max_width: int = max(len(line) for line in original) + 1
        padded: list[str] = [line[::-1].ljust(max_width) for line in original]
        return cls(padded)

    @property
    def h(self) -> int:
        return len(self.rows)

    @property
    def w(self) -> int:
        return len(self.rows[0])

    def column(self, c: int) -> list[str]:
        """Return vertical list of non-space characters from column c."""
        return [self.rows[r][c] for r in range(self.h) if self.rows[r][c] != " "]


@dataclass
class Block:
    """A contiguous block of column strings representing one problem."""

    columns: list[str]

    def evaluate(self) -> int:
        """Return the numeric result of this block."""
        if not self.columns:
            return 0

        has_plus: bool = any("+" in col for col in self.columns)
        cleaned: list[str] = [
            col.replace("+", "").replace("*", "") for col in self.columns
        ]
        nums: list[int] = [int(x) for x in cleaned if x.strip()]

        return sum(nums) if has_plus else multiply(nums)


def part1(data: list[str]) -> int:
    """Elegant structured implementation of Part 1."""
    if not data:
        return 0

    rows: list[list[str]] = [r.split() for r in data]
    operators: list[str] = rows[-1]
    num_cols: int = len(operators)

    total = 0
    for c in range(num_cols):
        op: str = operators[c]
        nums: list[int] = [int(rows[r][c]) for r in range(len(rows) - 1)]
        total += sum(nums) if op == "+" else multiply(nums)

    return total


def part2(data: list[str]) -> int:
    """Elegant structured implementation of Part 2."""
    if not data:
        return 0

    ws: Worksheet = Worksheet.from_reversed(data)

    current_block: list[str] = []
    total = 0

    for c in range(ws.w):
        col_chars: list[str] = ws.column(c)

        if not col_chars:
            if current_block:
                total += Block(current_block).evaluate()
                current_block = []
        else:
            current_block.append("".join(col_chars))

    # Last block
    if current_block:
        total += Block(current_block).evaluate()

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
