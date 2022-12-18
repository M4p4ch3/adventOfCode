#!/usr/bin/env python

"""
Advent of code 2022
Day 13 : Distress signal
https://adventofcode.com/2022/day/13
"""

# Started   at 14:10
# Completed at TODO

import argparse
import sys
from typing import List

def printf(fmt_str, *args):
    """
    C like printf
    """

    sys.stdout.write(fmt_str % args)

def parse_list(list_str: str) -> List:
    """parse list"""

    list_str = list_str[1:-1]
    list_ret = []

    list_str_idx = 0
    while list_str_idx < len(list_str):

        char = list_str[list_str_idx]

        if ord(char) in range(ord('0'), ord('9') + 1):

            list_str_idx_int_start = list_str_idx
            list_str_idx += 1

            while list_str_idx < len(list_str):

                char = list_str[list_str_idx]
                if ord(char) not in range(ord('0'), ord('9') + 1):
                    break

                list_str_idx += 1

            item_int = int(list_str[list_str_idx_int_start:list_str_idx])
            list_ret.append(item_int)

        elif char == '[':

            list_str_idx_list_start = list_str_idx
            list_str_idx += 1

            level = 0
            while list_str_idx < len(list_str):

                char = list_str[list_str_idx]
                if char == '[':
                    level += 1
                elif char == ']':
                    if level == 0:
                        break
                    level -= 1

                list_str_idx += 1

            list_nested = parse_list(list_str[list_str_idx_list_start:list_str_idx + 1])
            list_ret.append(list_nested)

        list_str_idx += 1

    return list_ret

def compare_lists(list_left: List, list_right: List, level: int = 0) -> int:
    """compare lists
    return left - right"""

    indent_str = ""
    for _ in range(level):
        indent_str += "  "

    # printf("%scompare %s vs %s\n", indent_str, list_left, list_right)
    # input()

    for (item_left, item_right) in zip(list_left, list_right):

        if isinstance(item_left, int) and isinstance(item_right, int):
            # printf("%scompare %u vs %u\n", indent_str, item_left, item_right)
            ret = item_left - item_right

        else:

            if isinstance(item_left, int):
                item_left = [item_left]
            elif isinstance(item_right, int):
                item_right = [item_right]

            ret = compare_lists(item_left, item_right, level + 1)

        if ret != 0:
            # printf("%sreturn %d\n", indent_str, ret)
            return ret

    # printf("%scompare lists lengths %u vs %u\n", indent_str, len(list_left), len(list_right))
    ret = len(list_left) - len(list_right)
    if ret != 0:
        # printf("%sreturn %d\n", indent_str, ret)
        return ret

    # printf("%sreturn 0\n", indent_str)
    return 0

def solve(data: str):
    """
    Solve puzzle
    """

    packet_list = []

    for data_line in data.split("\n"):

        if data_line == "":
            continue

        packet = parse_list(data_line)
        packet_list.append(packet)

    packet_list.append([[2]])
    packet_list.append([[6]])

    packet_idx = 0
    while packet_idx < len(packet_list):

        packet_idx_2 = 0
        while packet_idx_2 < len(packet_list) - 1 - packet_idx:

            packet = packet_list[packet_idx_2]
            packet_next = packet_list[packet_idx_2 + 1]

            if compare_lists(packet, packet_next) > 0:
                packet_list.remove(packet_next)
                packet_list.insert(packet_idx_2, packet_next)

            packet_idx_2 += 1

        packet_idx += 1

    decoder_key = 1
    packet_idx = 0
    while packet_idx < len(packet_list):

        print(packet_list[packet_idx])

        if packet_list[packet_idx] in [[[2]], [[6]]]:
            decoder_key *= (packet_idx + 1)

        packet_idx += 1

    return decoder_key

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
