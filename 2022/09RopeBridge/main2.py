#!/usr/bin/env python

"""
Advent of code 2022
Day 09 : Rope Bridge
https://adventofcode.com/2022/day/9
"""

# Started   at 09:30
# Completed at 11:55

import argparse
import logging

g_logger = logging.getLogger("main")

def show(rope_coord_list):
    """
    Show
    """

    grid_h = 30 + 1
    grid_l = 50 + 1

    grid_y = -(grid_h - 1) / 2
    while grid_y <= (grid_h - 1) / 2:

        grid_x = -(grid_l - 1) / 2
        while grid_x <= (grid_l - 1) / 2:

            knot_present = False
            for knot_idx in range(0, len(rope_coord_list), 1):
                knot_coord = rope_coord_list[knot_idx]
                if [grid_x, grid_y] == knot_coord:
                    print(knot_idx, end="")
                    knot_present = True
                    break

            if not knot_present:
                if [grid_x, grid_y] == [0, 0]:
                    print("s", end="")
                else:
                    print(".", end="")

            grid_x += 1

        print()
        grid_y += 1

    print()
    input()

def move_knot_to_next(knot_prev_coord, knot_coord):
    """
    Move rope knot to previous one (in head direction)
    """

    delta = [0, 0]
    delta[0] = knot_prev_coord[0] - knot_coord[0]
    delta[1] = knot_prev_coord[1] - knot_coord[1]

    if delta[0] == 0 or delta[1] == 0:
        # If the head is ever two steps directly up, down, left, or right from the tail
        # the tail must also move one step in that direction so it remains close enough
        if abs(delta[0]) > 1:
            knot_coord[0] += delta[0] / abs(delta[0])
        elif abs(delta[1]) > 1:
            knot_coord[1] += delta[1] / abs(delta[1])
    elif abs(delta[0]) > 1 or abs(delta[1]) > 1:
        # Otherwise, if the head and tail aren't touching and aren't in the same row or column
        # the tail always moves one step diagonally to keep up
        knot_coord[0] += delta[0] / abs(delta[0])
        knot_coord[1] += delta[1] / abs(delta[1])

    return knot_coord

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

    knot_nb = 10
    rope_coord_list = []
    for _ in range(0, knot_nb, 1):
        rope_coord_list.append([0, 0])
    tail_coord_hist_list = [[0, 0]]


    for line in data.split('\n'):

        direction = line[0]
        dist = int(line[2:])

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

            rope_coord_list[0][0] += d_x
            rope_coord_list[0][1] += d_y

            for knot_idx in range(1, knot_nb, 1):
                rope_coord_list[knot_idx] = move_knot_to_next(
                    rope_coord_list[knot_idx - 1], rope_coord_list[knot_idx])

            add_tail_visit_hist(
                rope_coord_list[len(rope_coord_list) - 1], tail_coord_hist_list)

            show(rope_coord_list)

        # show(rope_coord_list)
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
