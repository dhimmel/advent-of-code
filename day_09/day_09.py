"""
Day 9:
https://adventofcode.com/2021/day/9
"""
from pathlib import Path

import numpy as np
from scipy.signal import argrelextrema


def read_input(test: bool = True) -> np.ndarray:
    path = Path(__file__).parent.joinpath("test_input.txt" if test else "input.txt")
    text = Path(path).read_text().strip()
    values = [[int(x) for x in line] for line in text.splitlines()]
    matrix = np.array(values)
    # pad matrix with 9 to handle corner cases
    return np.pad(matrix, pad_width=1, constant_values=9)


def get_low_points(matrix: np.ndarray) -> list[tuple[int, int]]:
    col_trema = set(zip(*argrelextrema(matrix, np.less, axis=0)))
    row_trema = set(zip(*argrelextrema(matrix, np.less, axis=1)))
    return sorted(col_trema & row_trema)


def part_1(test: bool = True) -> int:
    """risk_level"""
    matrix = read_input(test=test)
    low_points = get_low_points(matrix)
    return sum(1 + matrix[i, j] for i, j in low_points)


assert part_1(True) == 15
print("part 1:", part_1(False))


def find_basin(
    matrix: np.ndarray, low_i: int, low_j: int, basin: set[tuple[int, int]]
) -> set[tuple[int, int]]:
    basin.add((low_i, low_j))
    for i, j in (
        (low_i - 1, low_j),
        (low_i + 1, low_j),
        (low_i, low_j - 1),
        (low_i, low_j + 1),
    ):
        if matrix[i, j] == 9:
            continue
        if (i, j) in basin:
            continue
        basin.add((i, j))
        find_basin(matrix, i, j, basin)
    return basin


def part_2(test: bool = True) -> int:
    matrix = read_input(test=test)
    low_points = get_low_points(matrix)
    basin_sizes = sorted(
        (len(find_basin(matrix, i, j, set())) for i, j in low_points), reverse=True
    )
    return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]


assert part_2(True) == 1134
print("part 2:", part_2(False))
