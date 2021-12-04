# Day 3: Binary Diagnostic
# https://adventofcode.com/2021/day/3

from pathlib import Path

import pandas as pd


def read_file(test=True) -> pd.DataFrame:
    path = "test_input.txt" if test else "input.txt"
    rows = list()
    for line in Path(path).read_text().splitlines():
        rows.append([int(x) for x in line.strip()])
    return pd.DataFrame(rows)


def get_mode(col: pd.Series) -> int:
    return int(sum(col) >= sum(col == 0))


def get_anti_mode(col: pd.Series) -> int:
    return int(sum(col) < sum(col == 0))


def binary_to_int(values: list[int]) -> int:
    binary_string = "".join([str(x) for x in values])
    return int(binary_string, base=2)


def part_1(test: bool = True) -> int:
    df = read_file(test)
    gamma_rate = binary_to_int(df.apply(get_mode))
    epsilon_rate = binary_to_int(df.apply(get_anti_mode))
    return gamma_rate * epsilon_rate


assert part_1(test=True) == 198
print("part 1", part_1(test=False))

# Part 2


def get_rating(df, anti: bool) -> int:
    filtered_df = df.copy()
    for i in range(len(filtered_df.columns)):
        values = filtered_df.iloc[:, i]
        fxn = get_anti_mode if anti else get_mode
        mode = fxn(values)
        filtered_df = filtered_df[values == mode]
        if len(filtered_df) == 1:
            break
    return binary_to_int(filtered_df.iloc[0, :])


def part_2(test=True) -> int:
    df = read_file(test)
    oxygen_generator_rating = get_rating(df, anti=False)
    co2_scrubber_rating = get_rating(df, anti=True)
    return oxygen_generator_rating * co2_scrubber_rating


assert part_2(test=True) == 230
print("part 2", part_2(test=False))
