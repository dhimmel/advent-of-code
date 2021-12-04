"""
Day 4: Giant Squid
https://adventofcode.com/2021/day/4
"""
from pathlib import Path
from io import StringIO
from typing import Optional
import pandas as pd

def read_board(board: str) -> pd.DataFrame:
    return pd.read_fwf(StringIO(board), header=None)

def read_input(test=True) -> tuple[list[int], list[pd.DataFrame]]:
    path =  "test_input.txt" if test else "input.txt"
    text = Path(path).read_text()
    draws, *boards = text.split("\n\n")
    draws = [int(x) for x in draws.split(",")]
    boards =[read_board(board) for board in boards]
    return draws, boards

def bingo_score(draws: list[int], board: pd.DataFrame, i: int) -> Optional[None]:
    calls = draws[:i+1]
    hits = board.isin(calls)
    bingo = hits.all(axis=0).any() or hits.all(axis=1).any()
    if bingo:
        # summing the whole dataframe ignored the hits mask
        return int(board[~hits].sum().sum()) * calls[i]

def get_winning_scores(test=True) -> list[int]:
    """Return winning board scores in order of the win."""
    draws, boards = read_input(test=test)
    player_to_board = dict(enumerate(boards))
    for i in range(len(draws)):
        for player, board in list(player_to_board.items()):
            score = bingo_score(draws, board, i)
            if score is not None:
                yield score
                player_to_board.pop(player)
                continue

test_scores = list(get_winning_scores(True))
assert test_scores[0] == 4512  # part 1
assert test_scores[-1] == 1924  # part 2

scores = list(get_winning_scores(True))
print(f"part 1: {scores[0]}\npart 2: {scores[-1]}")
