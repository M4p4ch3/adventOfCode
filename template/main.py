#!/usr/bin/env python

"""
Advent of code TODO
Day TODO : TODO
https://adventofcode.com/TODO/day/TODO
"""

# Started   at TODO
# Completed at TODO

import argparse
import logging
import sys

g_logger = logging.getLogger("main")

def printf(fmt_str, *args):
    """
    C like printf
    """

    sys.stdout.write(fmt_str % args)

def solve(data: str):
    """
    Solve puzzle
    """

    return 0

def main():
    """
    Main
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("file_name_in", type=str, action="store",
        default="input.txt", help="input file name")
    parser.add_argument("-d", "--debug", action="store_true", help="enable debug log")
    args = parser.parse_args()

    log_fmt = "[%(levelname)-5s] (%(name)s) %(message)s"
    logging.basicConfig(format=log_fmt, level=logging.INFO)
    if args.debug:
        g_logger.setLevel(logging.DEBUG)

    data_in = ""
    with open(args.file_name_in, "r", encoding="utf8") as file:
        data_in = file.read()

    ans = solve(data_in)
    g_logger.info("ans = %s", ans)

if __name__ == "__main__":
    main()
