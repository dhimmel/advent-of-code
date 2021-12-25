"""
Day 25: Sea Cucumber
https://adventofcode.com/2021/day/25
"""
from pathlib import Path

import numpy as np


def read_input(test: bool = True):
    path = Path(__file__).parent.joinpath("test_input.txt" if test else "input.txt")
    return np.array([list(line) for line in Path(path).read_text().splitlines()])


def step(array: np.ndarray) -> np.ndarray:
    """
    Every step, the sea cucumbers in the east-facing herd attempt to move forward one location,
    then the sea cucumbers in the south-facing herd attempt to move forward one location.
    """
    next_array = array.copy()
    for i, j in np.argwhere(array == ">"):
        next_j = j + 1 if j + 1 < array.shape[1] else 0
        if array[i, next_j] == ".":
            next_array[i, j] = "."
            next_array[i, next_j] = ">"
    array = next_array.copy()
    for i, j in np.argwhere(array == "v"):
        next_i = i + 1 if i + 1 < array.shape[0] else 0
        if array[next_i, j] == ".":
            next_array[i, j] = "."
            next_array[next_i, j] = "v"
    return next_array


def count_steps(test: bool = True) -> int:
    array = read_input(test=test)
    n_steps = 0
    while True:
        n_steps += 1
        # print("\n".join("".join(row) for row in array), "\n")
        next_array = step(array)
        if (next_array == array).all():
            break
        array = next_array
    return n_steps


assert count_steps(test=True) == 58
print("part 1", count_steps(test=False))  # 598
