#!/usr/bin/env python

"""
Advent of code 2022
Day 03 : Rucksack Reorganization
https://adventofcode.com/2022/day/3
"""

def main():
    """
    Main
    """

    prio_total = 0

    with open("input.txt", "r", encoding="utf8") as file:

        data = file.read()
        line_list = data.split('\n')

        for line_list_idx in range(0, len(line_list), 3):

            elf_list_item_list = []
            for _ in range(0, 3, 1):
                elf_list_item_list.append([])

            for elf_idx in range(0, 3, 1):

                for item in line_list[line_list_idx + elf_idx]:

                    elf_list_item_list[elf_idx] += item

        # for item_list in data.split('\n'):

        #     item_list_idx = 0
        #     item_list_compart1 = []
        #     item_list_compart2 = []

        #     while item_list_idx < len(item_list) / 2:
        #         item_list_compart1 += item_list[item_list_idx]
        #         item_list_idx += 1

        #     while item_list_idx < len(item_list):
        #         item_list_compart2 += item_list[item_list_idx]
        #         item_list_idx += 1

            for item in elf_list_item_list[0]:
                if item in elf_list_item_list[1] and item in elf_list_item_list[2]:
                    # print(f"item {item} shared by elf 1, 2, and 3")
                    if ord(item) <= ord('Z'):
                        prio = ord(item) - ord('A') + 27
                    else:
                        prio = ord(item) - ord('a') + 1
                    # print(f"prio={prio}")
                    prio_total += prio
                    break

    print(prio_total)

if __name__ == "__main__":
    main()
