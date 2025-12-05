"""
Advent of Code 2025 - Day 1: Secret Entrance.

Alternative/Elegant Solution - OOP approach with proper abstractions.
"""

from typing import Literal


# =============================================================================
# SOLUTION 4: ALTERNATIVE / ELEGANT
# =============================================================================
class SafeDial:
    """
    Object-oriented approach treating the dial as a stateful object.

    This solution demonstrates:
    - Encapsulation of dial behavior
    - Iterator protocol for click-by-click traversal
    - Property-based design
    - More testable and reusable code
    """

    def __init__(self, start_position: int = 50, modulo: int = 100) -> None:
        self._position = start_position
        self._modulo = modulo
        self._zero_crossings = 0

    @property
    def position(self) -> int:
        """Current dial position."""
        return self._position

    @property
    def zero_crossings(self) -> int:
        """Total number of times dial has crossed 0."""
        return self._zero_crossings

    def rotate(self, instruction: str, *, count_final_only: bool = True) -> None:
        """
        Rotate the dial according to instruction.

        Args:
            instruction: String like "L68" or "R48"
            count_final_only: If True, only count if we end on 0.
                              If False, count every pass through 0.

        """
        direction: str = instruction[0]
        distance = int(instruction[1:])
        step: Literal[-1, 1] = -1 if direction == "L" else 1

        if count_final_only:
            # Just jump to final position
            self._position = (self._position + step * distance) % self._modulo
            if self._position == 0:
                self._zero_crossings += 1
        else:
            # Count every click
            for _ in range(distance):
                self._position = (self._position + step) % self._modulo
                if self._position == 0:
                    self._zero_crossings += 1

    def reset(self, position: int = 50) -> None:
        """Reset the dial to a new position."""
        self._position = position
        self._zero_crossings = 0


def part1(data: list[str]) -> int:
    """Solution using the SafeDial class."""
    dial = SafeDial(start_position=50)
    for rotation in data:
        dial.rotate(rotation, count_final_only=True)
    return dial.zero_crossings


def part2(data: list[str]) -> int:
    """Solution using the SafeDial class with full click tracking."""
    dial = SafeDial(start_position=50)
    for rotation in data:
        dial.rotate(rotation, count_final_only=False)
    return dial.zero_crossings


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
