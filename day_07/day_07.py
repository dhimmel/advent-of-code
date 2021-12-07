"""
Day 7: The Treachery of Whales
https://adventofcode.com/2021/day/7
"""
from pathlib import Path
from math import comb

def read_input(test: bool=True) -> list[int]:
    path = "test_input.txt" if test else "input.txt"
    text = Path(path).read_text().strip()
    return [int(x) for x in text.split(",")]

def compute_fuel(n_moves: int, constant: bool=True) -> int:
    if constant:
        return abs(n_moves)
    # crab submarine engines don't burn fuel at a constant rate
    return comb(abs(n_moves) + 1, 2)

def get_min_fuel(test: bool=True, constant: bool=True) -> int:
    positions = read_input(test=test)
    scores = list()
    for i in range(min(positions), max(positions) + 1):
        score = sum(compute_fuel(pos - i, constant=constant) for pos in positions)
        scores.append((score, i))
    fuel, position = min(scores)
    return fuel

assert get_min_fuel(test=True, constant=True) == 37
assert get_min_fuel(test=True, constant=False) == 168

print("part 1", get_min_fuel(test=False, constant=True))
print("part 2", get_min_fuel(test=False, constant=False))
