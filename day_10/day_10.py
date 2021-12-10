"""
Day 10: Syntax Scoring
https://adventofcode.com/2021/day/10
"""
from pathlib import Path
from queue import LifoQueue
from typing import Literal


def read_input(test: bool = True):
    path = Path(__file__).parent.joinpath("test_input.txt" if test else "input.txt")
    return Path(path).read_text().strip().splitlines()


open_to_close = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

invalid_to_score = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}


def parse_line(line: str) -> tuple[Literal["invalid", "incomplete"], str]:
    queue = LifoQueue()
    for char in line:
        if char in open_to_close:
            queue.put(char)
        else:
            if char != open_to_close[queue.get()]:
                return "invalid", char
    completion_str = ""
    while not queue.empty():
        completion_str += open_to_close[queue.get()]
    return "incomplete", completion_str


def part_1(test: bool = True) -> int:
    score = 0
    for line in read_input(test=test):
        kind, invalid = parse_line(line)
        if kind == "invalid":
            score += invalid_to_score[invalid]
    return score


assert part_1() == 26397
print("part 1", part_1(test=False))


autocomplete_scores = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def part_2(test: bool = True) -> int:
    lines = read_input(test=test)
    scores = []
    for line in lines:
        kind, completion_str = parse_line(line)
        if kind != "incomplete":
            continue
        line_score = 0
        for char in completion_str:
            line_score *= 5
            line_score += autocomplete_scores[char]
        scores.append(line_score)
    scores.sort()
    return scores[len(scores) // 2]


assert part_2() == 288957
print("part 2", part_2(test=False))
