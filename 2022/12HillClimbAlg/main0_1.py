#!/usr/bin/env python

"""
Advent of code 2022
Day 12 : Hill Climbing Algorithm
https://adventofcode.com/2022/day/12
"""

# Started   at 10:05
# Paused    at 11:45

# Resumed   at 11:55
# Paused    at 12:00

# Resumed   at 12:55
# Paused    at 14:20

# Resumed   at TODO
# Completed at TODO

import argparse
import math
import random
import sys
from typing import List

def printf(fmt_str, *args):
    """
    C like printf
    """

    sys.stdout.write(fmt_str % args)

class Coord():
    """coord"""

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def get_delta(self, coord):
        """get delta from Coord"""
        return Coord(coord.x - self.x, coord.y - self.y)

    def get_dist(self, coord) -> int:
        """get distance from Coord"""
        delta = self.get_delta(coord)
        return int(math.sqrt(delta.x * delta.x + delta.y * delta.y))

    def clone(self):
        """clone"""
        return Coord(self.x, self.y)

class Path():
    """path"""

    def __init__(self, alt_grid: List[List[int]],
                    pos_start: Coord, pos_end: Coord) -> None:

        self.alt_grid = alt_grid
        self.pos_start = pos_start
        self.pos_end = pos_end

        self.pos_cur = pos_start.clone()

        self.step_dir_list: List[str] = []
        self.step_dir_grid: List[List[str]] = [
            (["."] * len(alt_grid[0])) for _ in range(len(alt_grid))
        ]

    def clone(self):
        """clone"""

        path = Path(self.alt_grid, self.pos_start, self.pos_end)

        path.pos_cur = self.pos_cur.clone()

        for step_dir in self.step_dir_list:
            path.step_dir_list.append(step_dir)

        for grid_y in range(len(self.step_dir_grid[0])):
            for grid_x in range(len(self.step_dir_grid)):
                path.step_dir_grid[grid_x][grid_y] = self.step_dir_grid[grid_x][grid_y]

        return path

    def get_dist(self) -> int:
        """get distance from current pos to end"""

        # dist_2d_max = Coord(0, 0).get_delta(Coord(len(self.alt_grid[0]), len(self.alt_grid)))
        # dist_alt_max = get_char_alt('z') - get_char_alt('a')
        # dist_max = dist_2d_max + dist_alt_max * dist_alt_max

        dist_2d = self.pos_cur.get_dist(self.pos_end)
        delta_alt = (self.alt_grid[self.pos_end.x][self.pos_end.y] -
            self.alt_grid[self.pos_cur.x][self.pos_cur.y])
        dist = dist_2d + int(math.sqrt(delta_alt))

        return dist

    def step(self, step_dir: str) -> bool:
        """step"""

        delta_coord = Coord(0, 0)
        step_char = ' '

        if step_dir == 'l':
            delta_coord.x = -1
            step_char = '<'
        elif step_dir == 'r':
            delta_coord.x = +1
            step_char = '>'
        elif step_dir == 'u':
            delta_coord.y = -1
            step_char = '^'
        elif step_dir == 'd':
            delta_coord.y = +1
            step_char = 'v'

        pos_new = Coord(self.pos_cur.x + delta_coord.x, self.pos_cur.y + delta_coord.y)

        if (pos_new.x < 0 or pos_new.x >= len(self.alt_grid) or
                pos_new.y < 0 or pos_new.y >= len(self.alt_grid[0])):
            # Out of bounds
            return False

        if self.step_dir_grid[pos_new.x][pos_new.y] != '.':
            # Already stepped
            return False

        if (self.alt_grid[pos_new.x][pos_new.y] <=
                self.alt_grid[self.pos_cur.x][self.pos_cur.y] + 1):
            # At most one level higher
            self.step_dir_list.append(step_dir)
            self.step_dir_grid[self.pos_cur.x][self.pos_cur.y] = step_char
            self.pos_cur.x += delta_coord.x
            self.pos_cur.y += delta_coord.y
            return True

        return False

    def check_reach_end(self) -> bool:
        """check end reachedcomplete"""
        return self.pos_cur.x == self.pos_end.x and self.pos_cur.y == self.pos_end.y

    def print(self) -> None:
        """print"""

        # pos_cur = Coord(self.pos_start.x, self.pos_start.y)

        for grid_y in range(len(self.step_dir_grid[0])):
            for grid_x in range(len(self.step_dir_grid)):
                if (grid_x, grid_y) == (self.pos_cur.x, self.pos_cur.y):
                    printf("c")
                else:
                    printf("%c", self.step_dir_grid[grid_x][grid_y])
                    # printf(".")
            printf("\n")
        printf("\n")

        # for (grid_y, grid_line) in enumerate(self.alt_grid):
        #     for (grid_x, grid_char) in enumerate(grid_line):
        #         for step_dir in self.step_dir_list:
        #             if step_dir == "l":
        #                 printf("<")
        #                 pos_cur.x -= 1

def get_char_alt(char: str):
    """
    get altitude from char
    """

    if char == 'S':
        char = 'a'
    elif char == 'E':
        char = 'z'

    return ord(char) - ord('a')

# def insert_path(path_list: List[Path], path_insert: Path, path_insert_idx: int) -> None:
#     """insert path in list at index"""

#     for path_idx in range()

def insert_path_on_dist(path_list: List[Path], path_insert: Path) -> None:
    """insert path in list based on dist"""

    path_insert_dist = path_insert.get_dist()

    for (path_idx, path) in enumerate(path_list):
        if path_insert_dist < path.get_dist():
            # insert_path(path_list, path_insert, path_idx)
            path_list.insert(path_idx, path_insert)
            return

    path_list.append(path_insert)

def fork_and_step(path: Path, step_nb_max: int):
    """fork path into 4 childs and perform 1 step for each one"""

    step_cnt_min = 99999

    step_dir_list = ['l', 'r', 'u', 'd']

    # level = len(path.step_dir_list)
    # indent_str = ""
    # for _ in range(level):
    #     indent_str += "  "

    # printf("%sfork_and_step\n", indent_str)
    # printf("%slevel = %u\n", indent_str, level)
    path.print()
    printf("dist = %u\n", path.get_dist())
    # input()

    path_child_list = [(path.clone()) for _ in range(len(step_dir_list))]
    path_child_list_continue: List[Path] = []

    for (path_child_idx, path_child) in enumerate(path_child_list):

        # printf("%slevel = %u\n", indent_str, level)
        # printf("%sstep dir = %s\n", indent_str, step_dir)
        # input()

        step_dir_idx = random.randint(0, len(step_dir_list) - 1)
        step_dir = step_dir_list[step_dir_idx]
        step_dir_list.remove(step_dir)

        stepped = path_child.step(step_dir)
        if stepped:
            # printf("%sstepped\n", indent_str)

            step_cnt = len(path_child.step_dir_list)

            if path_child.check_reach_end():
                printf("end reached in %u steps\n", step_cnt)
                return step_cnt

            if step_cnt >= step_nb_max:
                printf("aleady too long\n")
                return step_cnt

            # # printf("fork and step\n")
            # step_cnt = fork_and_step(path_child, step_nb_max)
            # if step_cnt and step_cnt < step_cnt_min:
            #     step_cnt_min = step_cnt

            insert_path_on_dist(path_child_list_continue, path_child)

        else:
            # printf("%sstuck\n", indent_str)
            # path.print()
            # path_child_alt_list[path_child_idx] = -1
            pass

    for (path_child_idx, path_child) in enumerate(path_child_list_continue):

        # printf("fork and step\n")
        step_cnt = fork_and_step(path_child, step_nb_max)
        if step_cnt and step_cnt < step_cnt_min:
            step_cnt_min = step_cnt


    # printf("return None\n")
    return step_cnt_min

def solve(data: str):
    """
    Solve puzzle
    """

    data_grid = []
    for data_line in data.split('\n'):
        grid_line = []
        for data_char in data_line:
            grid_line.append(data_char)
        data_grid.append(grid_line)

    # for grid_line in data_grid:
    #     for grid_char in grid_line:
    #         printf("%c", grid_char)
    #     printf("\n")

    pos_start = Coord(0, 0)
    pos_end = Coord(0, 0)

    alt_grid = [([0] * len(data_grid)) for _ in range(len(data_grid[0]))]
    for (grid_y, grid_line) in enumerate(data_grid):
        for (grid_x, grid_char) in enumerate(grid_line):
            alt_grid[grid_x][grid_y] = get_char_alt(grid_char)
            if grid_char == 'S':
                pos_start.x = grid_x
                pos_start.y = grid_y
            elif grid_char == 'E':
                pos_end.x = grid_x
                pos_end.y = grid_y
    # print(alt_grid)

    # for grid_y in range(len(alt_grid[0])):
    #     for grid_x in range(len(alt_grid)):
    #         printf("%02d ", alt_grid[grid_x][grid_y])
    #     printf("\n")

    step_cnt_min = 99999
    path = Path(alt_grid, pos_start, pos_end)
    step_cnt = fork_and_step(path, step_cnt_min)
    if step_cnt and step_cnt < step_cnt_min:
        step_cnt_min = step_cnt

    printf("Best path length : %u steps\n", step_cnt_min)
    return step_cnt_min

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
