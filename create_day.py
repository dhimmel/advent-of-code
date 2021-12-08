import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("day", type=int)
parser.add_argument("--year", type=int, default=2021)
args = parser.parse_args()
day_str = f"day_{args.day:02d}"
directory = Path(day_str)
directory.mkdir()
directory.joinpath("input.txt").write_text("")
directory.joinpath("test_input.txt").write_text("")
py_code = f'''\
"""
Day {args.day}:
https://adventofcode.com/{args.year}/day/{args.day}
"""
from pathlib import Path
import pandas as pd
import numpy as np


def read_input(test: bool = True):
    path = Path(__file__).parent.joinpath("test_input.txt" if test else "input.txt")
    text = Path(path).read_text().strip()
    return text
'''
directory.joinpath(f"{day_str}.py").write_text(py_code)
