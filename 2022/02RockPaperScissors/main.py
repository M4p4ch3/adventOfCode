#!/usr/bin/env python

"""
Advent of code 2022
Day 02 : Rock Paper Scissors
https://adventofcode.com/2022/day/2
"""

"""
A for Rock, B for Paper, and C for Scissors
X for Rock, Y for Paper, and Z for Scissors

The score for a single round is the score for the shape you selected
1 for Rock, 2 for Paper, and 3 for Scissors

plus the score for the outcome of the round
0 if you lost, 3 if the round was a draw, and 6 if you won
"""

from enum import Enum

class Rps(Enum):
    """
    RockPaperScissors (RPS)
    """
    ROCK = 0
    PAPER = 1
    SCISSORS = 2
    LAST = 3

class Outcome(Enum):
    """
    Outcome
    """
    LOSS = 0
    DRAW = 1
    WIN = 2
    LAST = 3

def get_rps_from_str(rps_str: str) -> Rps:
    """
    Get RPS from string

    Args:
        rps_str (str): RPS as tring

    Returns:
        Rps: RPS
    """

    rps = Rps.LAST

    if rps_str == "A":
        rps = Rps.ROCK
    elif rps_str == "B":
        rps = Rps.PAPER
    elif rps_str == "C":
        rps = Rps.SCISSORS
    else:
        rps = Rps.LAST

    return rps

def get_outcome_from_str(outcome_str: str) -> Outcome:
    """
    Get outcome from string

    Args:
        outcome_str (str): Outcome as string

    Returns:
        Outcome: Outcome
    """

    outcome = Outcome.LAST

    if outcome_str == "X":
        outcome = Outcome.LOSS
    elif outcome_str == "Y":
        outcome = Outcome.DRAW
    elif outcome_str == "Z":
        outcome = Outcome.WIN
    else:
        outcome = Outcome.LAST

    return outcome

def get_round_outcome(rps_opp: Rps, rps_mine: Rps) -> Outcome:
    """
    Get round outcome

    Args:
        rps_opp (Rps): Opponent RPS
        rps_mine (Rps): Mine RPS

    Returns:
        Outcome: Round outcome
    """

    outcome = Outcome.DRAW

    if (
        rps_opp == Rps.ROCK and rps_mine == Rps.PAPER or
        rps_opp == Rps.PAPER and rps_mine == Rps.SCISSORS or
        rps_opp == Rps.SCISSORS and rps_mine == Rps.ROCK
    ):
        outcome = Outcome.WIN
    elif (
        rps_opp == Rps.ROCK and rps_mine == Rps.SCISSORS or
        rps_opp == Rps.PAPER and rps_mine == Rps.ROCK or
        rps_opp == Rps.SCISSORS and rps_mine == Rps.PAPER
    ):
        outcome = Outcome.LOSS
    else:
        outcome = Outcome.DRAW

    return outcome

def get_rps_from_outcome(rps_opp: Rps, outcome: Outcome) -> Rps:
    """_summary_

    Args:
        rps_opp (Rps): _description_
        outcome (Outcome): _description_

    Returns:
        Rps: _description_
    """

    print(f"rps_opp={rps_opp}")
    print(f"outcome={outcome}")

    rps_mine = Rps.LAST

    if outcome == Outcome.DRAW:
        rps_mine = rps_opp
    elif outcome == Outcome.LOSS:
        if rps_opp == Rps.ROCK:
            rps_mine = Rps.SCISSORS
        elif rps_opp == Rps.PAPER:
            rps_mine = Rps.ROCK
        elif rps_opp == Rps.SCISSORS:
            rps_mine = Rps.PAPER
    elif outcome == Outcome.WIN:
        if rps_opp == Rps.ROCK:
            rps_mine = Rps.PAPER
        elif rps_opp == Rps.PAPER:
            rps_mine = Rps.SCISSORS
        elif rps_opp == Rps.SCISSORS:
            rps_mine = Rps.ROCK

    print(f"rps_mine={rps_mine}")

    return rps_mine

def get_round_score(rps_opp: Rps, outcome: Outcome) -> int:
    """
    Get roud score

    Args:
        rps_opp (Rps): Opponent RPS
        rps_mine (Rps): My RPS

    Returns:
        int: Round score
    """

    score = 0

    rps_mine = get_rps_from_outcome(rps_opp, outcome)
    if rps_mine == Rps.ROCK:
        score += 1
    elif rps_mine == Rps.PAPER:
        score += 2
    elif rps_mine == Rps.SCISSORS:
        score += 3

    # outcome = get_round_outcome(rps_opp, rps_mine)
    if outcome == Outcome.LOSS:
        score += 0
    elif outcome == Outcome.DRAW:
        score += 3
    elif outcome == Outcome.WIN:
        score += 6

    return score

def main():
    """
    Main
    """

    score_total = 0

    with open("input.txt", "r", encoding="utf8") as file:

        data = file.read()

        for line in data.split('\n'):

            if len(line) <= 1:
                continue

            rps_opp = get_rps_from_str(line[0])
            outcome = get_outcome_from_str(line[2])
            score_round = get_round_score(rps_opp, outcome)
            score_total += score_round

    print(score_total)

if __name__ == "__main__":
    main()
