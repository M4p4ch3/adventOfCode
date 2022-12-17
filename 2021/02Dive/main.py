#!/usr/bin/env python

"""
Advent of code 2021
Day 02 : Dive
https://adventofcode.com/2021/day/2
"""

# Started   at 14:05
# Completed at 14:10

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

    pos_hrz = 0
    pos_vrt = 0

    for line in data.split('\n'):

        if line.startswith("forward"):
            pos_hrz += int(line[len("forward "):])
        elif line.startswith("down"):
            pos_vrt += int(line[len("down "):])
        elif line.startswith("up"):
            pos_vrt -= int(line[len("up "):])

    ret = str(pos_hrz * pos_vrt)

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
