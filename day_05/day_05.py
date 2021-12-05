"""
Day 5: Hydrothermal Venture
https://adventofcode.com/2021/day/4
"""

from collections import Counter
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Line:
    x1: int
    y1: int
    x2: int
    y2: int

    @classmethod
    def from_string(cls, line_str: str) -> "Line":
        # x1,y1 -> x2,y2
        x1y1, x2y2 = line_str.strip().split(" -> ")
        x1, y1 = x1y1.split(",")
        x2, y2 = x2y2.split(",")
        return cls(x1=int(x1), y1=int(y1), x2=int(x2), y2=int(y2))

    def __str__(self):
        return f"{self.x1},{self.y1} -> {self.x2},{self.y2}"

    def vertical(self) -> bool:
        return self.x1 == self.x2

    def horizontal(self) -> bool:
        return self.y1 == self.y2

    @staticmethod
    def range(start, stop):
        if start < stop:
            return range(start, stop + 1)
        return range(start, stop - 1, -1)

    def points(self, exclude_diagonal: True) -> list[tuple[int, int]]:
        if self.horizontal():
            return [(x, self.y1) for x in self.range(self.x1, self.x2)]
        elif self.vertical():
            return [(self.x1, y) for y in self.range(self.y1, self.y2)]
        elif exclude_diagonal:
            return []
        return list(zip(self.range(self.x1, self.x2), self.range(self.y1, self.y2)))


def read_input(test=True) -> list[Line]:
    path = "test_input.txt" if test else "input.txt"
    text = Path(path).read_text()
    lines = list()
    for line_str in text.splitlines():
        lines.append(Line.from_string(line_str))
    return lines


def count_overlaps(test: bool = True, exclude_diagonal: bool = True) -> int:
    lines = read_input(test=test)
    all_points = list()
    for line in lines:
        all_points.extend(line.points(exclude_diagonal=exclude_diagonal))
    counts = Counter(all_points)
    return sum(c > 1 for c in counts.values())


assert 5 == count_overlaps(test=True, exclude_diagonal=True)
assert 12 == count_overlaps(test=True, exclude_diagonal=False)

print("part 1", count_overlaps(test=False, exclude_diagonal=True))
print("part 2", count_overlaps(test=False, exclude_diagonal=False))
