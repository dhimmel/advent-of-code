"""
# Day 2: Dive!
https://adventofcode.com/2021/day/2/answer
"""

import pandas as pd


def read_input(path: str) -> pd.DataFrame:
    return pd.read_csv(path, sep=" ", names=["direction", "amount"])


def part_1(move_df) -> int:
    position = 0
    depth = 0
    for move in move_df.itertuples():
        if move.direction == "forward":
            position += move.amount
        elif move.direction == "up":
            # overengineering: they never tried to move the submarine into the air
            depth = max(0, depth - move.amount)
        elif move.direction == "down":
            depth += move.amount
    return position * depth


def part_2(move_df) -> int:
    position = 0
    depth = 0
    aim = 0
    for move in move_df.itertuples():
        if move.direction == "forward":
            position += move.amount
            # increases your depth by your aim multiplied by X
            depth += aim * move.amount
        elif move.direction == "up":
            aim -= move.amount
        elif move.direction == "down":
            aim += move.amount
    return position * depth

# test data
test_moves = read_input("test_input.txt")
assert part_1(test_moves) == 150
assert part_2(test_moves) == 900

# competition data
moves = read_input("input.txt")
print("part 1", part_1(moves))
print("part 2", part_2(moves))
