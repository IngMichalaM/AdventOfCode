# Solution for Day 04 Part A
# https://adventofcode.com/2024/day/4

def count_word_in_line(line: str, word: str) -> int:
    return line.count(word)

# with open("input/input_test.txt", "r") as file:
with open("input/inputA.txt", "r") as file:
    aoc_input = [line.strip() for line in file.readlines()]  # for search in lines

# columns to rows - transposition of the list of strings - for search in columns
aoc_input_transposed = [''.join(i) for i in zip(*aoc_input)]

# diagonal from  left-top to right-bottom
rows = len(aoc_input)
columns = len(aoc_input[0])

down_right_diagonals = []

for d in range(columns + rows - 1):
    current_diagonal = []

    if d < rows:
        r = abs(rows-1-d)
        c = 0
    else:
        r = 0
        c = d-rows+1

    while r < rows and c < columns:
        current_diagonal.append(aoc_input[r][c])
        r += 1
        c += 1

    down_right_diagonals.append(''.join(current_diagonal))

# diagonal from right-top to left-bottom
down_left_diagonals = []
for d in range(columns + rows - 1):
    current_diagonal = []

    if d < columns:
        r = 0
        c = d
    else:
        r = d-columns+1
        c = columns-1

    while r < rows and 0 <= c < columns:
        current_diagonal.append(aoc_input[r][c])
        r += 1
        c -= 1

    down_left_diagonals.append(''.join(current_diagonal))

# counting
num_xmas = 0

# count XMAS and SAMX in lines
for row in aoc_input:
    num_xmas += count_word_in_line(row, 'XMAS')
    num_xmas += count_word_in_line(row, 'SAMX')

# count XMAS and SAMX in columns
for row in aoc_input_transposed:
    num_xmas += count_word_in_line(row, 'XMAS')
    num_xmas += count_word_in_line(row, 'SAMX')

# count XMAS and SAMX in diagonal to down-right
for line in down_right_diagonals:
    num_xmas += count_word_in_line(line, 'XMAS')
    num_xmas += count_word_in_line(line, 'SAMX')

# count XMAS and SAMX in diagonal to down-left
for line in down_left_diagonals:
    num_xmas += count_word_in_line(line, 'XMAS')
    num_xmas += count_word_in_line(line, 'SAMX')

print(f"There are in total {num_xmas} XMAS")