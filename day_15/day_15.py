"""
Day 15: Chiton
https://adventofcode.com/2021/day/15
"""
from pathlib import Path

import numpy as np


def read_input(test: bool = True):
    path = Path(__file__).parent.joinpath("test_input.txt" if test else "input.txt")
    data = [
        [int(x) for x in line.rstrip()] for line in Path(path).read_text().splitlines()
    ]
    return np.array(data)


def increment_cost(cost: np.ndarray) -> np.ndarray:
    new_costs = cost + 1
    new_costs[new_costs > 9] = 1
    return new_costs


def expand_matrix(cost: np.ndarray, times=5) -> np.ndarray:
    arrays = [cost]
    for i in range(times - 1):
        arrays.append(increment_cost(arrays[-1]))
    slabs = [np.concatenate(arrays, axis=0)]
    for i in range(times - 1):
        slabs.append(increment_cost(slabs[-1]))
    return np.concatenate(slabs, axis=1)


def init_total_costs(cost: np.ndarray) -> np.ndarray:
    """Minimum Cost Path, dynamic programming"""
    len_i, len_j = cost.shape
    total = np.zeros_like(cost)
    for i in range(1, len_i):
        total[i][0] = total[i - 1][0] + cost[i][0]
    for j in range(1, len_j):
        total[0][j] = total[0][j - 1] + cost[0][j]
    for i in range(1, len_i):
        for j in range(1, len_j):
            total[i][j] = min(total[i - 1][j], total[i][j - 1]) + cost[i][j]
    return total


def iterate_total_costs(
    cost: np.ndarray, total: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    """Iterate on minimum cost path to allow backwards moves."""
    original_total = total.copy()
    len_i, len_j = cost.shape
    for i in range(0, len_i):
        for j in range(0, len_j):
            for before_i, before_j in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if before_i < 0 or before_i >= len_i:
                    continue
                if before_j < 0 or before_j >= len_j:
                    continue
                total[i, j] = min(total[i, j], total[before_i, before_j] + cost[i, j])
    if (total != original_total).any():
        # print("Iterating with cost matrix sum", total.sum())
        return iterate_total_costs(cost, total)
    return cost, total


def get_min_cost(test: bool = True, expand: bool = False) -> int:
    cost = read_input(test=test)
    if expand:
        cost = expand_matrix(cost)
    total = init_total_costs(cost)
    cost, total = iterate_total_costs(cost, total)
    return total[-1, -1]


assert get_min_cost(test=True, expand=False) == 40
print("part 1", get_min_cost(test=False, expand=False))

assert get_min_cost(test=True, expand=True) == 315
print("part 2", get_min_cost(test=False, expand=True))
