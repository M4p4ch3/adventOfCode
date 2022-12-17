#!/usr/bin/env python

"""
Advent of code 2021
Day 03 : Binary Diagnostic
https://adventofcode.com/2021/day/3
"""

# Started   at 14:39
# Completed at 14:xx

import argparse

def get_bit_cnt_list(data_list):
    """
    Get bit count list
    """

    line_len = len(data_list[0])

    bit_cnt_list = [0] * line_len
    for bit_idx in range(0, line_len, 1):
        for diag_line in data_list:
            bit_cnt_list[bit_idx] += diag_line[bit_idx]

    return bit_cnt_list

def get_bit_most_common(data_list, bit_idx):
    """
    Get most common bit at index of list
    """

    diag_bit_cnt_list = get_bit_cnt_list(data_list)

    if diag_bit_cnt_list[bit_idx] >= len(data_list) / 2:
        return 1

    return 0

def get_dec_from_bit_list(bit_list) -> int:
    """
    Get decimal number from bit list
    """

    bit_list_len = len(bit_list)

    nb_dec = 0
    for bit_idx in range(0, bit_list_len, 1):
        if bit_list[bit_idx] == 1:
            nb_dec += pow(2, bit_list_len - bit_idx - 1)

    return nb_dec

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
        # print(diag_line)
    # print(diag_line_list)

    diag_line_len = len(diag_line_list[0])

    # print("oxygen generator list")
    oxy_gen_list = []
    for diag_line in diag_line_list:
        oxy_gen_list.append(diag_line)
        # print(diag_line)

    for diag_bit_idx in range(0, diag_line_len, 1):
        # print("diag_bit_idx=%u" % diag_bit_idx)

        if len(oxy_gen_list) <= 1:
            # print("only 1 item remaining")
            break

        bit_most_common = get_bit_most_common(oxy_gen_list, diag_bit_idx)
        # print("bit_most_common=%u" % bit_most_common)

        diag_line_idx = 0
        while diag_line_idx < len(oxy_gen_list):
            if oxy_gen_list[diag_line_idx][diag_bit_idx] != bit_most_common:
                oxy_gen_list.remove(oxy_gen_list[diag_line_idx])
            else:
                diag_line_idx += 1

        # print("oxygen generator list")
        # for diag_line in oxy_gen_list:
        #   print(diag_line)

    oxy_gen = get_dec_from_bit_list(oxy_gen_list[0])
    print("oxy_gen=%u" % oxy_gen)

    # print("co2 scrubber list")
    co2_scr_list = []
    for diag_line in diag_line_list:
        co2_scr_list.append(diag_line)
        # print(diag_line)

    for diag_bit_idx in range(0, diag_line_len, 1):
        # print("diag_bit_idx=%u" % diag_bit_idx)

        if len(co2_scr_list) <= 1:
            # print("only 1 item remaining")
            break

        bit_least_common = 1 - get_bit_most_common(co2_scr_list, diag_bit_idx)
        # print("bit_least_common=%u" % bit_least_common)

        diag_line_idx = 0
        while diag_line_idx < len(co2_scr_list):
            if co2_scr_list[diag_line_idx][diag_bit_idx] != bit_least_common:
                co2_scr_list.remove(co2_scr_list[diag_line_idx])
            else:
                diag_line_idx += 1

        # print("co2 scrubber list")
        # for diag_line in co2_scr_list:
        #     print(diag_line)

    co2_scr = get_dec_from_bit_list(co2_scr_list[0])
    print("co2_scr=%u" % co2_scr)

    return co2_scr * oxy_gen

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
