"""
Day 24: Arithmetic Logic Unit
https://adventofcode.com/2021/day/24
"""
from pathlib import Path


def read_input(test: bool = False):
    path = Path(__file__).parent.joinpath("test_input.txt" if test else "input.txt")
    programs = [line.split() for line in Path(path).read_text().splitlines()]
    return programs


def run_program(program, inputs: list[int]):
    inputs = inputs.copy()
    variables = {x: 0 for x in "wxyz"}
    for instruction in program:
        if instruction[0] == "inp":
            variables[instruction[1]] = inputs.pop(0)
            continue
        operator, a, b = instruction
        b = variables[b] if b in variables else int(b)
        if operator == "add":
            variables[a] += b
        if operator == "mul":
            variables[a] *= b
        if operator == "div":
            variables[a] = variables[a] // b
        if operator == "mod":
            variables[a] = variables[a] % b
        if operator == "eql":
            variables[a] = int(variables[a] == b)
    return variables["z"] == 0


def count_down():
    for x in range(99_999_999_999_999, 0, -1):
        if "0" not in str(x):
            yield x


program = read_input()
for number in count_down():
    inputs = [int(x) for x in str(number)]
    if run_program(program, inputs):
        break
print("part 1", number)
