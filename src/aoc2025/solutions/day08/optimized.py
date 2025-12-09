"""
Advent of Code 2025 - Day 8: Playground.

Optimized solution:
"""

# =============================================================================
# SOLUTION 3: OPTIMIZED / EFFICIENT
# =============================================================================


def parse_points(data: list[str]) -> list[tuple[int]]:
    pts: list[tuple[int]] = []
    for line in data:
        line: str = line.strip()  # noqa: PLW2901
        if not line:
            continue
        x, y, z = line.split(",")
        pts.append((int(x), int(y), int(z)))
    return pts


# ------------------- DSU helpers (procedural) ------------------- #
def dsu_find(parent: list[int], x: int) -> int:
    while parent[x] != x:
        parent[x] = parent[parent[x]]  # path compression
        x = parent[x]
    return x


def dsu_union(parent: list[int], size: list[int], a: int, b: int) -> bool:
    ra: int = dsu_find(parent, a)
    rb: int = dsu_find(parent, b)
    if ra == rb:
        return False
    if size[ra] < size[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    size[ra] += size[rb]
    return True


def compute_edges(points: list[tuple[int]]) -> list[tuple[int]]:
    """Squared distances; returns sorted list of (dist_sq, i, j)."""
    edges: list[tuple[int]] = []
    n: int = len(points)
    for i in range(n):
        x1, y1, z1 = points[i]
        for j in range(i + 1, n):
            x2, y2, z2 = points[j]
            dx: int = x1 - x2
            dy: int = y1 - y2
            dz: int = z1 - z2
            edges.append((dx * dx + dy * dy + dz * dz, i, j))
    edges.sort(key=lambda e: e[0])
    return edges


def part1(data: list[str], n_closest_edges: int = 1000) -> int:
    points: list[tuple[int]] = parse_points(data)
    n: int = len(points)
    if n == 0:
        return 0

    edges: list[tuple[int]] = compute_edges(points)
    parent: list[int] = list(range(n))
    size: list[int] = [1] * n

    # Apply first 1000 edges
    limit: int = min(n_closest_edges, len(edges))
    for k in range(limit):
        _, a, b = edges[k]
        dsu_union(parent, size, a, b)

    # Compute final component sizes
    comp_count: dict = {}
    for i in range(n):
        r: int = dsu_find(parent, i)
        comp_count[r] = comp_count.get(r, 0) + 1

    sizes: list = sorted(comp_count.values(), reverse=True)
    if not sizes:
        return 0

    prod = 1
    for s in sizes[:3]:
        prod *= s
    return prod


def part2(data: list[str]) -> int:
    points: list[tuple[int]] = parse_points(data)
    n: int = len(points)
    if n == 0:
        return 0
    if n == 1:
        x, _, _ = points[0]
        return x * x

    edges: list[tuple[int]] = compute_edges(points)
    parent: list[int] = list(range(n))
    size: list[int] = [1] * n
    components: int = n

    for _, a, b in edges:
        if dsu_union(parent, size, a, b):
            components -= 1
            if components == 1:
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
