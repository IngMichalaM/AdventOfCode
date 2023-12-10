import re
from itertools import cycle

map_guide = 'LR'

with open("input_test.txt") as f:
    input = [line.strip('\n') for line in f.readlines()]

my_map = dict()
pattern = r'[=,]'
for line in input:
    my_key, val1, val2 = re.split(pattern, line)
    my_map[my_key.strip()] = [val1.strip(' ( '), val2.strip(' ) ')]

gen = cycle(map_guide)
current_key = 'AAA'
counter = 0

while True:
    counter = counter + 1
    instruction = next(gen)

    LR = 0 if instruction == 'L' else 1

    current_key = my_map[current_key][LR]

    if current_key == 'ZZZ':
        print(counter)
        break
