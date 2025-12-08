"""
Advent of Code 2025 - Day 4: Printing Department.

My initial working solution - first draft before refactoring.
"""


# =============================================================================
# SOLUTION 1: My Initial Solution
# =============================================================================
def part1(data: list[str]) -> int:
    verbose: bool = False

    width: int = len(data[0])
    length: int = len(data)

    accessible_paper_rolls: int = 0

    for row in range(length):
        for column in range(width):
            check_for_paper: list[bool] = [
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
            ]

            if data[row][column] == ".":
                if verbose:
                    print(data[row][column], end="")
                continue

            if row == 0:
                if column in (0, width - 1):
                    # We don't need to check this, there are only 3 possible loactions
                    # Since it is a paper roll, we count it.
                    pass
                else:
                    check_for_paper[2] = data[row][column + 1] == "@"
                    check_for_paper[3] = data[row + 1][column + 1] == "@"
                    check_for_paper[4] = data[row + 1][column] == "@"
                    check_for_paper[5] = data[row + 1][column - 1] == "@"
                    check_for_paper[6] = data[row][column - 1] == "@"

            elif row == length - 1:
                if column in (0, width - 1):
                    # These are corners. We don't need to check them,
                    # becuse there are only 3 possible loactions.
                    pass
                else:
                    check_for_paper[0] = data[row - 1][column] == "@"
                    check_for_paper[1] = data[row - 1][column + 1] == "@"
                    check_for_paper[2] = data[row][column + 1] == "@"
                    check_for_paper[6] = data[row][column - 1] == "@"
                    check_for_paper[7] = data[row - 1][column - 1] == "@"
            elif column == 0:
                check_for_paper[0] = data[row - 1][column] == "@"
                check_for_paper[1] = data[row - 1][column + 1] == "@"
                check_for_paper[2] = data[row][column + 1] == "@"
                check_for_paper[3] = data[row + 1][column + 1] == "@"
                check_for_paper[4] = data[row + 1][column] == "@"
            elif column == length - 1:
                check_for_paper[0] = data[row - 1][column] == "@"
                check_for_paper[4] = data[row + 1][column] == "@"
                check_for_paper[5] = data[row + 1][column - 1] == "@"
                check_for_paper[6] = data[row][column - 1] == "@"
                check_for_paper[7] = data[row - 1][column - 1] == "@"
            else:
                check_for_paper[0] = data[row - 1][column] == "@"
                check_for_paper[1] = data[row - 1][column + 1] == "@"
                check_for_paper[2] = data[row][column + 1] == "@"
                check_for_paper[3] = data[row + 1][column + 1] == "@"
                check_for_paper[4] = data[row + 1][column] == "@"
                check_for_paper[5] = data[row + 1][column - 1] == "@"
                check_for_paper[6] = data[row][column - 1] == "@"
                check_for_paper[7] = data[row - 1][column - 1] == "@"

            # print(f"{row}{column}: {data[row][column]}")
            # print(check_for_paper)
            # print()
            paper_roll_threshold: int = 4
            if sum(check_for_paper) < paper_roll_threshold and data[row][column] == "@":
                accessible_paper_rolls += 1
            if verbose:
                print(data[row][column], end="")
        if verbose:
            print(f" [+{accessible_paper_rolls:>2}]")

    return accessible_paper_rolls


def part2(data: list[str]) -> int:
    verbose: bool = False

    width: int = len(data[0])
    length: int = len(data)

    accessible_paper_rolls: int = 0
    accessible_paper_rolls_this_round: int = -1
    while accessible_paper_rolls_this_round != 0:
        accessible_paper_rolls_this_round = 0
        for row in range(length):
            for column in range(width):
                check_for_paper: list[bool] = [
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                ]

                if data[row][column] == ".":
                    if verbose:
                        print(data[row][column], end="")
                    continue

                if row == 0:
                    if column in (0, width - 1):
                        # We don't need to check this, there are only 3 possible loactions
                        # Since it is a paper roll, we count it.
                        pass
                    else:
                        check_for_paper[2] = data[row][column + 1] == "@"
                        check_for_paper[3] = data[row + 1][column + 1] == "@"
                        check_for_paper[4] = data[row + 1][column] == "@"
                        check_for_paper[5] = data[row + 1][column - 1] == "@"
                        check_for_paper[6] = data[row][column - 1] == "@"

                elif row == length - 1:
                    if column in (0, width - 1):
                        # These are corners. We don't need to check them,
                        # becuse there are only 3 possible loactions.
                        pass
                    else:
                        check_for_paper[0] = data[row - 1][column] == "@"
                        check_for_paper[1] = data[row - 1][column + 1] == "@"
                        check_for_paper[2] = data[row][column + 1] == "@"
                        check_for_paper[6] = data[row][column - 1] == "@"
                        check_for_paper[7] = data[row - 1][column - 1] == "@"
                elif column == 0:
                    check_for_paper[0] = data[row - 1][column] == "@"
                    check_for_paper[1] = data[row - 1][column + 1] == "@"
                    check_for_paper[2] = data[row][column + 1] == "@"
                    check_for_paper[3] = data[row + 1][column + 1] == "@"
                    check_for_paper[4] = data[row + 1][column] == "@"
                elif column == length - 1:
                    check_for_paper[0] = data[row - 1][column] == "@"
                    check_for_paper[4] = data[row + 1][column] == "@"
                    check_for_paper[5] = data[row + 1][column - 1] == "@"
                    check_for_paper[6] = data[row][column - 1] == "@"
                    check_for_paper[7] = data[row - 1][column - 1] == "@"
                else:
                    check_for_paper[0] = data[row - 1][column] == "@"
                    check_for_paper[1] = data[row - 1][column + 1] == "@"
                    check_for_paper[2] = data[row][column + 1] == "@"
                    check_for_paper[3] = data[row + 1][column + 1] == "@"
                    check_for_paper[4] = data[row + 1][column] == "@"
                    check_for_paper[5] = data[row + 1][column - 1] == "@"
                    check_for_paper[6] = data[row][column - 1] == "@"
                    check_for_paper[7] = data[row - 1][column - 1] == "@"

                paper_roll_threshold: int = 4
                if (
                    sum(check_for_paper) < paper_roll_threshold
                    and data[row][column] == "@"
                ):
                    accessible_paper_rolls_this_round += 1
                    data[row][column] = "."
                if verbose:
                    print(data[row][column], end="")
            if verbose:
                print(f" [+{accessible_paper_rolls:>2}]")
        accessible_paper_rolls += accessible_paper_rolls_this_round

    return accessible_paper_rolls


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
