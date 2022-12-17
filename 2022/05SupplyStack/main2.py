#!/usr/bin/env python

"""
Advent of code 2022
Day 05 : Supply Stacks
https://adventofcode.com/2022/day/5
"""

import re

def main():
    """
    Main
    """

    with open("input.txt", "r", encoding="utf8") as file:

        data = file.read()
        line_list = data.split('\n')

        # Get index of line with stacks indexes
        stack_idx_line_idx = 0
        for (line_idx, line_data) in enumerate(line_list):
            print(line_data)
            if line_data == "":
                stack_idx_line_idx = line_idx - 1
                break

        # Get stack cnt
        stack_cnt = int(line_list[stack_idx_line_idx][len(line_list[stack_idx_line_idx]) - 2])
        print(f"stack_cnt={stack_cnt}")

        # Create stack list
        stack_list = [None] * stack_cnt
        for stack_idx in range(0, stack_cnt, 1):
            stack_list[stack_idx] = []
        print(stack_list)

        # Fill stack list with crates
        for line_idx in range(0, stack_idx_line_idx, 1):
            line_data = line_list[line_idx]
            # print(line_data)
            for stack_idx in range(0, stack_cnt, 1):
                crate = line_data[stack_idx * 4 + 1]
                # print(crate)
                if crate != ' ':
                    stack_list[stack_idx].insert(0, crate)
        print(stack_list)

        # Move crates
        for line_idx in range(stack_idx_line_idx + 2, len(line_list), 1):
            line_data = line_list[line_idx]
            print(line_data)
            match = re.search(r"move ([0-9]+) from ([0-9]+) to ([0-9]+)", line_data)
            crate_cnt = int(match.group(1))
            stack_idx_src = int(match.group(2)) - 1
            stack_idx_dst = int(match.group(3)) - 1

            stack_tmp = []
            for _ in range(0, crate_cnt, 1):
                stack_tmp.append(stack_list[stack_idx_src].pop())
            # print(stack_tmp)
            for _ in range(0, crate_cnt, 1):
                stack_list[stack_idx_dst].append(stack_tmp.pop())
            print(stack_list)
        # return

        # Get crates on top of each stack
        crate_list = ""
        for stack in stack_list:
            crate_list += str(stack[len(stack) - 1])
        print(crate_list)

if __name__ == "__main__":
    main()
