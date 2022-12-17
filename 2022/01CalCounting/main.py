#!/usr/bin/env python

"""
Advent of code 2022
Day 01 : Calorie Counting
https://adventofcode.com/2022/day/1
"""

from typing import List

def insert_val_list(a_list: List[int], insert_idx: int, insert_val: int) -> List[int]:
    """
    Insert value in list at index

    Args:
        list (List[int]): List to insert into
        insert_idx (int): Index where to insert
        insert_val (int): Value to insert

    Returns:
        list (List[int]): Updated list
    """

    # print(a_list)
    # print(insert_val)

    list_idx = len(a_list) - 1
    while list_idx > insert_idx:
        a_list[list_idx] = a_list[list_idx - 1]
        list_idx -= 1

    a_list[insert_idx] = insert_val

    # print(a_list)
    # print()

    return a_list

def main():
    """
    Main
    """

    elf_cal_total = 0
    elf_cal_total_max_list = [0] * 3
    top_elves_cal_total_max = 0

    with open("input.txt", "r", encoding="utf8") as file:

        data = file.read()

        for line in data.split('\n'):

            if line != "":
                # New elf food item
                elf_cal_total += int(line)

            else:
                # End of elf food items

                for (elf_cal_total_max_idx, elf_cal_total_max
                    ) in enumerate(elf_cal_total_max_list):
                    if elf_cal_total > elf_cal_total_max:
                        elf_cal_total_max_list = insert_val_list(
                            elf_cal_total_max_list, elf_cal_total_max_idx, elf_cal_total)
                        break

                # Reset elf total cal for nex elf
                elf_cal_total = 0

    top_elves_cal_total_max = 0
    for elf_cal_total_max in elf_cal_total_max_list:
        top_elves_cal_total_max += elf_cal_total_max

    print(elf_cal_total_max_list)
    print(top_elves_cal_total_max)

if __name__ == "__main__":
    main()
