# https://adventofcode.com/2025/day/7
# direction DOWN
# when a splitter ^ is hit the beam is divided to two adjacent columns
# count the number of divisions.

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


def get_next_step_coordinates(current_row_path_coordinates: list):
    """ Get all the points for the next step. """
    next_step = []
    for next_step_point_coor in current_row_path_coordinates:
        next_step.append((next_step_point_coor[0] + 1, next_step_point_coor[1]))
    return next_step


def check_current_point(point):
    """ Check what is in the current point.
        True - emtpy space
        False - splitter
    """
    if point == '^':
        return False
    return True

def divide_beam(target_point_coor):
    """ Divide the beam to left and right column from the target point"""
    new_points_coor = []
    # go left if there is space (we are not in column 0)
    if target_point_coor[1] > 0:
        new_points_coor.append((target_point_coor[0], target_point_coor[1] - 1))
    # go right if there is space (we are not in the last column)2
    if target_point_coor[1] < len(my_input[0]) - 1:
        new_points_coor.append((target_point_coor[0], target_point_coor[1] + 1))
    return new_points_coor

beam_split_counter = 0
row = starting_point[0]
current_beam_coordinates = [starting_point]
while row + 1 < len(my_input):
    list_of_next_coordinates = get_next_step_coordinates(current_beam_coordinates)
    temp_list_of_next_coordinates = []
    for next_point_coor in list_of_next_coordinates:
        next_point = my_input[next_point_coor[0]][next_point_coor[1]]
        if check_current_point(next_point) == True:
            # empty space
            temp_list_of_next_coordinates.append(next_point_coor)
            my_input[next_point_coor[0]][next_point_coor[1]] = '|'
        else:
            # print(f'Divide the beam to left and right column, target point: {next_point_coor}')
            temp_list_of_next_coordinates.extend(divide_beam(next_point_coor))
            for temp_coor in temp_list_of_next_coordinates:
                my_input[temp_coor[0]][temp_coor[1]] = '|'
            beam_split_counter += 1

    current_beam_coordinates = list(set(temp_list_of_next_coordinates))
    row += 1


def pretty_print(input_grid):
    for row in input_grid:
        print(''.join(row))


pretty_print(my_input)
print(f'Beam was split {beam_split_counter} times.')
