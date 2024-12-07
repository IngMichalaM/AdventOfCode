# Solution for Day 04 Part B
# X-MAS - looking for 2 MAS organised as X

from typing import List, Tuple


def count_word_in_line(line: str, word: str) -> int:
    return line.count(word)


# with open("input/input_test.txt", "r") as file:
with open("input/inputA.txt", "r") as file:
    aoc_input = [line.strip() for line in file.readlines()]  # for search in lines


def opposite_direction(direction):
    if direction == [-1, -1]:
        return [1, 1]
    elif direction == [-1, 1]:
        return [1, -1]
    elif direction == [1, 1]:
        return [-1, -1]
    elif direction == [1, -1]:
        return [-1, 1]
    else:
        raise Exception("Unknown direction")


def num_A_around_here(aoc_input: List[str], counter: int, counter_c: int) -> int:
    """ Check all the four possible direction for M and S in the opposite directions.
     The durrent position si in [counter, counter_c] """
    looking_for = ['M', 'S']
    # left up / right up / left down / right down
    directions = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
    num_xmas = 0
    # print(f"Current positions is {counter},{counter_c} and current letter is {aoc_input[counter][counter_c]}")
    for d in directions:
        # print(f"Current direction is {d=}")
        if aoc_input[counter + d[0]][counter_c + d[1]] == looking_for[0]:
            # there might be XMAS here
            # print(f"The letter there is {aoc_input[counter + d[0]][counter_c + d[1]] }")
            # check the opposite direction
            x, y = opposite_direction(d)
            # print(f"Opposite direction is {x}, {y} and the letter there is {aoc_input[counter + x][counter_c + y]}")
            if aoc_input[counter + x][counter_c + y] == looking_for[1]:
                # found one!
                num_xmas += 1

    return 1 if num_xmas == 2 else 0


total_num_mas = 0
# leave the sides - there would not be space for the XMAS if A is on the edge
for counter in range(1, len(aoc_input)-1):
    # print(list(aoc_input[counter]))
    for counter_c in range(1, len(aoc_input[counter])-1):
        if aoc_input[counter][counter_c] == 'A':
            total_num_mas += num_A_around_here(aoc_input, counter, counter_c)

print(f"There are {total_num_mas} X-MAS!")
