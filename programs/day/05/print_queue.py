# https://adventofcode.com/2024/day/5

from sys import stdin
from functools import cache
from graphlib import TopologicalSorter


@cache
def puzzle_input():
    rules = set()
    updates = []
    for line in stdin:
        if "|" in line:
            rules.add(tuple(int(x) for x in line.strip().split("|")))
        elif "," in line:
            updates.append(tuple(int(x) for x in line.strip().split(",")))
    return frozenset(rules), tuple(updates)


def is_ordered_correctly(rules, update):
    for index, page_number in enumerate(update):
        for following_page_number in update[index + 1 :]:
            if (following_page_number, page_number) in rules:
                return False
    return True


def part1_solution(rules, updates):
    return sum(
        update[len(update) // 2]
        for update in updates
        if is_ordered_correctly(rules, update)
    )


def ordered_update(rules, update):
    update = set(update)
    sorter = TopologicalSorter()
    for a, b in rules:
        if a in update and b in update:
            sorter.add(b, a)
    return tuple(sorter.static_order())


def part2_solution(rules, updates):
    return sum(
        update[len(update) // 2]
        for update in (
            ordered_update(rules, update)
            for update in updates
            if not is_ordered_correctly(rules, update)
        )
    )


if __name__ == "__main__":
    print(f"  Correct order sum: {part1_solution(*puzzle_input())}")
    print(f"Incorrect order sum: {part2_solution(*puzzle_input())}")
