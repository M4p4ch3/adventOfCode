#!/usr/bin/env python

"""
Advent of code 2022
Day 07 : No Space Left On Device
https://adventofcode.com/2022/day/7
"""

import re

class File():

    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size
        self.dir_parent = None

    def print(self, indent: int = 0):

        for _  in range(0, indent, 1):
            print("  ", end="")

        print(f"- {self.name} (file, size={self.size})")

class Dir():

    def __init__(self, name: str) -> None:
        self.name = name
        self.dir_parent = None
        self.dir_list = []
        self.file_list = []

    def get_child(self, dir_name: str):

        for dir in self.dir_list:
            if dir.name == dir_name:
                return dir

        return None

    def get_size(self) -> int:

        size = 0

        for dir in self.dir_list:
            size += dir.get_size()

        for file in self.file_list:
            size += file.size

        return size

    def add_dir(self, dir):

        for dir_child in self.dir_list:
            if dir_child.name == dir.name:
                return

        self.dir_list.append(dir)
        dir.dir_parent = self

    def add_file(self, file):

        for file_child in self.file_list:
            if file_child.name == file.name:
                return

        self.file_list.append(file)
        file.dir_parent = self

    def print(self, indent: int = 0):

        for _  in range(0, indent, 1):
            print("  ", end="")

        print(f"- {self.name} (dir, size={self.get_size()})")

        for dir in self.dir_list:
            dir.print(indent + 1)

        for file in self.file_list:
            file.print(indent + 1)

def cd_parent(pwd: str) -> str:

    if pwd == "/":
        return

    # Remove trailing /
    pwd = pwd[:-1]

    while pwd[len(pwd) - 1] != '/':
        pwd = pwd[:-1]

    return pwd

def get_dir_size_sum(dir: Dir, size_max):

    dir_size_sum = 0

    dir_size = dir.get_size()
    if dir_size <= size_max:
        dir_size_sum += dir_size

    for dir_child in dir.dir_list:
        dir_size_sum += get_dir_size_sum(dir_child, size_max)

    return dir_size_sum

def main():
    """
    Main
    """

    with open("input.txt", "r", encoding="utf8") as file:

        # pwd = "/"
        # dir_root = Dir("/")
        dir_cur = Dir("/")

        data = file.read()
        line_list = data.split('\n')

        line_idx = 0
        while line_idx < len(line_list):
            line_data = line_list[line_idx]

            # print(line_data)

            if line_data[0] == '$':

                if line_data[2:4] == "cd":

                    if line_data[5] == "/":
                        # pwd = "/"
                        # dir_cur = dir_root
                        while dir_cur.dir_parent is not None:
                            dir_cur = dir_cur.dir_parent

                    elif line_data[5:7] == "..":
                        # pwd = cd_parent(pwd)
                        dir_cur = dir_cur.dir_parent

                    else:
                        # pwd += line_data[5:] + '/'
                        dir_name = line_data[5:]
                        dir = Dir(dir_name)
                        dir_cur.add_dir(dir)
                        dir_cur = dir_cur.get_child(dir_name)

            else:

                if line_data[0:3] == "dir":
                    dir_name = line_data[4:]
                    dir = Dir(dir_name)
                    dir_cur.add_dir(dir)

                else:
                    match = re.search(r"([0-9]+) ([a-zA-Z\.]+)", line_data)
                    file_size = int(match.group(1))
                    file_name = match.group(2)
                    file = File(file_name, file_size)
                    dir_cur.add_file(file)

            line_idx += 1

            # print(f"DEBUG pwd={pwd}")
            # print(f"DEBUG dir_cur.name={dir_cur.name}")
            # print("DEBUG dir_cur")
            # dir_cur.print()
            # print("DEBUG dir_root")
            # dir_tmp = dir_cur
            # while dir_tmp.dir_parent is not None:
            #     dir_tmp = dir_tmp.dir_parent
            # dir_tmp.print()

        dir_tmp = dir_cur
        while dir_tmp.dir_parent is not None:
            dir_tmp = dir_tmp.dir_parent
        dir_tmp.print()

        dir_size_sum = get_dir_size_sum(dir_tmp, 100000)
        print(dir_size_sum)


if __name__ == "__main__":
    main()
