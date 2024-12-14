""" Read the input and get
    - starting position of the guard
    - list of the coordinates (tuples) of the obstacles
    - size of the field/grid """

from typing import List, Tuple

# with open("input/inputA.txt") as f:
with open("input/input_test.txt") as f:
    aoc_input = [line.strip('\n') for line in f.readlines()]

ROWS = len(aoc_input)
COLUMNS = len(aoc_input[0])


def find_starting_position(A: List[str], guard_pattern: str) -> List[int]:
    """ Find starting coordingates for the character 'guard_pattern' in the 'matrix' A.
        x coresponds to columns, y to rows in the list of the cooreinates of the area. """
    for r_count, current_row in enumerate(A):
        for c_count, c in enumerate(current_row):
            if c == guard_pattern:
                return [c_count, r_count]


guard_starting_position = find_starting_position(aoc_input, '^')


def get_obstacles(grid: List[str]) -> List[Tuple[int, int]]:
    """ Return list of tuples with coordinates of the obstacles
        x coresponds to columns, y to rows in the list of the cooreinates of the area. """

    obstacles = []
    for row_index, row in enumerate(grid):
        for col_index, char in enumerate(row):
            if char == "#":
                obstacles.append((col_index, row_index))

    return obstacles


obstacles = get_obstacles(aoc_input)
