# https://adventofcode.com/2025/day/7
#
# DO NOT KEEP ALL THE COORDINATES, BUT ONLY THE NUMBER OF TIMELINES IN THE POINTS
#
# direction DOWN
# when a splitter ^ is hit, the beam is divided to two adjacent columns
# count the number of timelines.

from collections import defaultdict

# with open("my_ex.txt") as f:
# with open("input_example.txt") as f:
with open("real_input.txt") as f:
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


timelines_counter = 0  # the current started timeline - counts how many timelines reached the end
timelines = defaultdict(int)  # current state of the universe
timelines[starting_point] = 1  # keep track of how many timelines are in each point

for row_counter in range(len(my_input)-1):
    timelines_next = defaultdict(int)  # the next state / line  of the universe
    for (row_coor, col_coor), count in timelines.items():
        # print(f'In the {row_counter}. row there are {count} timeline(s) at the point ({row_coor}, {col_coor})')
        next_point_coor = (row_coor + 1, col_coor)  # move down
        if check_point(my_input[next_point_coor[0]][next_point_coor[1]]):
            # print(f"""The next point ({next_point_coor[0]}, {next_point_coor[1]}) on the way is save,
            #         adding the "next point" to the timelines""")
            timelines_next[next_point_coor] += count  # defaultdict will handle the case of new point not existing yet
            # there might be multiple timelines going to the same point
        else:
            # print(f'Divide beam for ({next_point_coor[0]}, {next_point_coor[1]}).')
            divided_beam_coordinates = divide_beam(next_point_coor)
            for coor in divided_beam_coordinates:
                timelines_next[coor] += count

    timelines = timelines_next  # move to the next line

print(f'There are {sum(timelines.values())} timelines')

#
# def pretty_print(input_grid):
#     for row in input_grid:
#         print(''.join(row))
#
# pretty_print(my_input)
