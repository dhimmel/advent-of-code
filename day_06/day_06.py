"""
Day 6: Lanternfish
https://adventofcode.com/2021/day/6
"""
from collections import Counter
from pathlib import Path

n_times = 9
"""Total number of day/time states a fish can exist in"""


def read_input(test=True) -> list[int]:
    path = "test_input.txt" if test else "input.txt"
    text = Path(path).read_text().strip()
    counts = Counter(int(x) for x in text.split(","))
    return [counts[i] for i in range(n_times)]


def increment(counts: list[int]) -> list[int]:
    new_counts = n_times * [0]
    for i in range(1, n_times):
        new_counts[i - 1] = counts[i]
    # lanternfish that creates a new fish resets its timer to 6
    new_counts[6] += counts[0]
    # new lanternfish starts with an internal timer of 8
    new_counts[n_times - 1] += counts[0]
    return new_counts


def population_size(days: int, test: bool) -> int:
    counts = read_input(test=test)
    for _ in range(days):
        counts = increment(counts)
    return sum(counts)


assert population_size(days=18, test=True) == 26
assert population_size(days=80, test=True) == 5934
assert population_size(days=256, test=True) == 26984457539

print("part 1", population_size(days=80, test=False))
print("part 2", population_size(days=256, test=False))
