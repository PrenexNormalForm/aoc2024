# https://adventofcode.com/2024/day/1


from sys import stdin
from functools import cache
from collections import Counter


@cache
def puzzle_input():
    lists = ([], [])
    for line in stdin:
        item0, item1 = (int(x) for x in line.split())
        lists[0].append(item0)
        lists[1].append(item1)
    return lists


def distance_sum(list_a, list_b):
    return sum(abs(a - b) for a, b in zip(sorted(list_a), sorted(list_b)))


def similarity_score(list_a, list_b):
    frequency = Counter(list_b)
    return sum(num * frequency[num] for num in list_a)


if __name__ == "__main__":
    print(f"Distance Sum: {distance_sum(*puzzle_input())}")
    print(f"Similarity Score: {similarity_score(*puzzle_input())}")
