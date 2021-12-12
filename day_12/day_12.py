"""
Day 12:
https://adventofcode.com/2021/day/12
"""
from pathlib import Path
from typing import Counter, Iterator

import networkx as nx


def read_input(test: bool = True) -> nx.Graph:
    path = Path(__file__).parent.joinpath("test_input.txt" if test else "input.txt")
    graph = nx.Graph()
    for line in Path(path).read_text().strip().splitlines():
        graph.add_edge(*line.split("-"))
    return graph


def breadth_first_paths(
    graph: nx.Graph, path: list[str], part_2: bool = False
) -> Iterator[list[str]]:
    # for part 2: a single small cave can be visited at most twice,
    # and the remaining small caves can be visited at most once.
    node_counts = Counter(x for x in path if x == x.lower())
    ((_, max_count),) = node_counts.most_common(n=1)
    has_duplicate_small = max_count > 1
    # breadth first search
    for node in graph.neighbors(path[-1]):
        if node == "start":
            continue
        if node == node.lower():
            if not part_2 and node in path:
                continue
            if part_2 and has_duplicate_small and node in path:
                continue
        new_path = path + [node]
        yield new_path
        if node != "end":
            yield from breadth_first_paths(graph, new_path, part_2)


def count_paths(test: bool, part_2: bool) -> int:
    graph = read_input(test=test)
    paths = breadth_first_paths(graph, ["start"], part_2=part_2)
    paths = [path for path in paths if path[-1] == "end"]
    return len(paths)


assert count_paths(test=True, part_2=False) == 10
assert count_paths(test=True, part_2=True) == 36
print("part 1", count_paths(test=False, part_2=False))
print("part 2", count_paths(test=False, part_2=True))
