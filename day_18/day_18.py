"""
Day 18: Snailfish
https://adventofcode.com/2021/day/18
"""
from ast import literal_eval
from pathlib import Path


def read_input(test: bool = True):
    path = Path(__file__).parent.joinpath("test_input.txt" if test else "input.txt")
    return [literal_eval(line) for line in Path(path).read_text().splitlines()]


# snails = read_input()
# print(snails)


def explode(snail, depth=1):
    print(f"{snail=}")
    left, right = snail
    if depth > 4:
        print("explode")
    if isinstance(left, list):
        explode(left, depth + 1)
    if isinstance(right, list):
        explode(right, depth + 1)


input = [[[[[9, 8], 1], 2], 3], 4]
input = [[6, [5, [4, [3, 2]]]], 1]
explode(input)


def reduce(snail):
    raise NotImplementedError


def add(left, right):
    snail = [left, right]
    return reduce(snail)


def magnitude(snail) -> int:
    left, right = snail
    left_mag = 3 * (left if isinstance(left, int) else magnitude(left))
    right_mag = 2 * (right if isinstance(right, int) else magnitude(right))
    return left_mag + right_mag


assert magnitude([[1, 2], [[3, 4], 5]]) == 143
assert magnitude([[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]]) == 1384
assert (
    magnitude([[[[8, 7], [7, 7]], [[8, 6], [7, 7]]], [[[0, 7], [6, 6]], [8, 7]]])
    == 3488
)
