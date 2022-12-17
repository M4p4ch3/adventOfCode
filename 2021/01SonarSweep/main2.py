#!/usr/bin/env python

"""
Advent of code 2021
Day 01 : Sonar Sweep
https://adventofcode.com/2021/day/1
"""

# Started   at 13:48
# Completed at 14:02

import argparse
import logging

g_logger = logging.getLogger("main")

def solve(data: str) -> str:
    """
    Solve puzzle

    Args:
        data (str): Puzzle input data

    Returns:
        str: Puzzle answer
    """

    ret = ""

    meas_list = data.split('\n')
    meas_inc_cnt = 0

    # g_logger.debug("%u", meas_list[0])

    for meas_idx in range(1, len(meas_list) - 2, 1):

        meas_sum = 0
        for meas_off in range(0, 3, 1):
            meas_sum += int(meas_list[meas_idx + meas_off])

        meas_prev_sum = 0
        for meas_off in range(0, 3, 1):
            meas_prev_sum += int(meas_list[meas_idx - 1+ meas_off])

        if meas_sum > meas_prev_sum:
            g_logger.debug("%u (inc)", meas_sum)
            meas_inc_cnt += 1
        else:
            g_logger.debug("%u", meas_sum)

    ret = str(meas_inc_cnt)

    return ret

def main():
    """
    Main
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("file_name_in", type=str, action="store",
        default="input.txt", help="input file name")
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

if __name__ == "__main__":
    main()
