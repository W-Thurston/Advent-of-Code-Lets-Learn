"""
Advent of Code 2025 - Day 3: Lobby.

Alternative/Elegant Solution - OOP approach with proper abstractions.
This version focuses on clarity and maintainability:
- Separate modules for scanning and subsequence extraction.
- Descriptive helper names.
- Pure functions, easy to test individually.
"""


# =============================================================================
# SOLUTION 4: ALTERNATIVE / ELEGANT
# =============================================================================


def max_two_digit_subsequence(bank: str) -> int:
    """Return the max 2-digit subsequence (lexicographically largest pair)."""
    digits: list[int] = [int(d) for d in bank.strip()]
    n: int = len(digits)

    # best digit available to the right of each index
    best_right: list[int] = [0] * n
    best_right[-1] = digits[-1]
    for i in range(n - 2, -1, -1):
        best_right[i] = max(best_right[i + 1], digits[i + 1])

    best = 0
    for i in range(n - 1):
        candidate: int = digits[i] * 10 + best_right[i]
        best: int = max(best, candidate)
    return best


def max_k_subsequence(bank: str, k: int) -> int:
    """Monotonic stack extraction of maximum-length-k subsequence."""
    digits: str = bank.strip()
    n: int = len(digits)
    stack: list[str] = []
    drops: int = n - k

    for d in digits:
        while drops > 0 and stack and stack[-1] < d:
            stack.pop()
            drops -= 1
        stack.append(d)

    return int("".join(stack[:k]))


def part1(data: list[str]) -> int:
    return sum(max_two_digit_subsequence(line.strip()) for line in data if line.strip())


def part2(data: list[str]) -> int:
    return sum(max_k_subsequence(line.strip(), 12) for line in data if line.strip())


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
