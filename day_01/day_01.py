"""
# Day 1: Sonar Sweep
<https://adventofcode.com/2021/day/1>
"""
import pandas as pd


def read_input(path: str) -> pd.Series:
    return pd.read_csv(path, names=["measurement"]).measurement


def get_number_of_increases(values: pd.Series) -> int:
    return (values.diff() > 0).sum()


def get_rolling_number_of_increases(values: pd.Series) -> int:
    rolling_values = values.rolling(window=3).sum().dropna()
    return get_number_of_increases(rolling_values)


test_values = read_input("test_input.txt")
assert len(test_values) == 10
assert get_number_of_increases(test_values) == 7
assert get_rolling_number_of_increases(test_values) == 5

values = read_input("input.txt")
len(values)

# part 1 answer
get_number_of_increases(values)

# part 2 answer
get_rolling_number_of_increases(values)
