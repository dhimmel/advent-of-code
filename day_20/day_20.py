"""
Day 20: Trench Map
https://adventofcode.com/2021/day/20
"""
from functools import cache
from pathlib import Path

import numpy as np


def read_input(test: bool = True, pad_width=10):
    path = Path(__file__).parent.joinpath("test_input.txt" if test else "input.txt")
    pixel_map, image = Path(path).read_text().split("\n\n")
    image = [list(line) for line in image.splitlines()]
    image = np.array(image)
    image = np.pad(image, pad_width=pad_width, constant_values=".")
    return pixel_map, image


def get_replacement_pixel(image, pixel_map, i, j):
    return pixel_map[
        int(
            "".join(image[i - 1 : i + 2, j - 1 : j + 2].flatten())
            .replace(".", "0")
            .replace("#", "1"),
            base=2,
        )
    ]


def refine(image, pixel_map):
    output = np.full_like(image, fill_value=".")
    for i in range(1, image.shape[0] - 1):
        for j in range(1, image.shape[1] - 1):
            output[i, j] = get_replacement_pixel(image, pixel_map, i, j)
    return output


@cache
def multi_refine(test: True, n_times=2):
    pixel_map, image = read_input(test=test, pad_width=n_times * 2 + 10)
    for iteration in range(n_times):
        image = refine(image, pixel_map)
        if iteration % 2 == 1:
            image = image[3:-3, 3:-3]
            image = np.pad(image, pad_width=3, constant_values=".")
    # text_image = "\n".join("".join(row) for row in image)
    # Path(__file__).parent.joinpath("output.txt").write_text(text_image)
    return (image == "#").sum()


assert multi_refine(test=True, n_times=2) == 35
assert multi_refine(test=False, n_times=2) == 5498
print("part 1", multi_refine(test=False, n_times=2))

assert multi_refine(test=True, n_times=50) == 3351
assert multi_refine(test=False, n_times=50) == 16014
print("part 2", multi_refine(test=False, n_times=50))
