"""
Day 8: The Treachery of Whales
https://adventofcode.com/2021/day/8
"""
from pathlib import Path


def read_input(test: bool = True):
    path = Path(__file__).parent.joinpath("test_input.txt" if test else "input.txt")
    for line in Path(path).read_text().splitlines():
        signals, outputs = line.strip().split(" | ")
        yield signals.split(), outputs.split()


def decode_fixed_len(output):
    letters_to_digit = dict(cf=2, bcdf=4, acf=7, abcdefg=8)
    len_to_letters = {len(k): k for k in letters_to_digit}
    if len(output) not in len_to_letters:
        return None
    letters = len_to_letters[len(output)]
    # decoder = dict(zip(output, letters))
    return letters_to_digit[letters]


def part_1(test: bool = True):
    part_1_count = 0
    for signals, outputs in read_input(True):
        for output in outputs:
            digit = decode_fixed_len(output)
            if digit:
                part_1_count += 1
    return part_1_count


assert part_1(test=True) == 26
print("part 1:", part_1(test=False))
