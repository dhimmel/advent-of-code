"""
Day 22: Reactor Reboot
https://adventofcode.com/2021/day/22
"""
import itertools
from pathlib import Path

import numpy as np
import parse


def read_input(test: bool = True):
    path = Path(__file__).parent.joinpath("test_input.txt" if test else "input.txt")
    text = Path(path).read_text().strip()
    # https://github.com/r1chardj0n3s/parse
    steps = parse.findall(
        "{switch:S} x={x_min:d}..{x_max:d},y={y_min:d}..{y_max:d},z={z_min:d}..{z_max:d}",
        string=text,
    )
    return list(steps)


def get_cubes(step, offset=50):
    x_min = max(step["x_min"], -offset)
    x_max = min(step["x_max"], offset)
    y_min = max(step["y_min"], -offset)
    y_max = min(step["y_max"], offset)
    z_min = max(step["z_min"], -offset)
    z_max = min(step["z_max"], offset)
    return itertools.product(
        range(x_min + offset, x_max + offset + 1),
        range(y_min + offset, y_max + offset + 1),
        range(z_min + offset, z_max + offset + 1),
    )


def part_1(test=True):
    steps = read_input(test=test)
    size = 101
    core = np.zeros((size, size, size), dtype=int)
    for step in steps:
        for x, y, z in get_cubes(step):
            core[x, y, z] = int(step["switch"] == "on")
    return core.sum()


assert part_1(test=True) == 590784
print("part 1", part_1(test=False))
