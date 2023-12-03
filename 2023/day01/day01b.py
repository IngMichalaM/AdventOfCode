# day 1, part 2 - find first and last number (can be written as word) in a string

import re

# filename = 'input_01b.txt'
filename = 'input.txt'

num_dict = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9", "0": "0",
            "1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9"}

with open(filename) as f:
    input = [line.strip('\n') for line in f.readlines()]

res_num = 0

for count, line in enumerate(input):
    first_run = True

    for key in num_dict:
        found_one = [m.start() for m in re.finditer(key, line)]

        for ind in found_one:
            # print(f"Index for {key} is {ind}")
            if first_run:
                first_run = False
                first_num = (ind, num_dict[key])
                last_num = (ind, num_dict[key])
            else:
                if ind < first_num[0]:
                    first_num = (ind, num_dict[key])
                elif ind > last_num[0]:
                    last_num = (ind, num_dict[key])

    # print(f"The final number for line {count} is {first_num[1]}{last_num[1]}")
    res_num += int(first_num[1]+last_num[1])

print(res_num)