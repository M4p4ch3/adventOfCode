#!/usr/bin/env python

"""
Advent of code 2021
Day 03 : Binary Diagnostic
https://adventofcode.com/2021/day/3
"""

# Started   at 14:15
# Completed at 14:39

import argparse

def solve(data: str):
    """
    Solve puzzle

    Args:
        data (str): Puzzle input data

    Returns:
        str: Puzzle answer
    """

    diag_line_list = []
    for line in data.split('\n'):
        diag_line = []
        for bit in line:
            diag_line.append(int(bit))
        diag_line_list.append(diag_line)
    # print(diag_line_list)

    diag_line_len = len(diag_line_list[0])
    diag_bit_cnt_list = [0] * diag_line_len
    # print(diag_bit_cnt_list)

    for diag_bit_idx in range(0, diag_line_len, 1):
        for diag_line in diag_line_list:
            diag_bit_cnt_list[diag_bit_idx] += diag_line[diag_bit_idx]
    # print(diag_bit_cnt_list)

    gamma_rate_list = [0] * diag_line_len
    epsilon_rate_list = [1] * diag_line_len
    for diag_bit_idx in range(0, diag_line_len, 1):
        if diag_bit_cnt_list[diag_bit_idx] > len(diag_line_list) / 2:
            gamma_rate_list[diag_bit_idx] = 1
            epsilon_rate_list[diag_bit_idx] = 0
    print(gamma_rate_list)
    print(epsilon_rate_list)

    gamma_rate = 0
    epsilon_rate = 0
    for diag_bit_idx in range(0, diag_line_len, 1):
        if gamma_rate_list[diag_bit_idx] == 1:
            gamma_rate += pow(2, diag_line_len - diag_bit_idx - 1)
        if epsilon_rate_list[diag_bit_idx] == 1:
            epsilon_rate += pow(2, diag_line_len - diag_bit_idx - 1)
    print(gamma_rate)
    print(epsilon_rate)

    pwr_consum = gamma_rate * epsilon_rate

    return pwr_consum

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
    print("ans=%u" % ans)

if __name__ == "__main__":
    main()
