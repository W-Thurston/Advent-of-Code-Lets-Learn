"""
Advent of Code 2025 - Day 4: Printing Department.

Alternative/Elegant Solution - OOP approach with proper abstractions.
- Clean, production-like structure using a Grid helper class.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable

# =============================================================================
# SOLUTION 4: ALTERNATIVE / ELEGANT
# =============================================================================

# 8 directions
D8: list[tuple[int, int]] = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]


@dataclass
class Grid:
    cells: list[list[str]]

    @property
    def h(self) -> int:
        return len(self.cells)

    @property
    def w(self) -> int:
        return len(self.cells[0])

    def neighbors8(self, r: int, c: int) -> Iterable[tuple[int, int]]:
        for dr, dc in D8:
            rr, cc = r + dr, c + dc
            if 0 <= rr < self.h and 0 <= cc < self.w:
                yield rr, cc

    def count_adj(self, r: int, c: int) -> int:
        return sum(1 for rr, cc in self.neighbors8(r, c) if self.cells[rr][cc] == "@")

    def all_coords(self):
        for r in range(self.h):
            for c in range(self.w):
                yield (r, c)

    def clone(self) -> Grid:
        return Grid([row[:] for row in self.cells])


def part1(data: list[str]) -> int:
    g = Grid([list(row.rstrip()) for row in data])
    adjacent_roll_threshold: int = 4

    count = 0
    for r, c in g.all_coords():
        if g.cells[r][c] == "@" and g.count_adj(r, c) < adjacent_roll_threshold:
            count += 1
    return count


def part2(data: list[str]) -> int:
    g = Grid([list(row.rstrip()) for row in data])
    adjacent_roll_threshold: int = 4

    # Precompute adjacency counts for all '@'
    adj: list[list[int]] = [[0] * g.w for _ in range(g.h)]
    for r, c in g.all_coords():
        if g.cells[r][c] == "@":
            adj[r][c] = g.count_adj(r, c)

    q: deque = deque()
    for r, c in g.all_coords():
        if g.cells[r][c] == "@" and adj[r][c] < adjacent_roll_threshold:
            q.append((r, c))

    removed = 0

    while q:
        r, c = q.popleft()
        if g.cells[r][c] != "@":
            continue

        g.cells[r][c] = "."
        removed += 1

        # Update neighbors
        for rr, cc in g.neighbors8(r, c):
            if g.cells[rr][cc] == "@":
                adj[rr][cc] -= 1
                if adj[rr][cc] < adjacent_roll_threshold:
                    q.append((rr, cc))

    return removed


# =============================================================================
# MAIN
# =============================================================================
if __name__ == "__main__":
    import time

    from src.aoc2025.solutions.day04.utils import parse

    # Example data
    example: list[str] = parse("src/aoc2025/solutions/day04/example.txt")
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
        data: list[str] = parse("src/aoc2025/solutions/day04/input.txt")
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
