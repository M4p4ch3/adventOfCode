#!/usr/bin/env python

"""
Advent of code 2022
Day 10 : Cathode-Ray Tube
https://adventofcode.com/2022/day/10
"""

# Started   at 17:08
# Completed at 17:45

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

    # x_at_cycle[cycle_idx] = x reg val during cyle cycle_idx

    x_val = 1
    x_at_cycle = []

    data_line_list = data.split('\n')
    for data_line in data_line_list:

        x_at_cycle.append(x_val)

        if data_line.startswith("addx "):
            x_at_cycle.append(x_val)
            x_val += int(data_line[len("addx "):])

    print(x_at_cycle)

    sig_strenght_sum = 0
    for cycle_idx in range(20 - 1, 220 + 40 - 1, 40):
        sig_strenght = x_at_cycle[cycle_idx] * cycle_idx
        sig_strenght_sum += sig_strenght
        # printf("cycle_idx=%u : x=%u sig_strenght=%u\n",
        #     cycle_idx, x_at_cycle[cycle_idx], sig_strenght)

    # printf("sig_strenght_sum=%u\n", sig_strenght_sum)

    pix_idx = 0
    for cycle_idx in range(0, len(x_at_cycle), 1):

        if pix_idx in range(x_at_cycle[cycle_idx] - 1, x_at_cycle[cycle_idx] + 2):
            printf("#")
        else:
            printf(".")

        if (pix_idx + 1) % 40 == 0:
            pix_idx = -1
            printf("\n")

        pix_idx += 1

    printf("\n")

    return sig_strenght_sum

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
