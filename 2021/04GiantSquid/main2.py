#!/usr/bin/env python

"""
Advent of code 2021
Day 04 : Giant Squid
https://adventofcode.com/2021/day/4
"""

# Started   at xx:xx
# Completed at xx:xx

import argparse
import sys

def printf(fmt_str, *args):
    """
    C like printf
    """

    sys.stdout.write(fmt_str % args)

class BingoGrid():

    def __init__(self, nb_grid) -> None:

        self.nb_grid = nb_grid
        self.mark_grid = [[False] * len(nb_grid[0]) for _ in range(len(nb_grid))]
        # print(self.mark_grid)

    def print(self):

        for (row_idx, row) in enumerate(self.nb_grid):
            for (line_idx, number) in enumerate(row):
                if self.mark_grid[row_idx][line_idx]:
                    printf("x")
                else:
                    printf(" ")
                printf("%02u ", number)
            printf("\n")

    def mark(self, nb_in):

        for (row_idx, row) in enumerate(self.nb_grid):
            for (line_idx, number) in enumerate(row):
                if number == nb_in:
                    # printf("mark nb %u at row %u line %u\n", nb_in, row_idx, line_idx)
                    self.mark_grid[row_idx][line_idx] = True

        # print(self.mark_grid)

    def check_win(self):

        for line_idx in range(0, len(self.mark_grid), 1):
            line_complete = True
            for col_idx in range(0, len(self.mark_grid[0]), 1):
                if not self.mark_grid[line_idx][col_idx]:
                    line_complete = False
                    break
            if line_complete:
                return True

        for col_idx in range(0, len(self.mark_grid[0]), 1):
            col_complete = True
            for line_idx in range(0, len(self.mark_grid), 1):
                if not self.mark_grid[line_idx][col_idx]:
                    col_complete = False
                    break
            if col_complete:
                return True

        return False

    def get_score(self):

        score = 0

        for (line_idx, line) in enumerate(self.nb_grid):
            for (col_idx, number) in enumerate(line):
                if not self.mark_grid[line_idx][col_idx]:
                    score += number

        return score


def solve(data: str):
    """
    Solve puzzle
    """

    grid_list = []
    bingo_grid_list = []

    for data_grid in data.split("\n\n")[1:]:

        grid = []

        for data_grid_line in data_grid.split("\n"):

            grid_line = []

            for data_grid_line_nb in data_grid_line.split(" "):

                if data_grid_line_nb == "":
                    continue

                grid_line.append(int(data_grid_line_nb))

            grid.append(grid_line)

        grid_list.append(grid)

        bingo_grid = BingoGrid(grid)
        bingo_grid_list.append(bingo_grid)

    score = 0
    last_win = False
    nb_list = data.split("\n")[0].split(",")

    for nb_in in nb_list:
        nb_in = int(nb_in)

        bingo_grid_idx = 0
        while bingo_grid_idx < len(bingo_grid_list):

            bingo_grid = bingo_grid_list[bingo_grid_idx]
            bingo_grid.mark(nb_in)

            if bingo_grid.check_win():

                if len(bingo_grid_list) == 1:
                    score = bingo_grid.get_score()
                    score = score * nb_in
                    last_win = True
                    break

                bingo_grid_list.remove(bingo_grid)
                bingo_grid_idx -= 1

            bingo_grid_idx += 1

        if last_win:
            break

    return score

def main():
    """
    Main
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("file_name_in", type=str, action="store",
        default="input.txt", help="input file name")
    args = parser.parse_args()

    data_in = ""
    with open(args.file_name_in, "r", encoding="utf8") as file:
        data_in = file.read()

    ans = solve(data_in)
    printf("ans=%u\n", ans)

if __name__ == "__main__":
    main()
