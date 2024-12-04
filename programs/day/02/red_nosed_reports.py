# https://adventofcode.com/2024/day/2


from functools import cache
from itertools import pairwise
from sys import stdin


@cache
def puzzle_input():
    reports = []
    for line in stdin:
        if line.strip():
            reports.append([int(s) for s in line.split()])
    return reports


def steps(iterable):
    return (b - a for a, b in pairwise(iterable))


def is_safe(report: list, problem_dampener=False):
    if len(report) <= 1:
        return False
    elif problem_dampener:
        # This could written to be in O(n) (n being len(report)),
        # but that would be annoying
        # and all the test cases are n <= 8  so whatever
        if is_safe(report):
            return True
        for i in range(len(report)):
            if is_safe(report[:i] + report[i + 1 :]):
                return True
        return False
    else:
        steps = {b - a for a, b in pairwise(report)}
        return steps > set() and (steps <= {1, 2, 3} or steps <= {-1, -2, -3})


def count_safe_reports(reports, problem_dampener=False):
    return sum(int(is_safe(report, problem_dampener)) for report in reports)


if __name__ == "__main__":
    print(f"Safe reports: {count_safe_reports(puzzle_input())}")
    print(
        f"Safe reports (with Problem Dampener): {count_safe_reports(puzzle_input(), problem_dampener=True)}"
    )
