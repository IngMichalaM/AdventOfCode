# Solution for Day 03 Part 1
# https://adventofcode.com/2024/day/3

import re

# with open("input/inputA.txt", "r") as file:
with open("input/input_test.txt", "r") as file:
    content = file.read()  # Read the entire file

match_mull = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', content)
print(f'The result is: {sum([int(x) * int(y) for x, y in match_mull])}')
