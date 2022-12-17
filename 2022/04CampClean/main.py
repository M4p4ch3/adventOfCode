#!/usr/bin/env python

"""
Advent of code 2022
Day 4: Camp Cleanup
https://adventofcode.com/2022/day/4
"""

class SectionRange():
    """
    Section range
    """

    def __init__(self, idx_start, idx_end) -> None:
        self.idx_start = idx_start
        self.idx_end = idx_end

    def print(self):
        """
        Print
        """
        print(self.get_str())

    def get_str(self) -> str:
        """
        Get string representation

        Returns:
            str: String representation
        """
        return f"{self.idx_start}-{self.idx_end}"

    def check_overlap(self, section_range) -> bool:
        """
        Check if overlaps with other section range

        Args:
            section_range (SectionRange): Other section range to check overlap with

        Returns:
            bool: Section ranges overlapping status
        """

        if (self.idx_start >= section_range.idx_start and
            self.idx_start <= section_range.idx_end):

            return True

        if (self.idx_end <= section_range.idx_end and
            self.idx_end >= section_range.idx_start):

            return True

        if (self.idx_start <= section_range.idx_start and
            self.idx_end >= section_range.idx_end):

            return True

        return False

def main():
    """
    Main
    """

    overlap_cnt = 0

    with open("input.txt", "r", encoding="utf8") as file:

        data = file.read()

        for line in data.split('\n'):

            section_range_0 = SectionRange(
                int(line.split(',')[0].split('-')[0]),
                int(line.split(',')[0].split('-')[1]))

            section_range_1 = SectionRange(
                int(line.split(',')[1].split('-')[0]),
                int(line.split(',')[1].split('-')[1]))

            # section_range_0.print()
            # section_range_1.print()

            if section_range_0.check_overlap(section_range_1):
                print(f"{section_range_0.get_str()} and {section_range_1.get_str()} overlap")
                overlap_cnt += 1

    print(overlap_cnt)

if __name__ == "__main__":
    main()
