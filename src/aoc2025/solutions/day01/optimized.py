"""
Advent of Code 2025 - Day 1: Secret Entrance.

Optimized/Efficient Solution - mathematical approach for performance.
"""


# =============================================================================
# SOLUTION 3: OPTIMIZED / EFFICIENT
# =============================================================================
def part1(data: list[str]) -> int:
    """
    Optimized version using single-pass calculation.

    Optimization: Use ternary operator and eliminate intermediate variables.
    Time: O(n), Space: O(1) where n = number of rotations
    """
    position = 50
    zero_count = 0

    for rotation in data:
        position: int = (
            position + (-1 if rotation[0] == "L" else 1) * int(rotation[1:])
        ) % 100
        zero_count += position == 0

    return zero_count


def part2(data: list[str]) -> int:
    """
    Optimized version using mathematical calculation instead of simulation.

    Key optimization: Instead of simulating each click, calculate how many
    times we cross 0 mathematically.

    Going RIGHT from position P by distance D:
    - We cross 0 at positions: 100, 200, 300, ...
    - Number of crossings = (P + D) // 100

    Going LEFT from position P by distance D:
    - We cross 0 going backwards at: P, P+100, P+200, ... steps
    - If P == 0: crossings at 100, 200, ... → D // 100
    - If P > 0 and D >= P: crossings = (D - P) // 100 + 1
    - Otherwise: 0 crossings

    Time: O(n) but with much better constant factor - no inner loop!
    Space: O(1)
    """
    position = 50
    zero_count = 0

    for rotation in data:
        direction: str = rotation[0]
        distance = int(rotation[1:])

        if direction == "R":
            # Going right: count crossings through 0
            zero_count += (position + distance) // 100
            position: int = (position + distance) % 100
        else:  # direction == 'L'
            # Going left: count crossings through 0
            if position == 0:
                # Starting at 0, don't count it, cross at 100, 200, ...
                zero_count += distance // 100
            elif distance >= position:
                # Will cross at least once
                zero_count += (distance - position) // 100 + 1
            # else: distance < position, no crossings

            position = (position - distance) % 100

    return zero_count


# =============================================================================
# MAIN
# =============================================================================
if __name__ == "__main__":
    import time

    from src.aoc2025.solutions.day01.utils import parse

    # Example data
    example: list[str] = parse("src/aoc2025/solutions/day01/example.txt")
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
        data: list[str] = parse("src/aoc2025/solutions/day01/input.txt")
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
