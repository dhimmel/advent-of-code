"""
Day 17: Trick Shot
https://adventofcode.com/2021/day/17
"""
from functools import cache

import numpy as np


@cache
def get_input(test: bool = True):
    if not test:
        x_min, x_max = 179, 201
        y_mix, y_max = -109, -63
        return x_min, x_max, y_mix, y_max
    x_min, x_max = 20, 30
    y_mix, y_max = -10, -5
    return x_min, x_max, y_mix, y_max


def fire(velocity_x: int, velocity_y: int):
    x, y = 0, 0
    while True:
        x += velocity_x
        y += velocity_y
        yield x, y
        # drag
        if velocity_x > 0:
            velocity_x -= 1
        if velocity_x < 0:
            velocity_x += 1
        # gravity
        velocity_y -= 1


def get_highest_y(velocity_x: int, velocity_y: int, test=True):
    x_min, x_max, y_min, y_max = get_input(test=test)
    highest_y = 0
    for x, y in fire(velocity_x, velocity_y):
        highest_y = max(highest_y, y)
        if y < y_min:
            return None
        if x_min <= x <= x_max and y_min <= y <= y_max:
            return highest_y


@cache
def grid_search(test=True):
    x_min, x_max, y_min, y_max = get_input(test=test)
    x_search = list(range(x_max + 1))
    y_search = list(range(y_min - 1, 750))
    grid = [[get_highest_y(x, y, test=test) for y in y_search] for x in x_search]
    grid = np.array(grid, dtype=np.float64)
    best_x_index, best_y_index = np.unravel_index(np.nanargmax(grid), grid.shape)
    return dict(
        max_height=int(np.nanmax(grid)),
        best_x=x_search[best_x_index],
        best_y=y_search[best_y_index],
        n_hits=np.count_nonzero(~np.isnan(grid)),
    )


# tests
assert get_highest_y(6, 9, test=True) == 45
assert grid_search(test=True)["max_height"] == 45
assert grid_search(test=True)["best_x"] == 6
assert grid_search(test=True)["best_y"] == 9
assert grid_search(test=True)["n_hits"] == 112

print(
    "Max reacheable height {max_height} via velocity x={best_x}, y={best_y}. Total velocities that hit {n_hits}".format(
        **grid_search(test=False)
    )
)
