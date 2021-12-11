"""
Day 8: The Treachery of Whales
https://adventofcode.com/2021/day/8
"""
from pathlib import Path

# def read_input(test: bool = True):
#     path = Path(__file__).parent.joinpath("test_input.txt" if test else "input.txt")
#     for line in Path(path).read_text().splitlines():
#         signals, outputs = line.strip().split(" | ")
#         yield signals.split(), outputs.split()


# def decode_fixed_len(output):
#     letters_to_digit = dict(cf=2, bcdf=4, acf=7, abcdefg=8)
#     len_to_letters = {len(k): k for k in letters_to_digit}
#     if len(output) not in len_to_letters:
#         return None
#     letters = len_to_letters[len(output)]
#     # decoder = dict(zip(output, letters))
#     return letters_to_digit[letters]


# def part_1(test: bool = True):
#     part_1_count = 0
#     for signals, outputs in read_input(True):
#         for output in outputs:
#             digit = decode_fixed_len(output)
#             if digit:
#                 part_1_count += 1
#     return part_1_count


# assert part_1(test=True) == 26
# print("part 1:", part_1(test=False))

str_code_to_digit = dict(
    abcefg=0,
    cf=1,
    acdeg=2,
    acdfg=3,
    bcdf=4,
    abdfg=5,
    abdefg=6,
    acf=7,
    abcdefg=8,
    abcdfg=9,
)
set_code_to_digit = {frozenset(k): v for k, v in str_code_to_digit.items()}

length_solver = {
    len(code): code for code in set_code_to_digit if len(code) in {2, 3, 4, 7}
}


class Line:
    def __init__(self, line: str) -> None:
        inputs, outputs = line.strip().split(" | ")
        self.inputs = [frozenset(x) for x in inputs.split()]
        self.outputs = [frozenset(x) for x in outputs.split()]
        self.len_to_inputs = dict()
        for input in self.inputs:
            self.len_to_inputs.setdefault(len(input), list()).append(input)
        self.bad_code_to_good = dict()
        self.letter_map = dict()

    @property
    def good_code_to_bad(self):
        return {v: k for k, v in self.bad_code_to_good.items()}

    def map_codes(self):
        for leng, inputs in self.len_to_inputs.items():
            # solves cf=1,acf=7,bcdf=4,abcdefg=8
            if len(inputs) == 1:
                self.bad_code_to_good[inputs[0]] = length_solver[leng]
        (bad_a,) = (
            self.good_code_to_bad[frozenset("acf")]
            - self.good_code_to_bad[frozenset("cf")]
        )
        self.letter_map[bad_a] = "a"
        for input in self.len_to_inputs[6]:
            # solves abdefg=6
            if self.good_code_to_bad[frozenset("cf")] - input:
                self.bad_code_to_good[input] = frozenset("abdefg")


def read_input(test: bool = True) -> list[Line]:
    path = Path(__file__).parent.joinpath("test_input.txt" if test else "input.txt")
    return [Line(line) for line in Path(path).read_text().splitlines()]


line = read_input()[0]
line.map_codes()
print(line.bad_code_to_good)


# cf=1,
# acf=7,
# bcdf=4,
# abdfg=5,
# acdeg=2,
# acdfg=3,
# abcdfg=9,
# abcefg=0,
# abdefg=6,
# abcdefg=8,
