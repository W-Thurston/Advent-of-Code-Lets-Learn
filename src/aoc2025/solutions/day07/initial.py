"""
Advent of Code 2025 - Day 7: Laboratories.

My initial working solution - first draft before refactoring.
"""


# =============================================================================
# SOLUTION 1: My Initial Solution
# =============================================================================
def part1(data: list[str]) -> int:
    verbose: bool = False

    data = [list(x) for x in data]

    splitter_counter: int = 0
    beam_locations: int = [data[0].index("S")]
    if verbose:
        print("".join(data[0]))
    for row_idx in range(1, len(data)):
        new_beam_locations: list[int] = []
        for idx in beam_locations:
            if data[row_idx][idx] == "^":
                if verbose:
                    data[row_idx][idx - 1] = "|"
                    data[row_idx][idx + 1] = "|"
                new_beam_locations.extend([idx - 1, idx + 1])
                splitter_counter += 1
            else:
                if verbose:
                    data[row_idx][idx] = "|"
                new_beam_locations.extend([idx])

        if verbose:
            print("".join(data[row_idx]))
        beam_locations = list(set(new_beam_locations))

    return splitter_counter


def part2(data: list[str]) -> int:
    verbose: bool = False

    data = [list(x.replace(".", "0").replace("S", "1")) for x in data]

    beam_locations: int = [data[0].index("1")]
    if verbose:
        print("0000000S0000000")
    for row_idx in range(1, len(data)):
        new_beam_locations: list[int] = []
        for idx in beam_locations:
            if data[row_idx][idx] == "^":
                data[row_idx][idx - 1] = str(
                    int(data[row_idx][idx - 1]) + int(data[row_idx - 1][idx]),
                )
                data[row_idx][idx + 1] = str(
                    int(data[row_idx][idx + 1]) + int(data[row_idx - 1][idx]),
                )
                new_beam_locations.extend([idx - 1, idx + 1])
            else:
                data[row_idx][idx] = str(
                    int(data[row_idx][idx]) + int(data[row_idx - 1][idx]),
                )
                new_beam_locations.extend([idx])

        if verbose:
            print("".join(data[row_idx]))
        beam_locations = list(set(new_beam_locations))

    unique_paths: int = sum(int(x) for x in data[-1])
    return unique_paths


# =============================================================================
# MAIN
# =============================================================================
if __name__ == "__main__":
    import time

    from src.aoc2025.solutions.day07.utils import parse

    # Example data
    example: list[str] = parse("src/aoc2025/solutions/day07/example.txt")
    print("Testing with example data:")
    try:
        # Time Part 1
        start: float = time.perf_counter()
        p1_answer: int = part1(example)
        p1_time: float = time.perf_counter() - start

        print(f"Part 1: {p1_answer: 8} ({p1_time * 1000:7.3f}ms)")
    except NameError as e:
        print(f"Warning: Solution 'Initial' missing required function: {e}")

    try:
        # Time Part 2
        start: float = time.perf_counter()
        p2_answer: int = part2(example)
        p2_time: float = time.perf_counter() - start

        print(f"Part 2: {p2_answer: 8} ({p2_time * 1000:7.3f}ms)")
    except NameError as e:
        print(f"Warning: Solution 'Initial' missing required function: {e}  - skipping")

    # Real data
    try:
        data: list[str] = parse("src/aoc2025/solutions/day07/input.txt")
        print("\n\nTesting with real puzzle input:")
        try:
            # Time Part 1
            start: float = time.perf_counter()
            p1_answer: int = part1(data)
            p1_time: float = time.perf_counter() - start

            print(f"Part 1: {p1_answer: 15} ({p1_time * 1000:7.3f}ms)")
        except NameError as e:
            print(f"Warning: Solution 'Initial' missing required function: {e}")

        try:
            # Time Part 2
            start: float = time.perf_counter()
            p2_answer: int = part2(data)
            p2_time: float = time.perf_counter() - start

            print(f"Part 2: {p2_answer: 15} ({p2_time * 1000:7.3f}ms)")
        except NameError as e:
            print(
                f"Warning: Solution 'Initial' missing required function: {e}  - skipping",
            )
    except FileNotFoundError:
        print("\n(Real puzzle input not found - skipping)")
