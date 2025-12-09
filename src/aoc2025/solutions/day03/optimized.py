"""
Advent of Code 2025 - Day 3: Lobby.

Optimized/Efficient Solution - mathematical approach for performance.
- Part 1: O(n) scan for best 2-digit using tracking of max-from-right.
- Part 2: Uses the monotonic stack algorithm to select the maximum
  lexicographic subsequence of length 12 in O(n).

This approach is extremely fast even on very large inputs.
"""


# =============================================================================
# SOLUTION 3: OPTIMIZED / EFFICIENT
# =============================================================================


def best_two_digit(bank: str) -> int:
    """O(n) method for best 2-digit subsequence."""
    digits: list[int] = [int(d) for d in bank.strip()]
    n: int = len(digits)

    # Precompute best digit to the right of each index.
    max_right: list[int] = [0] * n
    max_right[-1] = digits[-1]
    for i in range(n - 2, -1, -1):
        max_right[i] = max(digits[i + 1], max_right[i + 1])

    best = 0
    for i in range(n - 1):
        value: int = digits[i] * 10 + max_right[i]
        best: int = max(best, value)
    return best


def best_k_digit(bank: str, k: int) -> int:
    """Return the lexicographically largest subsequence of length k, using the monotonic decreasing stack technique."""
    digits: str = bank.strip()
    n: int = len(digits)

    drops_allowed: int = n - k
    stack: list[str] = []

    for d in digits:
        while drops_allowed > 0 and stack and stack[-1] < d:
            stack.pop()
            drops_allowed -= 1
        stack.append(d)

    # Truncate if needed (in case we didn't drop enough)
    result: str = "".join(stack[:k])
    return int(result)


def part1(data: list[str]) -> int:
    return sum(best_two_digit(line.strip()) for line in data if line.strip())


def part2(data: list[str]) -> int:
    k = 12
    return sum(best_k_digit(line.strip(), k) for line in data if line.strip())


# =============================================================================
# MAIN
# =============================================================================
if __name__ == "__main__":
    import time

    from src.aoc2025.solutions.day03.utils import parse

    # Example data
    example: list[str] = parse("src/aoc2025/solutions/day03/example.txt")
    print("Testing with example data:")
    try:
        # Time Part 1
        start: float = time.perf_counter()
        p1_answer: int = part1(example)
        p1_time: float = time.perf_counter() - start

        print(f"Part 1: {p1_answer: 14} ({p1_time * 1000:7.3f}ms)")
    except NameError as e:
        print(f"Warning: Solution 'Initial' missing required function: {e}")

    try:
        # Time Part 2
        start: float = time.perf_counter()
        p2_answer: int = part2(example)
        p2_time: float = time.perf_counter() - start

        print(f"Part 2: {p2_answer: 14} ({p2_time * 1000:7.3f}ms)")
    except NameError as e:
        print(f"Warning: Solution 'Initial' missing required function: {e}  - skipping")

    # Real data
    try:
        data: list[str] = parse("src/aoc2025/solutions/day03/input.txt")
        print("\n\nTesting with real puzzle input:")
        try:
            # Time Part 1
            start: float = time.perf_counter()
            p1_answer: int = part1(data)
            p1_time: float = time.perf_counter() - start

            print(f"Part 1: {p1_answer: 16} ({p1_time * 1000:7.3f}ms)")
        except NameError as e:
            print(f"Warning: Solution 'Initial' missing required function: {e}")

        try:
            # Time Part 2
            start: float = time.perf_counter()
            p2_answer: int = part2(data)
            p2_time: float = time.perf_counter() - start

            print(f"Part 2: {p2_answer: 16} ({p2_time * 1000:7.3f}ms)")
        except NameError as e:
            print(
                f"Warning: Solution 'Initial' missing required function: {e}  - skipping",
            )
    except FileNotFoundError:
        print("\n(Real puzzle input not found - skipping)")
