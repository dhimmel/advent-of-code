"""
Day 13: Transparent Origami
https://adventofcode.com/2021/day/13
"""
from pathlib import Path

import numpy as np


def dots_to_matrix(dots):
    shape = max(x for x, y in dots) + 1, max(y for x, y in dots) + 1
    matrix = np.zeros(shape, dtype=int)
    for x, y in dots:
        matrix[x, y] = 1
    return matrix.transpose()


def read_input(test: bool = True):
    path = Path(__file__).parent.joinpath("test_input.txt" if test else "input.txt")
    text = Path(path).read_text().strip()
    dot_strs, instruction_strs = (x.splitlines() for x in text.split("\n\n"))
    dots = list()
    for dot in dot_strs:
        x, y = (int(x) for x in dot.rstrip().split(","))
        dots.append((x, y))
    instructions = list()
    for inst_str in instruction_strs:
        axis, value = inst_str.split()[-1].split("=")
        instructions.append((axis, int(value)))
    return dots_to_matrix(dots), instructions


def fold_y(matrix, y: int):
    # responds to fold x
    assert matrix.shape[1] // 2 == y
    right = matrix[:, :y]
    left = matrix[:, y + 1 :]
    left = np.flip(left, axis=1)
    return right + left


def fold_x(matrix, x: int):
    # responds to fold y
    assert matrix.shape[0] // 2 == x
    top = matrix[:x, :]
    bottom = matrix[x + 1 :, :]
    bottom = np.flip(bottom, axis=0)
    return top + bottom


def origami(test=True, max_instructions=None):
    matrix, instructions = read_input(test=test)
    if max_instructions is not None:
        instructions = instructions[:max_instructions]
    for axis, value in instructions:
        # note reverse x/y compared to instructions
        fxn = fold_y if axis == "x" else fold_x
        matrix = fxn(matrix, value)
    return (matrix > 0).astype(int)


def part_1(test: bool = True) -> int:
    return origami(test=test, max_instructions=1).sum()


assert part_1(test=True) == 17
print("part 1", part_1(test=False))


def part_2(test: bool = True) -> str:
    matrix = origami(test=test, max_instructions=None)
    return (
        "\n".join("".join(map(str, row)) for row in matrix)
        .replace("0", ".")
        .replace("1", "#")
    )


assert (
    part_2(test=True)
    == """
#####
#...#
#...#
#...#
#####
.....
.....
""".strip()
)

part_2_result = part_2(test=False)
print(f"part 2\n{part_2_result}")
Path(__file__).parent.joinpath("part_2_output.txt").write_text(part_2_result + "\n")
