#!/usr/bin/env python3

# https://adventofcode.com/2021/day/3

import os
import sys

with open(os.path.join(sys.path[0], "input.txt"), "r") as file:
    lines = [line.rstrip("\n") for line in file]


def power_consumption(data):
    counts = [0] * len(data[0])
    for binary in data:
        for i, c in enumerate(binary):
            if c == '1':
                counts[i] += 1
    gamma_rate = 0
    epsilon_rate = 0
    for i in range(len(data[0])):
        gamma_rate <<= 1
        epsilon_rate <<= 1
        if counts[i] > len(data) // 2:
            gamma_rate += 1
        else:
            epsilon_rate += 1
    return gamma_rate * epsilon_rate


def get_output_1(data):
    print(f"part 1 output: {power_consumption(data)}")


def get_output_2(data):
    pass


get_output_1(lines)
get_output_2(lines)
