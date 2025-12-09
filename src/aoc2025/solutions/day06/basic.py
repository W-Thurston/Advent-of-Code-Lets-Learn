"""
Advent of Code 2025 - Day 6: Trash Compactor.

Basic / Straightforward solution:
- Literal, clear parsing with minimal cleverness.
"""


# =============================================================================
# SOLUTION 2: BASIC / STRAIGHTFORWARD
# =============================================================================


def safe_int(value: str) -> int:
    """Convert a string to int safely after stripping spaces."""
    return int(value.strip()) if value.strip() else 0


def multiply(values: list[int]) -> int:
    """Multiply a list of integers."""
    result = 1
    for v in values:
        result *= v
    return result


def part1(data: list[str]) -> int:
    """
    Evaluate each column as its own arithmetic problem.

    Each line is split on whitespace, producing parallel columns of numbers.
    The final row contains "+" or "*" for each column.

    Returns:
        Sum of solved column-wise problems.

    """
    # Convert each line into list of tokens
    split_rows: list[list[str]] = [row.split() for row in data]
    if not split_rows:
        return 0

    num_rows: int = len(split_rows)
    num_cols: int = len(split_rows[0])

    total = 0

    # Last row holds operators
    operators: list[str] = split_rows[-1]

    # Each column forms an independent arithmetic problem
    for col in range(num_cols):
        col_values: list[int] = [
            safe_int(split_rows[r][col]) for r in range(num_rows - 1)
        ]
        op: str = operators[col]

        if op == "+":
            total += sum(col_values)
        else:
            total += multiply(col_values)

    return total


def part2(data: list[str]) -> int:
    """
    Reverse each row, pad to equal width, then read column-wise.

    Columns form "blocks" separated by empty columns. A block consists of
    multiple column strings. Operators '+' or '*' appear embedded inside the
    strings, typically the first or second-to-last entry.

    Returns:
        Total sum of block evaluations.

    """
    if not data:
        return 0

    # Reverse each line and pad to uniform width
    max_width: int = max(len(line) for line in data) + 1
    reversed_rows: list[str] = [line[::-1].ljust(max_width) for line in data]

    # Build columns (list of vertical strings)
    num_rows: int = len(reversed_rows)
    num_cols: int = max_width
    block_strings: list[str] = []
    result_total = 0

    def process_block(block: list[str]) -> int:
        """Evaluate a completed block of column-strings."""
        if not block:
            return 0

        # Determine operator
        has_plus: bool = any("+" in s for s in block)
        op: str = "+" if has_plus else "*"

        cleaned: list[str] = [s.replace("+", "").replace("*", "") for s in block]
        nums: list[int] = [int(st) for st in cleaned if st.strip()]

        return sum(nums) if op == "+" else multiply(nums)

    # Extract each column
    for c in range(num_cols):
        col_chars: list = []
        for r in range(num_rows):
            ch: str = reversed_rows[r][c]
            if ch != " ":
                col_chars.append(ch)

        if not col_chars:
            # Empty column → block boundary
            if block_strings:
                result_total += process_block(block_strings)
                block_strings = []
        else:
            block_strings.append("".join(col_chars))

    # Last block
    if block_strings:
        result_total += process_block(block_strings)

    return result_total


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
        print(f"Warning: Solution 'Basic' missing required function: {e}")

    try:
        # Time Part 2
        start: float = time.perf_counter()
        p2_answer: int = part2(example)
        p2_time: float = time.perf_counter() - start

        print(f"Part 2: {p2_answer:6} ({p2_time * 1000:7.3f}ms)")
    except NameError as e:
        print(f"Warning: Solution 'Basic' missing required function: {e}  - skipping")

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
