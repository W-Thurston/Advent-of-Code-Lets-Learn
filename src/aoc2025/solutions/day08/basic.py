"""
Advent of Code 2025 - Day 8: Playground.

Basic / Straightforward solution:
"""

import math

# =============================================================================
# SOLUTION 2: BASIC / STRAIGHTFORWARD
# =============================================================================


def parse_points(data: list[str]) -> list[tuple[int, int, int]]:
    pts: list[tuple[int, int, int]] = []
    for line in data:
        line: str = line.strip()  # noqa: PLW2901
        if not line:
            continue
        x, y, z = line.split(",")
        pts.append((int(x), int(y), int(z)))
    return pts


def euclid(p, q) -> float:
    """Full Euclidean distance (slow, but basic)."""
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2 + (p[2] - q[2]) ** 2)


def build_edges(points) -> list[tuple[int, int, int]]:
    """Brute-force all pairwise distances."""
    edges: list[tuple[int, int, int]] = []
    n: int = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            dist: float = euclid(points[i], points[j])
            edges.append((dist, i, j))
    edges.sort(key=lambda x: x[0])
    return edges


def build_components_bruteforce(n: int) -> list[set[int]]:
    """Represent components as a list of Python sets."""
    return [{i} for i in range(n)]


def merge_components(components, a, b) -> bool:
    """Given a, b, merge the two sets that contain them."""
    idx_a = idx_b = None
    for i, comp in enumerate(components):
        if a in comp:
            idx_a: int = i
        if b in comp:
            idx_b: int = i
    if idx_a is not None and idx_b is not None and idx_a != idx_b:
        components[idx_a] |= components[idx_b]
        components.pop(idx_b)
        return True
    return False


def part1(data: list[str], n_closest_edges: int = 1000) -> int:
    points: list[tuple[int, int, int]] = parse_points(data)
    n: int = len(points)
    if n == 0:
        return 0

    edges: list[tuple[int, int, int]] = build_edges(points)
    components: list[set[int]] = build_components_bruteforce(n)

    # Take first 1000 edges
    for _dist, a, b in edges[:n_closest_edges]:
        merge_components(components, a, b)

    # compute sizes
    sizes: list[int] = sorted([len(c) for c in components], reverse=True)
    if not sizes:
        return 0
    top3: list[int] = sizes[:3]
    prod = 1
    for s in top3:
        prod *= s
    return prod


def part2(data: list[str]) -> int:
    points: list[tuple[int, int, int]] = parse_points(data)
    n: int = len(points)
    if n == 0:
        return 0
    if n == 1:
        x, _, _ = points[0]
        return x * x

    edges: list[tuple[int, int, int]] = build_edges(points)
    components: list[set[int]] = build_components_bruteforce(n)

    for _dist, a, b in edges:
        merged: bool = merge_components(components, a, b)
        if merged and len(components) == 1:
            return points[a][0] * points[b][0]

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
        print(f"Warning: Solution 'Basic' missing required function: {e}")

    try:
        # Time Part 2
        start: float = time.perf_counter()
        p2_answer: int = part2(example)
        p2_time: float = time.perf_counter() - start

        print(f"Part 2: {p2_answer: 6} ({p2_time * 1000:7.3f}ms)")
    except NameError as e:
        print(f"Warning: Solution 'Basic' missing required function: {e}  - skipping")

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
