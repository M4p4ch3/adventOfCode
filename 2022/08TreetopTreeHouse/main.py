#!/usr/bin/env python

"""
Advent of code 2022
Day 08 : Treetop Tree House
https://adventofcode.com/2022/day/8
"""

# 20h40
# 21h05

def check_tree_visible(tree_height_grid, tree_x, tree_y) -> bool:

    tree_visible_left = True
    tree_visible_right = True
    tree_visible_up = True
    tree_visible_down = True

    line_cnt = len(tree_height_grid)
    row_cnt = len(tree_height_grid[0])

    tree_height = tree_height_grid[tree_x][tree_y]

    # For all trees at left
    for tree_next_x in range(0, tree_x, 1):
        if tree_height_grid[tree_next_x][tree_y] >= tree_height:
            tree_visible_left = False
            break

    # For all trees at right
    for tree_next_x in range(tree_x + 1, row_cnt, 1):
        if tree_height_grid[tree_next_x][tree_y] >= tree_height:
            tree_visible_right = False
            break

    # For all trees above
    for tree_next_y in range(0, tree_y, 1):
        if tree_height_grid[tree_x][tree_next_y] >= tree_height:
            tree_visible_up = False
            break

    # For all trees below
    for tree_next_y in range(tree_y + 1, line_cnt, 1):
        if tree_height_grid[tree_x][tree_next_y] >= tree_height:
            tree_visible_down = False
            break

    if (tree_visible_left is True or tree_visible_right is True or
        tree_visible_up is True or tree_visible_down is True):

        return True

    return  False

def main():
    """
    Main
    """

    tree_height_grid = None

    with open("input.txt", "r", encoding="utf8") as file:

        data = file.read()
        print(data)
        line_list = data.split('\n')
        row_cnt = len(line_list)
        line_cnt = len(line_list[0])

        # Init tree height grid
        tree_height_grid = [None] * row_cnt
        for row_idx in range(0, row_cnt, 1):
            tree_height_grid[row_idx] = [None] * line_cnt

        # Fill tree height grid
        for line_idx in range(0, line_cnt, 1):
            for row_idx in range(0, row_cnt, 1):
                tree_height_grid[row_idx][line_idx] = line_list[line_idx][row_idx]
        # print(tree_height_grid)

    tree_visible_cnt = 0
    for tree_x in range(0, line_cnt, 1):
        for tree_y in range(0, row_cnt, 1):
            if check_tree_visible(tree_height_grid, tree_x, tree_y) is True:
                tree_visible_cnt += 1

    print(tree_visible_cnt)

if __name__ == "__main__":
    main()
