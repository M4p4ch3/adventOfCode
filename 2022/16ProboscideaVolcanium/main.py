#!/usr/bin/env python

"""
Advent of code 2022
Day 16 : Proboscidea Volcanium
https://adventofcode.com/2022/day/16
"""

# Started   at 20:50
# Completed at 22:15

import argparse
import logging
import sys

from typing import List, Dict
import random
import re

g_logger = logging.getLogger("main")

def printf(fmt_str, *args):
    """
    C like printf
    """

    sys.stdout.write(fmt_str % args)

class Valve():
    """valve"""

    def __init__(self, name: str, flow_rate: int, tunnel_list: List[str]) -> None:

        self.name = name
        self.flow_rate = flow_rate
        self.tunnel_list = tunnel_list

        self.open = False

    def print(self):
        """print"""
        g_logger.debug("Valve")
        g_logger.debug("  name          = %s", self.name)
        g_logger.debug("  flow_rate     = %s", self.flow_rate)
        g_logger.debug("  tunnel_list   = %s", self.tunnel_list)

def browse_interactive(valve_dict: Dict[str, Valve]):
    """browse_interactive"""

    pressure_released = 0
    flow_rate = 0
    min_left = 30
    valve_cur = valve_dict["AA"]

    while min_left > 0:

        g_logger.debug("Minute %d", 30 - min_left + 1)
        g_logger.debug("  flow_rate         = %d", flow_rate)
        g_logger.debug("  pressure_released = %d", pressure_released)

        valve_cur.print()

        action_performed = False
        while not action_performed:
            action_str = input()
            if action_str == "o":
                if not valve_cur.open:
                    g_logger.debug("Open valve %s", valve_cur.name)
                    valve_cur.open = True
                    flow_rate += valve_cur.flow_rate
                    action_performed = True
                else:
                    g_logger.error("Valve %s already opened", valve_cur.name)
            elif action_str[0] == "m":
                if len(action_str) >= 3:
                    valve_dst = action_str[1:3]
                    if valve_dst in valve_cur.tunnel_list:
                        g_logger.debug("Move to valve %s", valve_dst)
                        valve_cur = valve_dict[valve_dst]
                        action_performed = True
                    else:
                        g_logger.error("Cant reach valve %s", valve_dst)
                else:
                    g_logger.error("Cant parse dst valve")
            elif action_str == "n":
                g_logger.debug("nop")
            else:
                g_logger.error("Unhandled command")

        pressure_released += flow_rate
        min_left -= 1

    return pressure_released

def browse(valve_dict: Dict[str, Valve]):
    """browse"""

    pressure_released = 0
    flow_rate = 0
    min_left = 30
    valve_cur = valve_dict["AA"]

    while min_left > 0:

        g_logger.debug("Minute %d", 30 - min_left + 1)
        g_logger.debug("  flow_rate         = %d", flow_rate)
        g_logger.debug("  pressure_released = %d", pressure_released)

        valve_cur.print()

        if valve_cur.open or valve_cur.flow_rate == 0:
            action = 1
        else:
            action = random.randint(0, 1)

        if action == 0:
            g_logger.debug("Open valve %s", valve_cur.name)
            valve_cur.open = True
            flow_rate += valve_cur.flow_rate
        else:
            dst_valve_idx = random.randint(0, len(valve_cur.tunnel_list) - 1)
            dst_valve_name = valve_cur.tunnel_list[dst_valve_idx]
            g_logger.debug("Move to valve %s", dst_valve_name)
            valve_cur = valve_dict[dst_valve_name]

        pressure_released += flow_rate
        min_left -= 1

    return pressure_released

def solve(data: str):
    """
    Solve puzzle
    """

    valve_dict: Dict[str, Valve] = dict()

    for data_line in data.split('\n'):

        match = re.match(
            r"""Valve ([A-Z]+) has flow rate=([0-9]+); """
            r"""tunnels? leads? to valves? ([, A-Z]+)""",
            data_line)

        if match:

            valve_name = match.group(1)
            valve_flow_rate = int(match.group(2))
            valve_tunnel_list = match.group(3).split(", ")

            valve = Valve(valve_name, valve_flow_rate, valve_tunnel_list)
            # valve.print()

            valve_dict[valve_name] = valve

    pressure_released_max = 0
    for _ in range(1000):
        pressure_released = browse(valve_dict)
        if pressure_released > pressure_released_max:
            pressure_released_max = pressure_released

    return pressure_released_max

def main():
    """
    Main
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("file_name_in", type=str, action="store",
        default="input.txt", help="input file name")
    parser.add_argument("-d", "--debug", action="store_true", help="enable debug log")
    args = parser.parse_args()

    log_fmt = "[%(levelname)-5s] (%(name)s) %(message)s"
    logging.basicConfig(format=log_fmt, level=logging.INFO)
    if args.debug:
        g_logger.setLevel(logging.DEBUG)

    data_in = ""
    with open(args.file_name_in, "r", encoding="utf8") as file:
        data_in = file.read()

    ans = solve(data_in)
    g_logger.info("ans = %s", ans)

if __name__ == "__main__":
    main()
