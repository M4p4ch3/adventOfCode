#!/usr/bin/env python

"""
Advent of code 2022
Day 14 : Regolith Reservoir
https://adventofcode.com/2022/day/14
"""

# Started   at 20:45
# Completed at 21:45

import argparse
from typing import List
import sys

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

    def clone(self):
        """clone"""
        return Coord(self.x, self.y)

class Path():
    """path
    string of lines"""

    def __init__(self) -> None:
        self.point_list: List[Coord] = []

    def add_point(self, point: Coord):
        """add point"""
        self.point_list.append(point)

class Grid():
    """grid"""

    def __init__(self, size_x: int, size_y: int, start_x: int, start_y: int) -> None:
        self.grid = [(["."] * size_y) for _ in range(size_x)]
        self.start_x = start_x
        self.start_y = start_y

    def add_path(self, path: Path):
        """add path"""

        for point_idx in range(len(path.point_list) - 1):

            point = path.point_list[point_idx]
            point_next = path.point_list[point_idx + 1]

            if point.x == point_next.x:
                way = int((point_next.y - point.y) / abs(point.y - point_next.y))
                for point_y in range(point.y, point_next.y + way, way):
                    # printf("x=%u y=%u\n", point.x, point_y)
                    self.grid[point.x - self.start_x][point_y - self.start_y] = "#"
            else: # y == next y
                way = int((point_next.x - point.x) / abs(point.x - point_next.x))
                for point_x in range(point.x, point_next.x + way, way):
                    self.grid[point_x - self.start_x][point.y - self.start_y] = "#"

    def pour_sand(self):
        """pour 1 unit of sand"""

        sand_coord = Coord(500 - self.start_x, 0)
        y = sand_coord.y

        while y + 1 < len(self.grid[0]):

            while y + 1 < len(self.grid[0]) and self.grid[sand_coord.x][y + 1] == ".":
                y += 1

            if y + 1 >= len(self.grid[0]):
                return False

            if self.grid[sand_coord.x - 1][y + 1] == ".":
                sand_coord.x -= 1
                y += 1
            elif self.grid[sand_coord.x + 1][y + 1] == ".":
                sand_coord.x += 1
                y += 1
            else:
                break

        self.grid[sand_coord.x][y] = "o"
        return True

    def print(self):
        """print"""

        for y in range(len(self.grid[0])):
            for x in range(len(self.grid)):

                printf("%c", self.grid[x][y])

            printf("\n")

def solve(data: str):
    """
    Solve puzzle
    """

    grid = Grid(540 - 470 + 5, 180 + 1, 470, 0)

    for data_line in data.split('\n'):

        path = Path()

        for line_point_str in data_line.split(" -> "):

            line_point_coord_list = line_point_str.split(',')
            line_point_coord = Coord(int(line_point_coord_list[0]), int(line_point_coord_list[1]))
            path.add_point(line_point_coord)

        grid.add_path(path)

    grid.print()

    sand_unti_cnt = 0
    while True:

        rested = grid.pour_sand()
        if not rested:
            break

        sand_unti_cnt += 1

    grid.print()

    return sand_unti_cnt

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
