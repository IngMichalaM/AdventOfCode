# https://adventofcode.com/2025/day/4

# with open("input_example.txt") as f:
with open("input.txt") as f:
    my_input = [line.strip('\n') for line in f.readlines()]

NEIGHBORS_8 = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1)
]

def check_surroundings(row: int, column: int, rolls_grid, num_rows, num_cols):
    """ If there are < 4 adjacent paper rolls, this roll is reachable - True """
    rolls = 0
    for dx, dy in NEIGHBORS_8:
        nx, ny = column + dx, row + dy
        if 0 <= nx < num_cols and 0 <= ny < num_rows and rolls_grid[ny][nx] == '@':
            rolls += 1

    if rolls < 4:
        return True
    return False


num_rows = len(my_input)  # height
num_cols = len(my_input[0])  # widht
empty = '.'
paper_roll = '@'

print(' ------------------ Settings ------------------')
for i in range(num_rows):
    for j in range(num_cols):
        print(my_input[i][j], end=' ')
    print('')

print(' ---------------  Result -------------------------------')
num_reachable_rolls = 0
for i in range(num_rows):
    for j in range(num_cols):
        if my_input[i][j] == '@' and check_surroundings(i, j, my_input, num_rows, num_cols):
            num_reachable_rolls += 1

print(f'There are {num_reachable_rolls} reachable paper rolls.')
