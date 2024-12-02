""" Day 2 of Advent of Code
https://adventofcode.com/2024/day/2
 https://adventofcode.com/2024/day/2#part2

 A report (list of numbers) is save if:
    - all the numbers are either increasing or all decreasing.
    - any two adjacent numbers differ by at least one and at most three.
"""


def set_direction(a: int, b: int) -> int:
    """ if b > a - increasing - 1
        if a > b - decreasing - -1
        if a = b - steady - 0  """
    return 1 if b > a else -1 if a > b else 0


def keep_direction(a: int, b: int, direction: int) -> bool:
    """ if a > b and direction = -1 - return true """
    # divocina :-) return ((a > b) & (direction == -1)) | ((a < b) & (direction == 1))

    if a == b:
        return False
        # raise ValueError("A and B cannot equal - unsuported direction")
    elif not (direction == 1 or direction == -1):
        raise ValueError("Unsuported direction")
    elif a > b and direction == -1:
        return True
    elif a < b and direction == 1:
        return True
    else:
        return False


def level_difference(a: int, b: int) -> bool:
    """ The difference between two adjacent numbers must be smaller or equal to 3 """
    return abs(a-b) <= 3


# "input/input_test.txt"
with open("input/inputA.txt") as f:
    my_input_str = [line.strip('\n').split() for line in f.readlines()]

save_levels = 0
for index_line, line_str in enumerate(my_input_str):
    line_int = list(map(int, line_str))

    # if steady slope, do not evaluate this line at all
    direction = set_direction(line_int[0], line_int[1])
    if direction == 0:
        continue

    for index, first_value in enumerate(line_int[:-1]):
        second_value = line_int[index+1]

        # if the adjacent numbers keep the direction - ok
        is_direction_ok = keep_direction(first_value, second_value, direction)
        if not is_direction_ok:
            break

        # if the distance from the two adjacent numbers is not greater than 3 - ok
        is_level_difference_ok = level_difference(first_value, second_value)
        if not is_level_difference_ok:
            break
    else:
        save_levels += 1

print(f"There are in total {save_levels} save levels.")