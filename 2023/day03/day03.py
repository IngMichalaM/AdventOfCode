# find numbers that have a special character in their neighbourhood

from collections import defaultdict
import re

filename = 'input_test.txt'
# filename = 'input.txt'

with open(filename) as f:
    input = [line.strip('\n') for line in f.readlines()]

def map_loc_def_value():
    return False

map_loc_char = defaultdict(map_loc_def_value)

# get locations of special characters, store in a dictionary
for counter_line, line in enumerate(input):
    for counter_column, character in enumerate(line):
        if character not in '0123456789.' or character == '':
            current_coordinates = '-'.join(map(str, [counter_line, counter_column]))
            map_loc_char[current_coordinates] = True

def check_surrounding_locations(start_line_num: int, column_num: int, char_len: int):
    """ Start location of the character and it length len(459) = 3
        Returns True if the number on the current location should be counted because
                it IS adjacent  to any symbol"""

    for i_line in range(start_line_num - 1, start_line_num + 2):
        if i_line != -1:
            for j_column in range(column_num - 1, column_num + char_len + 1):
                if j_column != -1:
                    location_under_exploration = '-'.join(map(str, [i_line, j_column]))
                    if map_loc_char[location_under_exploration]:
                        return True
    return False


def find_num_in_line(line: str) -> list:
    """ Retrun list of numbers (str) in the given string. If none, return [] """
    return re.findall(r'\d+', line)


def find_location_of_numbers_on_the_line(line: str, str_num: str, start_point: int) -> [int, int]:
    """ Return start index of the given number and its length """
    return line.index(str_num, start_point), len(str_num)  # to avoid getting wrong 9 from ...259...9...


engine_schematic_sum = 0
for counter_lines, line in enumerate(input):
    nums_in_line = find_num_in_line(line)

    if nums_in_line:
        num_loc_start_search = 0
        for curr_num in nums_in_line:
            column_num, char_len = find_location_of_numbers_on_the_line(line, curr_num, num_loc_start_search)
            num_loc_start_search = column_num + char_len
            if check_surrounding_locations(counter_lines, column_num, char_len):
                engine_schematic_sum += int(curr_num)

print(f'{engine_schematic_sum=}')