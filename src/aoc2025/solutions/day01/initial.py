"""
Advent of Code 2025 - Day 1: Secret Entrance.

My initial working solution - first draft before refactoring.
"""

from typing import Literal

# from tqdm import tqdm


# =============================================================================
# SOLUTION 1: My Initial Solution
# =============================================================================
def part1(data: list[str]) -> int:
    """Count times dial lands on 0 after rotations."""
    padding: int = max([len(x) for x in data])

    verbose: bool = False

    zero_counter: int = 0
    dial_location: int = 50

    if verbose:
        print(f"The dial starts by pointing at {dial_location}")

    # I used tqdm to track the iterations.
    # I am commenting it out for sake of comparing the solutions
    # for rotation in tqdm(data, desc="Rotations"):
    for rotation in data:
        step: Literal[-1, 1] = -1 if rotation[0] == "L" else 1
        amount = int(rotation[1:])
        dial_location: int = (dial_location + step * amount) % 100
        if dial_location == 0:
            zero_counter += 1

        if verbose:
            print(
                f"- The dial is rotated {rotation:<{padding}} to point at {dial_location:<2} [ZERO COUNTER: {zero_counter}].",
            )

    return zero_counter


def part2(data: list[str]) -> int:
    """Count times dial passes through 0 during rotations."""
    padding: int = max([len(x) for x in data])

    verbose: bool = False

    zero_counter: int = 0
    dial_location: int = 50

    if verbose:
        print(f"The dial starts by pointing at {dial_location}")

    # I used tqdm to track the iterations.
    # I am commenting it out for sake of comparing the solutions
    # for rotation in tqdm(data, desc="Rotations"):
    for rotation in data:
        zeros_this_rotation = 0
        step: Literal[-1, 1] = -1 if rotation[0] == "L" else 1
        amount: int = int(rotation[1:])
        for _click in range(amount):
            dial_location = (dial_location + step) % 100
            if dial_location == 0:
                zeros_this_rotation += 1
        zero_counter += zeros_this_rotation
        if verbose:
            print(
                f"- The dial is rotated {rotation:<{padding}} to point at {dial_location:<2} [ZERO COUNTER: {zero_counter}]",
                end="",
            )
            if zeros_this_rotation > 0 and dial_location != 0:
                print(
                    f"; during this rotation, it points at 0 {zeros_this_rotation} time(s).",
                )
            elif dial_location == 0:
                print("; Dial is left pointing to 0.")
            else:
                print(".")

    return zero_counter


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
