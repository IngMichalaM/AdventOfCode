# https://adventofcode.com/2025/day/7
#
# WORKS, BUT TOO COMPUTATIONALLY EXPENSIVE - NEEDS OPTIMIZATION
#
# direction DOWN
# when a splitter ^ is hit, the beam is divided to two adjacent columns
# count the number of timelines.

with open("my_ex.txt") as f:
# with open("input_example.txt") as f:
# with open("real_input.txt") as f:
    my_input = [list(line.strip('\n')) for line in f.readlines()]

# find starting point
starting_point = None
for r, row in enumerate(my_input):
    for c, char in enumerate(row):
        if char == 'S':
            starting_point = (r, c)
            break
    if starting_point is not None:
        break


def get_one_next_coordinate(one_point_coordinate: list):
    """ If the point is in the last row return the same point, else return the point in the next row """
    if one_point_coordinate[0] == len(my_input) - 1:
        return one_point_coordinate[0], one_point_coordinate[1]
    else:
        return one_point_coordinate[0] + 1, one_point_coordinate[1]


def check_point(point):
    """ Check what is in the given point.
        True - emtpy space
        False - splitter
    """
    if point == '^':
        return False
    return True


def divide_beam(target_point_coor):
    """ Divide the beam to left and right column from the target point """
    new_points_coor = []
    # go left if there is space (we are not in column 0)
    if target_point_coor[1] > 0:
        new_points_coor.append((target_point_coor[0], target_point_coor[1] - 1))
    # go right if there is space (we are not in the last column)2
    if target_point_coor[1] < len(my_input[0]) - 1:
        new_points_coor.append((target_point_coor[0], target_point_coor[1] + 1))
    return new_points_coor

timelines_counter = 0  # the current started timeline
row = starting_point[0]
timelines = [starting_point]  # we start with just one timeline, the one going down from 'S'
len_input = len(my_input)
while timelines:  # when the beam hits the last row of the grid, it will be removed from 'timelines' and counted to 'timelines_counter'
    print(f'All possible timelines in current time: {len(timelines)}')
    current_timeline = timelines.pop(0)
    next_coor = get_one_next_coordinate(current_timeline)
    if next_coor[0] >= len(my_input)-1:
        timelines_counter += 1
        continue

    if check_point(my_input[next_coor[0]][next_coor[1]]):
        timelines.append(next_coor)
    else:
        timelines.extend(divide_beam(next_coor))  # so in most cases we removed one point from 'timelines' and added two new timelines


print(f'There are {timelines_counter} timelines')


def pretty_print(input_grid):
    for row in input_grid:
        print(''.join(row))

pretty_print(my_input)