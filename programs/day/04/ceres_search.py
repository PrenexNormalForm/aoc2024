# https://adventofcode.com/2024/day/4

from sys import stdin
from functools import cache


@cache
def puzzle_input():
    return list(line.strip() for line in stdin if line.strip())


def search_2d_term(list_2d, term):
    assert len(term) > 1

    for row, line in enumerate(list_2d):
        for col, _ in enumerate(line):
            for row_offset, col_offset in ((-1, 1), (0, 1), (1, 0), (1, 1)):
                seq = "".join(
                    list_2d[row + row_offset * i][col + col_offset * i]
                    for i in range(len(term))
                    if 0 <= row + row_offset * i < len(list_2d)
                    and col + col_offset * i < len(list_2d[row + row_offset * i])
                )
                if seq == term:
                    yield (row, col)
                if seq[::-1] == term:
                    yield (row, col)


def search_2d_pattern(list_2d, pattern):
    for row, line in enumerate(list_2d):
        for col, _ in enumerate(line):
            pattern_match = True
            for row_offset, pattern_line in enumerate(pattern):
                for col_offset, pattern_piece in enumerate(pattern_line):
                    if pattern_piece != "." and (
                        (row + row_offset) >= len(list_2d)
                        or col + col_offset >= len(line)
                        or list_2d[row + row_offset][col + col_offset] != pattern_piece
                    ):
                        pattern_match = False
            if pattern_match:
                yield (row, col)


def search_x_mas(puzzle_input):
    return sum(
        sum(1 for _ in search_2d_pattern(puzzle_input, pattern))
        for pattern in (
            ("M.S", ".A.", "M.S"),
            ("S.S", ".A.", "M.M"),
            ("M.M", ".A.", "S.S"),
            ("S.M", ".A.", "S.M"),
        )
    )


if __name__ == "__main__":
    print(f'XMAS count: {sum(1 for _ in search_2d_term(puzzle_input(), "XMAS"))}')
    print(f"X-MAS count: {search_x_mas(puzzle_input())}")
