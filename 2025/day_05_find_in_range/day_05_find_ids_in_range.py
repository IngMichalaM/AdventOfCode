# https://adventofcode.com/2025/day/5
# TODO - optimisation 1 - merge overlaping ranges (however, it is enough when the ID is found in one of the ranges
#  so no need to check the rest when found one suitable range

with open("input_part1.txt") as f:
    my_input = [line.strip('\n') for line in f.readlines()]


def is_fresh(food_id: int, list_of_ranges) -> bool:
    """ Given a number (food_id, integer), check whether it is in any of the ranges provided in list_of_ranges.
        Each range is a tuple (start, end), inclusive.
    """
    for range_start, range_end in list_of_ranges:
        if range_start <= food_id <= range_end:
            return True
    return False


list_of_ranges = []
list_of_ids = []

for line in my_input:
    food_range = my_input.pop(0)

    if food_range == '':
        break

    range_start, range_end = map(int, food_range.split('-'))
    list_of_ranges.append((range_start, range_end))

for food in my_input:
    food_id = int(food)
    if is_fresh(food_id, list_of_ranges):
        list_of_ids.append(food_id)

print(f'There are {len(list_of_ids)} fresh foods.')
