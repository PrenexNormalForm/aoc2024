# https://adventofcode.com/2024/day/3
from functools import cache
from sys import stdin
import re

MUL_REGEX = r"mul\((\d{1,3}),(\d{1,3})\)"
INSTRUCTION_REGEX = r"(?P<ins>mul|do|don't)\((?:(\d{1,3})(?:,(\d{1,3}))?)?\)"


@cache
def puzzle_input():
    return stdin.read()


def all_multiplications(puzzle_input):
    return (int(a) * int(b) for a, b in re.findall(MUL_REGEX, puzzle_input))


def all_enabled_multiplications(puzzle_input):
    remaining_input = puzzle_input
    mul_enabled = True
    while match := re.search(INSTRUCTION_REGEX, remaining_input):
        ins, arg0, arg1 = match.group("ins"), match.group(2), match.group(3)
        match ins, arg0, arg1:
            case ["mul", a, b] if a and b and mul_enabled:
                yield int(a) * int(b)
            case ["do", None, None]:
                mul_enabled = True
            case ["don't", None, None]:
                mul_enabled = False
        remaining_input = remaining_input[match.end() :]


if __name__ == "__main__":
    print(
        f"Sum of all uncorrupted mul instructions: {sum(all_multiplications(puzzle_input()))}"
    )
    print(
        f"Sum of all enabled uncorrupted mul instructions: {sum(all_enabled_multiplications(puzzle_input()))}"
    )
