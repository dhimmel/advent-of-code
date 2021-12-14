"""
Day 14: Extended Polymerization
https://adventofcode.com/2021/day/14
"""
from pathlib import Path
from typing import Counter


def read_input(test: bool = True):
    path = Path(__file__).parent.joinpath("test_input.txt" if test else "input.txt")
    template, _, *insertions = Path(path).read_text().splitlines()
    insertions = [x.split(" -> ") for x in insertions]
    return template, insertions


def string_polymerizer(polymer, insertions, iterations=10):
    for _ in range(iterations):
        last_polymer = ""
        while last_polymer != polymer:
            last_polymer = polymer
            for match, insert in insertions:
                polymer = polymer.replace(match, match[0] + insert.lower() + match[1])
        polymer = polymer.upper()
    return polymer


def part_1(test=True, iterations=10):
    polymer, insertions = read_input(test=test)
    polymer = string_polymerizer(polymer, insertions=insertions, iterations=iterations)
    counts = Counter(polymer)
    return max(counts.values()) - min(counts.values())


assert part_1(test=True) == 1588
print("part 1", part_1(test=False))


def part_2(test=True, iterations=10):
    """Scalable polymerizer for part 2"""
    polymer, insertions = read_input(test=test)
    # convert string to 2-grams (pairs of letters)
    counts = Counter("".join(x) for x in zip(polymer, polymer[1:]))
    for _ in range(iterations):
        next_counts = Counter()
        for match, insert in insertions:
            if match not in counts:
                continue
            count = counts.pop(match)
            for new_pair in match[0] + insert, insert + match[1]:
                next_counts[new_pair] += count
        counts += next_counts
    letter_counts = Counter()
    for pair, count in counts.items():
        first_letter, _ = pair
        letter_counts[first_letter] += count
    # final letter is always the same
    letter_counts[polymer[-1]] += 1
    return max(letter_counts.values()) - min(letter_counts.values())


assert part_2(test=True, iterations=10) == 1588
assert part_2(test=True, iterations=40) == 2188189693529
print("part 2", part_2(test=False, iterations=40))
