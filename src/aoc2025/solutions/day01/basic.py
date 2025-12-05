"""
Advent of Code 2025 - Day 1: Secret Entrance.

Basic/Straightforward Solution - clear and readable approach.
"""


# =============================================================================
# SOLUTION 2: BASIC / STRAIGHTFORWARD
# =============================================================================
def part1(data: list[str]) -> int:
    """
    The "first instinct" solution - very explicit, no clever tricks.

    This is the most direct translation of the problem:
    - Start at 50
    - For each rotation, calculate new position
    - Count when we land on 0
    """
    position = 50
    count = 0

    for instruction in data:
        # Parse the instruction
        direction: str = instruction[0]  # First character is 'L' or 'R'
        distance = int(instruction[1:])  # Rest is the number

        # Move the dial
        if direction == "L":
            # Going left means subtracting
            position: int = position - distance
        elif direction == "R":
            # Going right means adding
            position = position + distance

        # Handle wrapping around the dial (0-99)
        while position < 0:
            position = position + 100
        while position >= 100:  # noqa: PLR2004
            position = position - 100

        # Check if we landed on 0
        if position == 0:
            count: int = count + 1

    return count


def part2(data: list[str]) -> int:
    """
    The "first instinct" solution for part 2 - simulate every single click.

    This might be slower, but it's crystal clear what's happening.
    """
    position = 50
    count = 0

    for instruction in data:
        direction: str = instruction[0]
        distance = int(instruction[1:])

        # Move one click at a time
        for _click_number in range(distance):
            # Move one position
            if direction == "L":
                position: int = position - 1
            elif direction == "R":
                position = position + 1

            # Wrap around if needed
            if position < 0:
                position = 99
            if position >= 100:  # noqa: PLR2004
                position = 0

            # Check if this click landed on 0
            if position == 0:
                count: int = count + 1

    return count


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
