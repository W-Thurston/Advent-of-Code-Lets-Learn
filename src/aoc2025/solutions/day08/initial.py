"""
Advent of Code 2025 - Day 8: Playground.

My initial working solution - first draft before refactoring.
"""

from math import dist

# =============================================================================
# SOLUTION 1: My Initial Solution
# =============================================================================


def find_circuit(circuits, point) -> None | int:
    for idx, c in enumerate(circuits):
        if point in c:
            return idx
    return None


def part1(data: list[str], n_closest_edges: int = 1000) -> int:
    # Parse the points
    points: list[tuple[int]] = []
    for line in data:
        x, y, z = map(int, line.split(","))
        points.append((x, y, z))

    # Compute all pairwise distances
    pairs: list[tuple[int]] = []
    n: int = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            d: float = dist(points[i], points[j])
            pairs.append((d, i, j))  # Store indices to avoid duplication

    # Sort by distance
    pairs.sort(key=lambda x: x[0])

    # Represent circuits as "sets of points"
    circuits: list[set[int]] = [{i} for i in range(n)]  # initially N circuits

    # Process the N closest edges
    edge_count: int = 0
    idx: int = 0
    while edge_count < n_closest_edges:
        d, a, b = pairs[idx]
        idx += 1

        ca: int | None = find_circuit(circuits, a)
        cb: int | None = find_circuit(circuits, b)

        if ca != cb:
            # Merge circuits
            circuits[ca].update(circuits[cb])
            circuits.pop(cb)
        # else: they're already connected -> skip

        edge_count += 1

    # Compute answer
    sizes: list[int] = sorted((len(c) for c in circuits), reverse=True)
    answer: int = sizes[0] * sizes[1] * sizes[2]

    return answer


def part2(data: list[str]) -> int:
    # Parse the points
    points: list[tuple[int]] = []
    for line in data:
        x, y, z = map(int, line.split(","))
        points.append((x, y, z))

    # Compute all pairwise distances
    pairs: list[tuple[int]] = []
    n: int = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            d: float = dist(points[i], points[j])
            pairs.append((d, i, j))  # Store indices to avoid duplication

    # Sort by distance
    pairs.sort(key=lambda x: x[0])

    # Represent circuits as "sets of points"
    circuits: list[set[int]] = [{i} for i in range(n)]  # initially N circuits

    for _d, a, b in pairs:
        ca: int | None = find_circuit(circuits, a)
        cb: int | None = find_circuit(circuits, b)

        if ca != cb:
            # Merge circuits
            circuits[ca].update(circuits[cb])
            circuits.pop(cb)

            # If only one circuit remains:
            if len(circuits) == 1:
                # Final connection is a <-> b
                ax, _ay, _az = points[a]
                bx, _by, _bz = points[b]
                return ax * bx
    return None


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
        p1_answer: int = part1(example, n_closest_edges=10)
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
            p1_answer: int = part1(data, n_closest_edges=1000)
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
