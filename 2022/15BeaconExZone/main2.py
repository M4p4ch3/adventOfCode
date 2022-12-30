#!/usr/bin/env python

"""
Advent of code 2022
Day 15 : Beacon Exclusion Zone
https://adventofcode.com/2022/day/15
"""

# Started   at 14:15
# Paused    at 14:30

# Resumed   at 19:40
# Completed at 20:30

import argparse
import sys

import re
from typing import List, Tuple

DEBUG = False
# DEBUG = True

def printf(fmt_str, *args):
    """
    C like printf
    """

    sys.stdout.write(fmt_str % args)

def printf_dbg(fmt_str, *args):

    if DEBUG:
        sys.stdout.write(fmt_str % args)

def print_dbg(to_print):

    if DEBUG:
        print(to_print)

class Coord():

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

def add_range_list(x_range_list: List[List[int]], x_range_param: List[int], level: int = 0):

    x_range_param_start = x_range_param[0]
    x_range_param_end = x_range_param[1]
    idx = 0

    indent_str = ""
    for _ in range(level):
        indent_str += "  "

    printf_dbg("%sadd range %s to %s\n", indent_str, x_range_param, x_range_list)

    for idx in range(len(x_range_list)):

        x_range_cur_start = x_range_list[idx][0]
        x_range_cur_end = x_range_list[idx][1]

        if x_range_param_end >= x_range_cur_start and x_range_param_start <= x_range_cur_end:
            # overlap

            printf_dbg("%s[%d, %d] overlaps with [%d, %d]\n", indent_str,
                x_range_param_start, x_range_param_end, x_range_cur_start, x_range_cur_end)

            # get overlaping range
            x_range_overlap_start = x_range_list[idx][0]
            x_range_overlap_end = x_range_list[idx][1]

            # remove overlaping range
            x_range_list.remove(x_range_list[idx])

            # create new range by merging overlaping with param one
            x_range_overlap_start = min(x_range_overlap_start, x_range_param_start)
            x_range_overlap_end = max(x_range_overlap_end, x_range_param_end)

            printf_dbg("%screate new range [%d, %d]\n", indent_str,
                x_range_overlap_start, x_range_overlap_end)

            # add updated overlaping range back
            x_range_list = add_range_list(
                x_range_list, [x_range_overlap_start, x_range_overlap_end], level + 1)

            return x_range_list

    # doesnt overlap with any range
    printf_dbg("%s[%d, %d] doesnt overlap with any\n",
        indent_str, x_range_param_start, x_range_param_end)
    printf_dbg("%sappend range [%d, %d] to %s\n",
        indent_str, x_range_param_start, x_range_param_end, x_range_list)
    x_range_list += [[x_range_param_start, x_range_param_end]]
    printf_dbg("%sreturn updated range list = %s\n", indent_str, x_range_list)
    printf_dbg("\n")
    return x_range_list

class Grid():

    def __init__(self, coord_min: Coord, coord_max: Coord) -> None:

        self.coord_min = coord_min

        self.width = coord_max.x - coord_min.x + 1
        self.height = coord_max.y - coord_min.y + 1

        self.sensor_range_list: List[Tuple[Coord, int]] = []

    def add_sensor_beacon(self, sensor_coord: Coord, beacon_coord: Coord):

        # sensor to beacon dist
        dist_s_b = abs(beacon_coord.x - sensor_coord.x) + abs(beacon_coord.y - sensor_coord.y)

        self.sensor_range_list += [(sensor_coord, dist_s_b)]

    def get_no_beacon_x_range_list(self, y: int, x_min: int, x_max: int):

        no_beacon_x_range_list: List[List[int]] = []

        # dist from sensor to beacon
        for (sensor_coord, dist_s_b) in self.sensor_range_list:

            # dist from sensor to row
            dist_s_r = abs(sensor_coord.y - y)
            if dist_s_r > dist_s_b:
                continue

            x_range_cur_start = sensor_coord.x - (dist_s_b - dist_s_r)
            x_range_cur_end = sensor_coord.x + (dist_s_b - dist_s_r)

            if x_range_cur_start < x_min:
                x_range_cur_start = x_min
            if x_range_cur_end < x_min:
                x_range_cur_end = x_min

            if x_range_cur_start > x_max:
                x_range_cur_start = x_max
            if x_range_cur_end > x_max:
                x_range_cur_end = x_max

            if x_range_cur_start == x_min and x_range_cur_end == x_max:
                return [[x_min, x_max]]

            no_beacon_x_range_list = add_range_list(
                no_beacon_x_range_list, [x_range_cur_start, x_range_cur_end])

            if (len(no_beacon_x_range_list) == 1 and
                no_beacon_x_range_list[0][0] == x_min and no_beacon_x_range_list[0][1] == x_max):

                return no_beacon_x_range_list

        return no_beacon_x_range_list

    def get_possible_beacon_x(self, y: int, x_min: int, x_max: int):

        no_beacon_x_range_list = self.get_no_beacon_x_range_list(y, x_min, x_max)
        if (len(no_beacon_x_range_list) == 1 and
            no_beacon_x_range_list[0][0] == x_min and no_beacon_x_range_list[0][1] == x_max):

            return None

        print(no_beacon_x_range_list)

        if len(no_beacon_x_range_list) == 2:
            if no_beacon_x_range_list[0][1] < no_beacon_x_range_list[1][0]:
                return no_beacon_x_range_list[0][1] + 1
            if no_beacon_x_range_list[1][1] < no_beacon_x_range_list[0][0]:
                return no_beacon_x_range_list[1][1] + 1
            return -1

        if len(no_beacon_x_range_list) == 1:
            if no_beacon_x_range_list[0][1] < x_max:
                return x_max
            if no_beacon_x_range_list[0][0] > x_min:
                return x_min
            return -1

        return -1

def solve(data: str):
    """
    Solve puzzle
    """

    coord_min = Coord(100, 100)
    coord_max = Coord(0, 0)

    sensor_beacon_coord_list: List[Tuple[Coord, Coord]] = []

    for data_line in data.split('\n'):

        match = re.match(
            r"""Sensor at x=(\-?[0-9]+), y=(\-?[0-9]+): """
            r"""closest beacon is at x=(\-?[0-9]+), y=(\-?[0-9]+)""",
            data_line)

        if match:

            sensor_coord = Coord(int(match.group(1)), int(match.group(2)))
            beacon_coord = Coord(int(match.group(3)), int(match.group(4)))

            sensor_beacon_coord_list += [(sensor_coord, beacon_coord)]

            coord_min.x = min(coord_min.x, sensor_coord.x, beacon_coord.x)
            coord_min.y = min(coord_min.y, sensor_coord.y, beacon_coord.y)
            coord_max.x = max(coord_max.x, sensor_coord.x, beacon_coord.x)
            coord_max.y = max(coord_max.y, sensor_coord.y, beacon_coord.y)

    grid = Grid(coord_min, coord_max)

    for (sensor_coord, beacon_coord) in sensor_beacon_coord_list:
        grid.add_sensor_beacon(sensor_coord, beacon_coord)

    possible_beacon_y = 0
    possible_beacon_x = 0
    for possible_beacon_y in range(3363767 - 100000, 4000000):

        if possible_beacon_y % (4000000 / 100) == 0:
            printf("%d/100\n", possible_beacon_y * 100 / 4000000)

        possible_beacon_x = grid.get_possible_beacon_x(possible_beacon_y, 0, 4000000)
        if possible_beacon_x:
            if possible_beacon_x == -1:
                printf("ERROR unhandled possible beacon in row %d\n", possible_beacon_y)
                break
            possible_beacon_x = int(possible_beacon_x)
            break

    # y = 3363767
    # x = 3157535

    tuning_freq = 0
    if possible_beacon_x:
        if possible_beacon_x != -1:
            tuning_freq = possible_beacon_x * 4000000 + possible_beacon_y

    return tuning_freq

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
