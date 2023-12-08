import re
from itertools import cycle
from math import lcm

map_guide = 'LR'

with open("input_test.txt") as f:
    input = [line.strip('\n') for line in f.readlines()]

my_map = dict()
pattern = r'[=,]'
starting_points = []
for line in input:
    my_key, val1, val2 = re.split(pattern, line)
    my_key = my_key.strip()
    my_map[my_key] = [val1.strip(' ( '), val2.strip(' ) ')]

    if my_key[-1] == 'A':
        starting_points.append(my_key)

gen = cycle(map_guide)
all_res = []
for i in starting_points:
    current_key = i
    counter = 0

    while True:
        counter = counter + 1
        instruction = next(gen)

        LR = 0 if instruction == 'L' else 1

        current_key = my_map[current_key][LR]

        if current_key[-1] == 'Z':
            all_res.append(counter)
            break

print(lcm(*all_res))