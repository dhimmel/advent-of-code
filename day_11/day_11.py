"""
Day 11: Dumbo Octopus
https://adventofcode.com/2021/day/11
"""
from pathlib import Path
from typing import Iterator

import numpy as np


def read_input(test: bool = True):
    path = Path(__file__).parent.joinpath("test_input.txt" if test else "input.txt")
    lines = Path(path).read_text().splitlines()
    # use float not int values for np.nan compatability
    return np.array([[float(char) for char in line] for line in lines])


def neighbor_indices(matrix: np.ndarray, i: int, j: int) -> Iterator[tuple[int, int]]:
    for i_off in -1, 0, 1:
        for j_off in -1, 0, 1:
            i_new = i + i_off
            j_new = j + j_off
            if i == i_new and j == j_new:
                continue
            if (0 <= i_new < matrix.shape[0]) and (0 <= j_new < matrix.shape[1]):
                yield i_new, j_new


def stepper(matrix) -> tuple[np.ndarray, int]:
    matrix += 1
    while (matrix > 9).any():
        for i, j in np.ndindex(*matrix.shape):
            if matrix[i, j] > 9:
                matrix[i, j] = np.nan
                for i_nbr, j_nbr in neighbor_indices(matrix, i, j):
                    matrix[i_nbr, j_nbr] += 1
    n_flashes = np.isnan(matrix).sum()
    matrix = np.nan_to_num(matrix)
    return matrix, n_flashes


def get_flashes(test: bool = True, n_steps=100) -> int:
    """How many total flashes are there after 100 steps?"""
    matrix = read_input(test=test)
    total_flashes = 0
    for _ in range(n_steps):
        matrix, n_flashes = stepper(matrix)
        total_flashes += n_flashes
    return total_flashes


assert get_flashes(test=True) == 1656
print("part 1", get_flashes(test=False))


def first_all_flash(test: bool = True) -> int:
    """What is the first step during which all octopuses flash?"""
    matrix = read_input(test=test)
    step = 0
    while True:
        if (matrix).sum() == 0:
            return step
        matrix, _ = stepper(matrix)
        step += 1


assert first_all_flash(test=True) == 195
print("part 2", first_all_flash(test=False))
