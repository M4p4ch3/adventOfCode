#!/usr/bin/env python

"""
Advent of code 2022
Day 06 : Tuning Trouble
https://adventofcode.com/2022/day/6
"""

from typing import List

BUF_LEN = 14

def check_dupl_char(buf: List) -> bool:
    """
    Check for dupl char in buf

    Args:
        buf (List): Buf to check for dupl char

    Returns:
        bool: True if dupl char in buf, False otherwise
    """

    for (char_idx, char) in enumerate(buf):

        for (char_idx_2, char_2) in enumerate(buf):

            if char_idx == char_idx_2:
                continue

            if char == char_2:
                return True

    return False

def main():
    """
    Main
    """

    with open("input.txt", "r", encoding="utf8") as file:

        char_list = file.read()

        char_idx = BUF_LEN - 1
        while char_idx < len(char_list):

            char_buf = char_list[char_idx - (BUF_LEN - 1):char_idx + 1]
            print(char_buf)

            if check_dupl_char(char_buf) is False:
                break

            char_idx += 1

        print(char_idx + 1)

if __name__ == "__main__":
    main()
