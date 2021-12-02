#!/usr/bin/env python3

# https://adventofcode.com/2021/day/2

import os
import sys

with open(os.path.join(sys.path[0], "input.txt"), "r") as file:
    lines = [line.rstrip("\n") for line in file]


def get_output_1(data):
    x = 0
    y = 0
    for instruction in data:
        (direction, value) = instruction.split()
        value = int(value)

        if direction == "forward":
            x += value
        elif direction == "down":
            y += value
        elif direction == "up":
            y -= value
    output = x * y
    print(f"part 1 output: {output}")


def get_output_2(data):
    x = 0
    y = 0
    aim = 0
    for instruction in data:
        (direction, value) = instruction.split()
        value = int(value)

        if direction == "forward":
            x += value
            y += aim * value
        elif direction == "down":
            aim += value
        elif direction == "up":
            aim -= value
    output = x * y
    print(f"part 2 output: {output}")


get_output_1(lines)
get_output_2(lines)
