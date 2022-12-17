#!/usr/bin/env python

"""
Advent of code TODO
Day TODO : TODO
https://adventofcode.com/TODO/day/TODO
"""

# Started   at TODO
# Completed at TODO

import argparse
import sys

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
    args = parser.parse_args()

    data_in = ""
    with open(args.file_name_in, "r", encoding="utf8") as file:
        data_in = file.read()

    ans = solve(data_in)
    printf("ans=%u\n", ans)

if __name__ == "__main__":
    main()
