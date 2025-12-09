"""
Advent of Code 2025 - Day 8: Playground.

Elegant / Pythonic solution:
"""

from dataclasses import dataclass


# =============================================================================
# SOLUTION 4: ALTERNATIVE / ELEGANT
# =============================================================================
@dataclass(frozen=True)
class Point3D:
    x: int
    y: int
    z: int


class DSU:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.size = [1] * n
        self.components = n

    def find(self, x: int) -> int:
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> bool:
        ra: int = self.find(a)
        rb: int = self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        self.components -= 1
        return True

    def component_sizes(self) -> list[int]:
        counts: dict = {}
        for i in range(len(self.parent)):
            r: int = self.find(i)
            counts[r] = counts.get(r, 0) + 1
        return list(counts.values())


def parse_points(data: list[str]) -> list[Point3D]:
    pts: list[Point3D] = []
    for line in data:
        line: str = line.strip()  # noqa: PLW2901
        if not line:
            continue
        x, y, z = line.split(",")
        pts.append(Point3D(int(x), int(y), int(z)))
    return pts


def sorted_edges(points: list[Point3D]) -> list[tuple[int]]:
    edges: list[tuple[int]] = []
    n: int = len(points)
    for i in range(n):
        p1: Point3D = points[i]
        for j in range(i + 1, n):
            p2: Point3D = points[j]
            dx: int = p1.x - p2.x
            dy: int = p1.y - p2.y
            dz: int = p1.z - p2.z
            dist_sq: int = dx * dx + dy * dy + dz * dz
            edges.append((dist_sq, i, j))
    edges.sort(key=lambda e: e[0])
    return edges


def part1(data: list[str], n_closest_edges: int = 1000) -> int:
    points: list[Point3D] = parse_points(data)
    n: int = len(points)
    if n == 0:
        return 0

    edges: list[tuple[int]] = sorted_edges(points)
    dsu = DSU(n)

    for _dist_sq, a, b in edges[: min(n_closest_edges, len(edges))]:
        dsu.union(a, b)

    sizes: list[int] = sorted(dsu.component_sizes(), reverse=True)
    if not sizes:
        return 0

    prod = 1
    for s in sizes[:3]:
        prod *= s
    return prod


def part2(data: list[str]) -> int:
    points: list[Point3D] = parse_points(data)
    n: int = len(points)
    if n == 0:
        return 0
    if n == 1:
        return points[0].x * points[0].x

    edges: list[tuple[int]] = sorted_edges(points)
    dsu = DSU(n)

    for _dist_sq, a, b in edges:
        if dsu.union(a, b) and dsu.components == 1:
            return points[a].x * points[b].x

    return 0


# =============================================================================
# MAIN
# =============================================================================
if __name__ == "__main__":
    import time

    from src.aoc2025.solutions.day08.utils import parse

    # Example data
    example: list[str] = parse("src/aoc2025/solutions/day08/example.txt")
    print("Testing with example data:")
    try:
        # Time Part 1
        start: float = time.perf_counter()
        p1_answer: int = part1(example)
        p1_time: float = time.perf_counter() - start

        print(f"Part 1: {p1_answer: 6} ({p1_time * 1000:7.3f}ms)")
    except NameError as e:
        print(f"Warning: Solution 'Initial' missing required function: {e}")

    try:
        # Time Part 2
        start: float = time.perf_counter()
        p2_answer: int = part2(example)
        p2_time: float = time.perf_counter() - start

        print(f"Part 2: {p2_answer: 6} ({p2_time * 1000:7.3f}ms)")
    except NameError as e:
        print(f"Warning: Solution 'Initial' missing required function: {e}  - skipping")

    # Real data
    try:
        data: list[str] = parse("src/aoc2025/solutions/day08/input.txt")
        print("\n\nTesting with real puzzle input:")
        try:
            # Time Part 1
            start: float = time.perf_counter()
            p1_answer: int = part1(data)
            p1_time: float = time.perf_counter() - start

            print(f"Part 1: {p1_answer: 11} ({p1_time * 1000:7.3f}ms)")
        except NameError as e:
            print(f"Warning: Solution 'Initial' missing required function: {e}")

        try:
            # Time Part 2
            start: float = time.perf_counter()
            p2_answer: int = part2(data)
            p2_time: float = time.perf_counter() - start

            print(f"Part 2: {p2_answer: 11} ({p2_time * 1000:7.3f}ms)")
        except NameError as e:
            print(
                f"Warning: Solution 'Initial' missing required function: {e}  - skipping",
            )
    except FileNotFoundError:
        print("\n(Real puzzle input not found - skipping)")
