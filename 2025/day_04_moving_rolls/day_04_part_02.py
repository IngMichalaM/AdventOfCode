# with open("input_example.txt") as f:
with open("input.txt") as f:
    my_input = [list(line.strip()) for line in f.readlines()]

NEIGHBORS_8 = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1)
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
num_cols = len(my_input[0])  # width
empty = '.'

print(' ------------------ Settings ------------------')
for i in range(num_rows):
    for j in range(num_cols):
        print(my_input[i][j], end=' ')
    print('')

print(' ---------------  Result -------------------------------')
total_rolls_removed = 0
rolls_to_be_removed = 1
while rolls_to_be_removed:
    num_reachable_rolls = 0
    rolls_to_be_removed = []
    for i in range(num_rows):
        for j in range(num_cols):
            if my_input[i][j] == '@' and check_surroundings(i, j, my_input, num_rows, num_cols):
                num_reachable_rolls += 1
                rolls_to_be_removed.append((i, j))

    # print(f'There are {num_reachable_rolls} reachable paper rolls.')
    # print(f'Rolls to be removed:')
    # print(rolls_to_be_removed)

    total_rolls_removed += num_reachable_rolls

    for coord in rolls_to_be_removed:
        row, col = coord
        my_input[row][col] = empty

    # for i in range(num_rows):
    #     for j in range(num_cols):
    #         print(my_input[i][j], end=' ')
    #     print('')
    # input("Press Enter to continue...")

print(f'There are a total of {total_rolls_removed} paper rolls removed.')
