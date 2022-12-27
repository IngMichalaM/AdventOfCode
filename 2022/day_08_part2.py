""" scenic score
    Sum all the ways from the current number to the closest higher
    in  the direction to the left, right, up and down.
    Just a for loop, brute force. """

import os
import time

filename = os.path.join('inputs', 'day_08_a.txt')
# filename = os.path.join('inputs', 'day_08_trial.txt')
start_time = time.time()

############### PART 2s ###############################################
# read the whole file
with open(filename) as f:
    all_data = [[*line.strip('\n')] for line in f.readlines()]

# convert to int
trees_heights_list = [list(map(int, line)) for line in all_data]

def check_up(cur_num, row_index, col_index, trees_heights_list):
    """ Return True if the current tree is visible over the tops of the trees that are nords (up).
        If it is sheilded return False. """

    for up_index in range(row_index-1, -1, -1): # need to include 0 as well
        if cur_num <= trees_heights_list[up_index][col_index]:
            # the tree is not visible
            return False, row_index - up_index# up_index+1
    else: # tree is visible
        return True,  row_index - up_index # up_index+1

def check_left(cur_num, row_index, col_index, trees_heights_list):
    """ Return True if the current tree is visible over the tops of the trees that are on teh left  .
            If it is sheilded return False. """

    for left_index in range(col_index-1, -1,-1):
        if cur_num > trees_heights_list[row_index][left_index]: # todo check the =
            pass
            # print(
            #     f'Current height is {cur_num}, the shielding is {trees_heights_list[row_index][left_index]} height. Our three is visible.')
        else:
            # print('The to the left  tree is higher or of the same haight , there fore the current tree is not visible ')
            return False, col_index-left_index # left_index+1
    return True, col_index-left_index  # left_index+1

def check_down(cur_num, row_index, col_index, trees_heights_list, tot_rows):
    """ Return True if the current tree is visible over the tops of the trees that are south (down).
            If it is sheilded return False. """

    for down_index in range(row_index+1, (tot_rows )):  # need to include 0 as well
        # print(f'Currentlu in (check_up_visibility), check indexes: up_index: {down_index}, col_index: {col_index}, cur_num={cur_num} ')
        if cur_num > trees_heights_list[down_index][col_index]:
            # print(f'(firstcase) Current height is {cur_num}, '
            #     f'the shielding is {trees_heights_list[down_index][col_index]} height. Our three is visible.')
            pass
        else:
            # print(f'(second) Current height is {cur_num}, '
            #       f'the shielding is {trees_heights_list[down_index][col_index]} height. Our three is visible.')
            return False, down_index-row_index
    return True, down_index-row_index

def check_right(cur_num, row_index, col_index, trees_heights_list, tot_cols):
    """ Return True if the current tree is visible over the tops of the trees that are on teh right .
            If it is sheilded return False. """

    for right_index in range(col_index+1, (tot_cols)):
        # print(f'Currentlu in (check_right_visibility), check indexes: right_index: {right_index}, col_index: {col_index}, cur_num={cur_num} ')
        if cur_num > trees_heights_list[row_index][right_index]:
            pass
            # print(
            #     f'Current height is {cur_num}, the shielding is {trees_heights_list[row_index][right_index]} height. Our three is visible.')
        else:
            # print('The to the right  tree is higher or of the same haight , there fore the current tree is not visible ')
            return False, right_index-col_index
    return True, right_index-col_index

# calculate how many items are visible from the outside
# so all items on the boundary are visible.
# the number = height
total = 0
counter_of_totally_hidden_trees = 0
num_rows = len(trees_heights_list)
max_scenic_score = 0
for row_index, row in enumerate(trees_heights_list):
    for col_index, col_num in enumerate(row):
        cur_num = row[col_index]  # current number
        # print(f'Number {cur_num} is in the inner area.')
        # print(f'--------- Row {row_index} Col {col_index} Num {cur_num} ---------')
        if col_index == 0 or col_index == (len(row) - 1) or row_index==0 or  row_index == num_rows-1:
            # boundary (left and right)
            total += 1
            continue
        else:
            # from each itme go UP, LEFT, DOWN and RIGHT and check if the numbers are smaller then the current
            # ok going up
            bol_check1, score1 = check_up(cur_num, row_index, col_index, trees_heights_list)
            #print(f'Direction UP, score: {score1}')
            bol_check2, score2 = check_left(cur_num, row_index, col_index, trees_heights_list)
            #  print(f'Direction LEFT, score: {score2}')
            bol_check3, score3 = check_down(cur_num, row_index, col_index, trees_heights_list, num_rows)
            # print(f'Direction DOWN, score: {score3}')
            bol_check4, score4 = check_right(cur_num, row_index, col_index, trees_heights_list, len(row))
            # print(f'Direction RIGHT, score: {score4}')
            current_score = score1*score2*score3*score4
            if current_score > max_scenic_score:
                max_scenic_score = current_score
           # print(f'\t current  score is: {current_score}, the maximal is {max_scenic_score}')

print(f'The maximal scenic score found in the inner trees is {max_scenic_score}')

print(f"Elapsed time is {time.time() - start_time} s.")

# correct from part 1
# There are 1803 trees visible from outside.
# There are 7998 totally hidden trees from all sides.
# control check of num trees. There are 9801. THere is 9801 trees in the forest.
# Elapsed time is 0.01779937744140625 s.

# Part 2 - done res:
# 268912
# Elapsed time is 0.025605440139770508 s.