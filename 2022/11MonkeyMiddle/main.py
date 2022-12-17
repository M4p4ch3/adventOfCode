#!/usr/bin/env python

"""
Advent of code 2022
Day 11 : Monkey in the Middle
https://adventofcode.com/2022/day/11
"""

# Started   at 15:40
# Completed at 16:50

import argparse
import sys
from typing import List

def printf(fmt_str, *args):
    """
    C like printf
    """

    sys.stdout.write(fmt_str % args)

class Monkey():

    def __init__(self, item_lvl_list, op_sign, op_operand, test_mod, dst_idx_true, dst_idx_false):
        self.item_lvl_list: List[int] = item_lvl_list
        self.op_sign: str = op_sign
        self.op_operand: int = op_operand
        self.test_mod: int = test_mod
        self.dst_idx_true: int = dst_idx_true
        self.dst_idx_false: int = dst_idx_false
        self.item_inspect_nb: int = 0

    def print(self):

        printf("  Items list : %s\n", self.item_lvl_list)
        printf("  Operation : new = old %c %u\n", self.op_sign, self.op_operand)
        printf("  Test : divisible by %u\n", self.test_mod)
        printf("    If true  : throw to monkey %u\n", self.dst_idx_true)
        printf("    If false : throw to monkey %u\n", self.dst_idx_false)

    def update_item_lvl(self, item_lvl: int) -> int:

        self.item_inspect_nb += 1

        if self.op_sign == "+":
            item_lvl += self.op_operand
        elif self.op_sign == "-":
            item_lvl -= self.op_operand
        elif self.op_sign == "*":
            item_lvl *= self.op_operand
        elif self.op_sign == "/":
            item_lvl = int(item_lvl / self.op_operand)
        elif self.op_sign == "^":
            item_lvl = pow(item_lvl, self.op_operand)

        item_lvl = int(item_lvl / 3)

        return item_lvl

    def check_test(self, item_lvl):

        return item_lvl % self.test_mod == 0

def solve(data: str):
    """
    Solve puzzle
    """

    line_list = data.split("\n")
    line_idx = 0
    monkey_idx = 0
    monkey_list: List[Monkey] = []

    for (line_idx, line) in enumerate(line_list):

        if line.startswith("Monkey "):

            line_idx += 1

            monkey_complete = False
            item_list = []
            op_sign = ""
            op_operand = 0
            test_mod = 0
            dst_idx_true = 0
            dst_idx_false = 0

            while not monkey_complete:

                line = line_list[line_idx]

                if line.startswith("  Starting items: "):
                    item_str_list = line[len("  Starting items: "):].split(", ")
                    item_list = []
                    for item in item_str_list:
                        item_list.append(int(item))

                elif line.startswith("  Operation: "):

                    op_sign = line[
                        len("  Operation: new = old "):len("  Operation: new = old ") + 1]
                    op_operand = line[len("  Operation: new = old + "):]

                    if op_operand == "old":
                        if op_sign == "+":
                            op_sign = "*"
                            op_operand = 2
                        elif op_sign == "*":
                            op_sign = "^"
                            op_operand = 2
                    else:
                        op_operand = int(op_operand)

                elif line.startswith("  Test: "):
                    test_mod = int(line[len("  Test: divisible by "):])

                elif line.startswith("    If true: "):
                    dst_idx_true = int(line[len("    If true: throw to monkey "):])

                elif line.startswith("    If false: "):
                    dst_idx_false = int(line[len("    If false: throw to monkey "):])
                    monkey_complete = True

                line_idx += 1

            monkey = Monkey(item_list, op_sign, op_operand, test_mod, dst_idx_true, dst_idx_false)
            monkey_list.append(monkey)
            monkey_idx += 1

        line_idx += 1

    # for (monkey_idx, monkey) in enumerate(monkey_list):
    #     printf("Monkey %u :\n", monkey_idx)
    #     monkey.print()

    round_cnt = 0
    while round_cnt < 20:

        for (monkey_idx, monkey) in enumerate(monkey_list):
            # printf("Monkey %u\n", monkey_idx)

            item_lvl = 0
            for item_lvl in monkey.item_lvl_list:
                # printf("  Monkey inspecst an item with a worry level of %u\n", item_lvl)

                item_lvl = monkey.update_item_lvl(item_lvl)
                # printf("    Worry level updated to %u\n", item_lvl)

                if monkey.check_test(item_lvl):
                    # printf("    Current worry level is divisble by %u\n", monkey.test_mod)
                    # printf("    Item with worry lelvel %u is sent o monkey %u\n",
                    #     item_lvl, monkey.dst_idx_true)
                    monkey_list[monkey.dst_idx_true].item_lvl_list.append(item_lvl)
                else:
                    # printf("    Current worry level is not divisble by %u\n", monkey.test_mod)
                    # printf("    Item with worry lelvel %u is sent o monkey %u\n",
                    #     item_lvl, monkey.dst_idx_false)
                    monkey_list[monkey.dst_idx_false].item_lvl_list.append(item_lvl)

            monkey.item_lvl_list.clear()

        # printf("After round %u :\n", round_cnt + 1)
        # for (monkey_idx, monkey) in enumerate(monkey_list):
        #     printf("  Monkey %u: %s\n", monkey_idx, monkey.item_lvl_list)

        round_cnt += 1

    def insert_at(item_list, item_val, item_idx):

        for idx in range(len(item_list) - 1, item_idx, -1):
            item_list[idx] = item_list[idx - 1]
        item_list[item_idx] = item_val

        return item_list

    item_inspect_nb_max_list = [0, 0]
    # printf("After round %u :\n", round_cnt + 1)
    for (monkey_idx, monkey) in enumerate(monkey_list):
        # printf("  Monkey %u: %s\n", monkey_idx, monkey.item_lvl_list)
        # printf("  Monkey %u inspected %u items\n", monkey_idx, monkey.item_inspect_nb)
        idx = 0
        while idx < len(item_inspect_nb_max_list):
            if monkey.item_inspect_nb > item_inspect_nb_max_list[idx]:
                item_inspect_nb_max_list = insert_at(
                    item_inspect_nb_max_list, monkey.item_inspect_nb, idx)
                break
            idx += 1

    # print(item_inspect_nb_max_list)
    monkey_business_lvl = 1
    for item_inspect_nb_max in item_inspect_nb_max_list:
        monkey_business_lvl *= item_inspect_nb_max

    return monkey_business_lvl

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
