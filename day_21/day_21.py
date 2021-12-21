"""
Day 21: Dirac Dice
https://adventofcode.com/2021/day/21
"""
from dataclasses import dataclass


@dataclass
class Player:
    position: int
    score: int = 0

    def play(self, rolls):
        self.position += sum(next(rolls) for _ in range(3))
        while self.position > 10:
            self.position -= 10
        self.score += self.position

    def wins(self):
        return self.score >= 1000

    def __lt__(self, other):
        if other.__class__ is self.__class__:
            return self.score < other.score


def get_players(test: bool = True):
    if test:
        # Player 1 starting position: 4
        # Player 2 starting position: 8
        return Player(4), Player(8)
    # Player 1 starting position: 4
    # Player 2 starting position: 6
    return Player(4), Player(6)


@dataclass
class RollCount:
    count: int = 0


def roll(roll_count: RollCount):
    while True:
        for side in range(1, 101):
            # n_rolls += 1
            roll_count.count += 1
            yield side


def part_1(test: True):
    roll_count = RollCount()
    rolls = roll(roll_count)
    players = get_players(test=test)
    # print(players)
    winner = None
    while not winner:
        for player in players:
            player.play(rolls)
            # print(player)
            if player.wins():
                winner = player
                break
    return sorted(players)[0].score * roll_count.count


assert part_1(test=True) == 739785
print("part 1", part_1(test=False))
