# https://adventofcode.com/2025/day/9
# There are some red tiles in the grid
# In between on the same line and/or column, they are green tiles (needs to be found)
# This creates a closed loop, inside is also full of green tiles
# Find the biggest rectangle that have two red tiles in the opposite corners and inside only green tiles

# Need to totally rethink the approach in comparison with Part 1. New approach:
# 1. Read red coordinates
# 2. Create a grid, place red tiles into it
# 3. Add green tiles to the loop
# 4. Find inner green area - "Flood fill" algorithm
# 5. Rectangle search


###########################################################################################
#                1. Read input and prepare red coordinates                                #
###########################################################################################
with open("input_example.txt") as f:
    my_input = [line.strip('\n') for line in f.readlines()]

coordinates = []
# Input coordinates are in matrix representation
# Modify to fit grid[row][column] representation
for coor in my_input:
    col_coor, row_coor = coor.split(',')
    coordinates.append((int(row_coor), int(col_coor)))


###########################################################################################
#                    Helper functions                                                     #
###########################################################################################
def pretty_print(grid, points=[], color='RED'):
    # ANSI escape codes for colors
    if color == 'RED':
        color_ansi = "\033[91m"
    elif color == 'YELLOW':
        color_ansi = "\033[93m"
    else:  # green
        color_ansi = "\033[92m"
    RESET = "\033[0m"

    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if (i, j) in points:
                print(f"{color_ansi}{val}{RESET}", end=" ")
            else:
                print(val, end=" ")
        print()


def mark_coordinates(grid, points, the_mark):
    for row, column in points:
        grid[row][column] = the_mark


###########################################################################################
#                    2. Create a grid, place red tiles into it                            #
###########################################################################################

# Find most outer red tiles --> size of the grid
# Add padding to the grid to avoid boundary issues
max_column = 0
max_row = 0

for red_row, red_column in coordinates:
    if red_column > max_column:
        max_column = red_column
    if red_row > max_row:
        max_row = red_row

# Create the grid with the padding
grid = []
for row in range(max_row + 3):
    line = []
    for col in range(max_column + 3):
        line.append('.')
    grid.append(line)

# Enhanced red coordinates with padding
enhanced_red_coordinates = []
for red_row, red_column in coordinates:
    enhanced_red_coordinates.append((red_row + 1, red_column + 1))

# Fill the grid with red tiles
mark_coordinates(grid, enhanced_red_coordinates, '#')


###########################################################################################
#                3. Add green tiles to the loop                                           #
###########################################################################################

def add_green_tiles(point_1, point_2):
    """ From the definition, the coordinates are in order.
        Find out if the two points are in the same line or column.
        if yes, fill the gap with green tiles (add the coordinates to green list)
    """
    new_green_tiles = []
    new_green_tiles_columns = []
    new_green_tiles_rows = []
    if point_1[0] == point_2[0]:
        # same column
        col = point_1[0]
        row_start = min(point_1[1], point_2[1]) + 1
        row_end = max(point_1[1], point_2[1])
        new_green_tiles_columns = [(col, row) for row in range(row_start, row_end)]
    elif point_1[1] == point_2[1]:
        # same row
        row = point_1[1]
        col_start = min(point_1[0], point_2[0]) + 1
        col_end = max(point_1[0], point_2[0])
        new_green_tiles_rows = [(col, row) for col in range(col_start, col_end)]

    if new_green_tiles_columns:
        new_green_tiles.extend(new_green_tiles_columns)
    if new_green_tiles_rows:
        new_green_tiles.extend(new_green_tiles_rows)

    return new_green_tiles


for point_1, point_2 in zip(enhanced_red_coordinates, enhanced_red_coordinates[1:] + enhanced_red_coordinates[:1]):
    # There will be green tiles between two adjacent red tiles
    green_tiles_loop = add_green_tiles(point_1, point_2)
    # Fill the grid with red tiles
    mark_coordinates(grid, green_tiles_loop, 'X')

pretty_print(grid)


###########################################################################################
#               4. Find inner green area - "Flood fill" algorithm                         #
###########################################################################################
# a. start on the outer boundary (the padding) [0][0]
# b. only go through allowed tiles '.'
# c. mark visited tiles
# d. after all reachable (outside the loop) tiles are marked, the rest '.' is green -> 'X'


def fill_outside(grid):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = [(0, 0)]
    to_be_walked = [(0, 0)]

    grid_rows, grid_cols = len(grid), len(grid[0])
    while to_be_walked:
        r, c = to_be_walked.pop()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < grid_rows and 0 <= nc < grid_cols:
                if grid[nr][nc] == '.' and (nr, nc) not in visited:
                    to_be_walked.append((nr, nc))
                    visited.append((nr, nc))
    return visited


outside_coor = fill_outside(grid)

# Mark visited as 0 in the grid
mark_coordinates(grid, outside_coor, 0)
pretty_print(grid)


# --> OK tiles are now marked as '#', 'X' and '.'

####################################################################################################
#                           5. Rectangle search                                                    #
####################################################################################################

def rectangle_allowed(grid, point_1, point_2):
    r1, c1 = point_1
    r2, c2 = point_2
    r1, r2 = min(r1, r2), max(r1, r2)
    c1, c2 = min(c1, c2), max(c1, c2)
    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
            if grid[r][c] == 0:  # blocked / outside
                return False
    return True


max_rectangle = 0
max_rectangle_coordinates = []
green_tiles = []

while enhanced_red_coordinates:
    current_coordinate = enhanced_red_coordinates.pop(0)

    for other_coordinate in enhanced_red_coordinates:

        rectangle_size = abs(current_coordinate[0] - other_coordinate[0] + 1) * abs(
            current_coordinate[1] - other_coordinate[1] + 1)
        if rectangle_size > max_rectangle:
            # This is the biggest rectangle so far
            # But does it fulfill the red/green rule?
            # Brute force - easiest - will it be enough?
            # print(f'Rectangle with the coordinates: {current_coordinate},{other_coordinate} ... ')
            if rectangle_allowed(grid, current_coordinate, other_coordinate):
                # print('... is allowed.')
                max_rectangle = rectangle_size
                max_rectangle_coordinates = [current_coordinate, other_coordinate]
                # pretty_print(grid, max_rectangle_coordinates, 'GREEN')
        #     else:
        #         print('... is NOT allowed.')
        #         pretty_print(grid, [current_coordinate, other_coordinate], 'RED')
        # else:
        #     print(f'Rectangle with the coordinates: {current_coordinate},{other_coordinate} is TOO SMALL.')
        #     pretty_print(grid, [current_coordinate, other_coordinate], 'YELLOW')
        # input('Enter ... ')

print("Max rectangle size:", max_rectangle)
print("Max rectangle coordinates:", max_rectangle_coordinates)

pretty_print(grid, max_rectangle_coordinates, 'GREEN')

# not enough for the real input  10 000 x 20 000 tiles
