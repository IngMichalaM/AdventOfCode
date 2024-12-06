"""
Solution for Day 06 Part A
https://adventofcode.com/2024/day/6
"""

from typing import List

# with open("input/inputA.txt") as f:
with open("input/input_test.txt") as f:
    aoc_input = [list(line.strip('\n')) for line in f.readlines()]

ROWS = len(aoc_input)
COLUMNS = len(aoc_input[0])


def find_starting_position(A: List[List[str]], guard_pattern: str) -> List[int]:
    """ Find starting coordingates for the character 'guard_pattern' in the 'matrix' A. """
    for r_count, current_row in enumerate(A):
        for c_count, c in enumerate(current_row):
            if c == guard_pattern:
                return [r_count, c_count]


def take_right_turn(current_direction: List[int]) -> List[int]:
    """ Return the new direction after turning to the right from the current direction. """
    if current_direction == [-1, 0]:  # up
        return [0, 1]
    elif current_direction == [0, 1]:  # right
        return [1, 0]
    elif current_direction == [1, 0]:  # down
        return [0, -1]
    elif current_direction == [0, -1]:  # left
        return [-1, 0]
    else:
        raise ValueError("Unknown direction")


def nicely_display(a: List[List[str]]) -> None:
    """ Nicely displaye the input matrix (list o lists of strings) """
    for line in a:
        print(''.join(line))


direction = [-1, 0]  # start direction - upwards
r, c = find_starting_position(aoc_input, '^')  # rows, columns


def go_and_turn(direction, r, c, aoc_input, ROWS, COLUMNS):
    """ When the guard hits the obstacle, it turns to the right and go on.
        Stop counting when the guard leaves the room.  """
    positions_counter = 1

    # go on as long as you are in the room
    while 0 <= r < ROWS and 0 <= c < COLUMNS:
        # nicely_display(aoc_input)
        # input("Press Enter to continue...")

        aoc_input[r][c] = 'X'

        r_new = r + direction[0]
        c_new = c + direction[1]

        if 0 <= r_new < ROWS and 0 <= c_new < COLUMNS:
            if aoc_input[r_new][c_new] != '#':
                # we can go there
                r = r_new
                c = c_new

                # if we have been there, we can go there, but do not count it as a unique position
                if aoc_input[r_new][c_new] == '.':
                    # count it
                    positions_counter += 1

            else:
                direction = take_right_turn(direction)

        else:
            # we are out
            return positions_counter, aoc_input

res, a = go_and_turn(direction, r,c, aoc_input, ROWS, COLUMNS)
print(f"There has been {res} steps")