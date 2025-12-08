"""
Advent of Code 2025 - Day 5: Cafeteria.

My initial working solution - first draft before refactoring.
"""


# =============================================================================
# SOLUTION 1: My Initial Solution
# =============================================================================
def part1(data: list[str]) -> int:
    # Split data into fresh ingredient ID ranges and available ingredient IDs
    newline_idx: int = data.index("")
    fresh_ingredient_id_ranges: list[tuple[int, int]] = [
        (int(parts[0]), int(parts[1]))
        for x in data[:newline_idx]
        if (parts := x.split("-"))
    ]
    available_ingredients_ids: list[int] = [int(x) for x in data[newline_idx + 1 :]]

    available_ingredient_id_counter = 0
    for available_ingredient_id in available_ingredients_ids:
        for lower_bound, upper_bound in fresh_ingredient_id_ranges:
            if lower_bound <= available_ingredient_id <= upper_bound:
                available_ingredient_id_counter += 1
                break  # Possible to be in multiple ranges

    return available_ingredient_id_counter


def part2(data: list[str]) -> int:
    # Split data into fresh ingredient ID ranges and available ingredient IDs
    newline_idx: int = data.index("")
    fresh_ingredient_id_ranges: list[str] = sorted(
        [list(map(int, x.split("-"))) for x in data[:newline_idx]],
    )

    change_made: bool = True
    while change_made:
        change_made = False
        for idx in range(len(fresh_ingredient_id_ranges) - 1):
            if (
                fresh_ingredient_id_ranges[idx][1]
                >= fresh_ingredient_id_ranges[idx + 1][0]
                and fresh_ingredient_id_ranges[idx][1]
                < fresh_ingredient_id_ranges[idx + 1][1]
            ):
                fresh_ingredient_id_ranges[idx][1] = fresh_ingredient_id_ranges[
                    idx + 1
                ][1]
                change_made = True
            elif (
                fresh_ingredient_id_ranges[idx][1]
                >= fresh_ingredient_id_ranges[idx + 1][0]
                and fresh_ingredient_id_ranges[idx][1]
                >= fresh_ingredient_id_ranges[idx + 1][1]
            ):
                fresh_ingredient_id_ranges[idx + 1] = fresh_ingredient_id_ranges[idx]
                change_made = True

        fresh_ingredient_id_ranges = list(
            map(list, dict.fromkeys(map(tuple, fresh_ingredient_id_ranges)).keys()),
        )

    fresh_ingredient_ids_count = 0
    for idx in range(len(fresh_ingredient_id_ranges)):
        fresh_ingredient_ids_count += (
            fresh_ingredient_id_ranges[idx][1] - fresh_ingredient_id_ranges[idx][0] + 1
        )

    return fresh_ingredient_ids_count


# =============================================================================
# MAIN
# =============================================================================
if __name__ == "__main__":
    import time

    from src.aoc2025.solutions.day05.utils import parse

    # Example data
    example: list[str] = parse("src/aoc2025/solutions/day05/example.txt")
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
        data: list[str] = parse("src/aoc2025/solutions/day05/input.txt")
        print("\n\nTesting with real puzzle input:")
        try:
            # Time Part 1
            start: float = time.perf_counter()
            p1_answer: int = part1(data)
            p1_time: float = time.perf_counter() - start

            print(f"Part 1: {p1_answer: 6} ({p1_time * 1000:7.3f}ms)")
        except NameError as e:
            print(f"Warning: Solution 'Initial' missing required function: {e}")

        try:
            # Time Part 2
            start: float = time.perf_counter()
            p2_answer: int = part2(data)
            p2_time: float = time.perf_counter() - start

            print(f"Part 2: {p2_answer: 6} ({p2_time * 1000:7.3f}ms)")
        except NameError as e:
            print(
                f"Warning: Solution 'Initial' missing required function: {e}  - skipping",
            )
    except FileNotFoundError:
        print("\n(Real puzzle input not found - skipping)")
