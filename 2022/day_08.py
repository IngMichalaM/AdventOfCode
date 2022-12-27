"""  Visibility of the trees from outside of the grid.
Check the height of the trees with respect to its left, right, up and down neighbour.
Kind of brut force method. """

import os
import time

filename = os.path.join('inputs', 'day_08_a.txt')
# filename = os.path.join('inputs', 'day_08_trial.txt')
start_time = time.time()

# read the whole file
with open(filename) as f:
    all_data = [[*line.strip('\n')] for line in f.readlines()]

trees_heights_list = [list(map(int, line)) for line in all_data]

def check_up_visibility(cur_num, row_index, col_index, trees_heights_list):
    """ Return True if the current tree is visible over the tops of the trees that are nords (up).
        If it is sheilded return False. """

    counter_prulez = 0
    for up_index in range(row_index-1, -1, -1): # need to include 0 as well
        if cur_num <= trees_heights_list[up_index][col_index]:
            #  print(f'Current height is {cur_num}, the shielding is {trees_heights_list[up_index][col_index]} height. Our three is visible.')
            counter_prulez +=1
            # print('The uppre tree is higher or of the same haight , there fore the current tree is not visible ')
            return False
    else:
        return True

def check_left(cur_num, row_index, col_index, trees_heights_list):
    """ Return True if the current tree is visible over the tops of the trees that are on teh left  .
            If it is sheilded return False. """

    # for left_index in range(0, col_index): # ok for part 1
    for left_index in range(col_index-1, -1,-1): # for part 2 go from the current tree to the side
        # todo what about range(0)?
        # print(f'Currentlu in (check_right_visibility), check indexes: right_index: {right_index}, col_index: {col_index}, cur_num={cur_num} ')
        if cur_num > trees_heights_list[row_index][left_index]:
            pass
            # print(
            #     f'Current height is {cur_num}, the shielding is {trees_heights_list[row_index][left_index]} height. Our three is visible.')
        else:
            # print('The to the left  tree is higher or of the same haight , there fore the current tree is not visible ')
            return False
    return True

def check_down(cur_num, row_index, col_index, trees_heights_list, tot_rows):
    """ Return True if the current tree is visible over the tops of the trees that are south (down).
            If it is sheilded return False. """
    for down_index in range(row_index+1, (tot_rows )):  # need to include 0 as well
        # print(f'Currentlu in (check_up_visibility), check indexes: up_index: {down_index}, col_index: {col_index}, cur_num={cur_num} ')
        if cur_num > trees_heights_list[down_index][col_index]:
            # print(
            #     f'Current height is {cur_num}, the shielding is {trees_heights_list[down_index][col_index]} height. Our three is visible.')
            pass
        else:
            # print('The downwards tree is higher or of the same haight , there fore the current tree is not visible ')
            return False
    return True

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
            return False
    return True

# calculate how many items is are visible from the outside
# so all items on the boundary are visible.

total = 0
counter_of_totally_hidden_trees = 0
num_rows = len(trees_heights_list)
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
            if check_up_visibility(cur_num, row_index, col_index, trees_heights_list):
                # print(f'\t\tVisibility up is True, we add 1 to total,'
                #       f' since it is already visible and counted, we dont need to check the otehr directions ')
                total+=1
                continue
            elif check_left(cur_num, row_index, col_index, trees_heights_list):
                # print(f'\t\t\t\t We are adding 1 for the num {cur_num} at the coordinates [{row_index},{col_index}] ')
                total += 1
                continue
            elif check_down(cur_num, row_index, col_index, trees_heights_list, num_rows):
                # print(f'\t\tVisibility DOWN is True, we add 1 to total,'
                #           f' since it is already visible and counted, we dont need to check the otehr directions ')
                total+=1
                continue
            elif check_right(cur_num, row_index, col_index, trees_heights_list, len(row)):
                # print(f'\t\tVisibility TO THE RIGHT is True, we add 1 to total,'
                #                       f' since it is already visible and counted, we dont need to check the otehr directions ')
                total+=1
                continue
            else:
                counter_of_totally_hidden_trees += 1
                # print('This three is totally hidden from all sides.')

print(f'There are {total} trees visible from outside.')
print(f'There are {counter_of_totally_hidden_trees} totally hidden trees from all sides.')
print(f'control check of num trees. There are {total+counter_of_totally_hidden_trees}. THere is {num_rows*len(trees_heights_list[1])} trees in the forest.')

print(f"Elapsed time is {time.time() - start_time} s.")
