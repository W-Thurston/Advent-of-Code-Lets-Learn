"""
Advent of Code 2025 - Day 3: Lobby.

Basic/Straightforward Solution - clear and readable approach.
- Part 1 brute-forces all (i < j) 2-digit combinations.
- Part 2 uses a simple greedy scanning approach for selecting a
  maximum-value length-12 subsequence.
"""


# =============================================================================
# SOLUTION 2: BASIC / STRAIGHTFORWARD
# =============================================================================


def best_two_digit(bank: str) -> int:
    """Brute-force the best 2-digit number."""
    digits: list[int] = [int(x) for x in bank.strip()]
    n: int = len(digits)
    best: int = 0
    for i in range(n):
        for j in range(i + 1, n):
            value: int = digits[i] * 10 + digits[j]
            best = max(best, value)
    return best


def best_k_digit(bank: str, k: int) -> int:
    """Greedy 'choose next largest digit in range' approach."""
    bank = bank.strip()
    n: int = len(bank)
    if k > n:
        raise ValueError("Bank has fewer than k digits.")

    remaining: int = k
    start = 0
    out: list[str] = []

    while remaining > 0:
        # Last possible start index such that enough digits remain
        last_pos: int = n - remaining

        best_digit = "0"
        best_index: int = start

        # Scan window
        for idx in range(start, last_pos + 1):
            d: str = bank[idx]
            if d > best_digit:
                best_digit: str = d
                best_index = idx
                if d == "9":  # can't do better
                    break

        out.append(best_digit)
        start: int = best_index + 1
        remaining -= 1

    return int("".join(out))


def part1(data: list[str]) -> int:
    total: int = 0
    for bank in data:
        bank: str = bank.strip()  # noqa: PLW2901
        if not bank:
            continue
        total += best_two_digit(bank)
    return total


def part2(data: list[str]) -> int:
    k: int = 12
    total: int = 0
    for bank in data:
        bank: str = bank.strip()  # noqa: PLW2901
        if not bank:
            continue
        total += best_k_digit(bank, k)
    return total


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
