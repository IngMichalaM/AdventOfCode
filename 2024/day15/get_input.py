""" Read the input and get
    - starting position of the robot
    - list of the coordinates (tuples) of the obstacles
    - size of the field/grid """

from typing import List, Tuple

with open("input/input_grid_test2.txt") as f:
    aoc_input = [line.strip('\n') for line in f.readlines()]

with open("input/input_direction_test2.txt") as f:
    directions_input = [line.strip('\n') for line in f.readlines()]
    directions_input = ''.join(directions_input)

# print(directions_input)
# print(f"len of the directions is {len(directions_input)}")
ROWS = len(aoc_input)
COLUMNS = len(aoc_input[0])


def get_locations(grid: List[str]):
    """ Return list of tuples with coordinates of the boxes, walls and the starting position of the robot
        x corresponds to columns, y to rows in the list of the coordinates of the area. """

    boxes = set()
    walls = set()
    robot = set()
    for row_index, row in enumerate(grid):
        for col_index, char in enumerate(row):
            if char == "O":
                boxes.add((col_index, row_index))
            elif char == "#":
                walls.add((col_index, row_index))
            elif char == '@':
                print(f"found the robot {col_index, row_index}")
                robot.add((col_index, row_index))

    return boxes, walls, robot


coor_boxes, coor_walls, coor_robot = get_locations(aoc_input)