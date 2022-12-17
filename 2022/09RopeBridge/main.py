#!/usr/bin/env python

"""
Advent of code 2022
Day 09 : Rope Bridge
https://adventofcode.com/2022/day/9
"""

# Started   at 08:48
# Completed at 09:30

import argparse
import logging

g_logger = logging.getLogger("main")

def show(head_coord, tail_coord):
    """
    Show
    """

    grid_h = 10 + 1
    grid_l = 10 + 1

    grid_y = -(grid_h - 1) / 2
    while grid_y <= (grid_h - 1) / 2:

        grid_x = -(grid_l - 1) / 2
        while grid_x <= (grid_l - 1) / 2:

            if [grid_x, grid_y] == tail_coord and tail_coord != head_coord:
                print("T", end="")
            elif [grid_x, grid_y] == head_coord:
                print("H", end="")
            elif [grid_x, grid_y] == [0, 0]:
                print("s", end="")
            else:
                print(".", end="")
            grid_x += 1

        print()
        grid_y += 1

def move_tail_to_head(head_coord, tail_coord):
    """
    Check tail more than 1 step away from head
    """

    for coord_idx in range(0, 2, 1):

        if abs(tail_coord[coord_idx] - head_coord[coord_idx]) > 1:
            if tail_coord[coord_idx] < head_coord[coord_idx]:
                tail_coord[coord_idx] += 1
            else:
                tail_coord[coord_idx] -= 1
            # Ensure aligned
            tail_coord[1 - coord_idx] = head_coord[1 - coord_idx]

    return tail_coord

def add_tail_visit_hist(tail_coord, tail_coord_hist_list):
    """
    Add tail coord to visit history
    """

    in_list = False
    for tail_coord_hist in tail_coord_hist_list:
        if (tail_coord[0] == tail_coord_hist[0] and
            tail_coord[1] == tail_coord_hist[1]):
            in_list = True
            break

    if not in_list:
        tail_coord_hist_list.append([tail_coord[0], tail_coord[1]])

    return tail_coord_hist_list

def solve(data: str) -> str:
    """
    Solve puzzle

    Args:
        data (str): Puzzle input data

    Returns:
        str: Puzzle answer
    """

    ret = 0

    head_coord = [0, 0]
    tail_coord = [0, 0]
    # g_logger.debug("head grid_x=%d grid_y=%d", head_x, head_y)
    # g_logger.debug("tail grid_x=%d grid_y=%d", head_x, head_y)
    tail_coord_hist_list = [[0, 0]]

    for line in data.split('\n'):

        direction = line[0]
        dist = int(line[2:])

        # g_logger.debug("%u steps %c", dist, direction)
        # g_logger.debug("before")
        # show(head_coord, tail_coord)
        # print()

        (d_x, d_y) = (0, 0)
        if direction == "L":
            d_x = -1
        elif direction == "R":
            d_x = 1
        elif direction == "U":
            d_y = -1
        elif direction == "D":
            d_y = 1

        for _ in range(0, dist, 1):

            head_coord[0] += d_x
            head_coord[1] += d_y

            tail_coord = move_tail_to_head(head_coord, tail_coord)
            add_tail_visit_hist(tail_coord, tail_coord_hist_list)

            # show(head_coord, tail_coord)
            # print()
            # input()

        # g_logger.debug("after")
        # show(head_coord, tail_coord)
        # print()
        # input()

        # print(tail_coord_hist_list)

    # print(tail_coord_hist_list)
    ret = str(len(tail_coord_hist_list))

    return ret

def main():
    """
    Main
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("file_name_in", type=str, action="store",
        default="input.txt", help="input file name")
    parser.add_argument("-a", "--ans_exp", type=str, action="store", help="expected answer")
    parser.add_argument("-v", "--verbose", action="store_true", help="log level verbose")
    args = parser.parse_args()

    log_fmt = "[%(levelname)-5s] (%(name)s) %(message)s"
    logging.basicConfig(format=log_fmt, level=logging.INFO)
    if args.verbose:
        g_logger.setLevel(logging.DEBUG)

    data_in = ""
    with open(args.file_name_in, "r", encoding="utf8") as file:
        data_in = file.read()

    ans = solve(data_in)
    g_logger.info("Answer = %s", ans)

    if args.ans_exp:
        if ans == args.ans_exp:
            g_logger.info("PASSED")
        else:
            g_logger.error("FAILED")

if __name__ == "__main__":
    main()
