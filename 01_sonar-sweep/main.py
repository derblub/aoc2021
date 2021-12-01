#!/usr/bin/env python3

# https://adventofcode.com/2021/day/1

import os
import sys

with open(os.path.join(sys.path[0], "input.txt"), "r") as file:
    lines = [int(line.rstrip("\n")) for line in file]


def count_increase(data, steps=1):
    return sum(data[i] > data[i - steps] for i in range(steps, len(data)))


def get_output_1(data):
    print(f"part 1 output: {count_increase(data)}")

def get_output_2(data):
    print(f"part 2 output: {count_increase(data, 3)}")


get_output_1(lines)
get_output_2(lines)
