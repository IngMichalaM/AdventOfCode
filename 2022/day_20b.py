import copy
import os
import time

#
filename = os.path.join('inputs', 'day_20a.txt')
start_time = time.time()

with open(filename) as f:
    the_list = [int(line.strip('\n')) for line in f.readlines()]

# print(the_list)
# the_list = [0, 10, -50, 6, 7, 20, -50, 6, 60]
# the_list = [1,2,-3, 3,-2,0,4]
# the_list = [1,10,1, 10, 1, 10]

orig_list = []
for counter, num in enumerate(the_list):
    orig_list.append((counter, num))
    if num == 0:
        print(f'The ZERO is: {(counter, num)}')
        the_zero_tuple = (counter, num)

# print(f'{orig_list}')

new_list = copy.deepcopy(orig_list)

for counter, the_tuple in enumerate(orig_list):
    lok_name, num = the_tuple

    # find the element whose turn it is (from the old list) in the new list
    index_el = new_list.index(the_tuple)

    # remove it
    new_list.remove(the_tuple)

    # insert it to the proper place
    new_index = index_el + num

    if new_index == 0:
        # in the example, if the new index is 0, it is placed in the end
        new_list.append(the_tuple)
    elif abs(new_index) in range(len(the_list)):
        # this is ok, just use the index
        new_list.insert(new_index, the_tuple)
    elif new_index >= len(orig_list):
        new_index_adj = new_index % (len(orig_list) - 1)
        new_list.insert(new_index_adj, the_tuple)
    elif abs(new_index) >= len(orig_list):
        new_index_adj = -1 * (abs(new_index) % (len(orig_list) - 1))
        new_list.insert(new_index_adj, the_tuple)
    else:
        print('Who knows what. ')

    # print(f'Element beeing moved is {the_tuple} and was on {counter} postion in the original list.')
    # print(new_list)
    # input('press sometin ..')

# print('back to the list: ')
final_list = []
for lok_name, num in new_list:
    final_list.append(num)

print(f'final lsit = {final_list}')

index_of_zero = final_list.index(0)

# find the 1000th, 2000th and 3000th number after zero (there is only one zero in teh list]
ind_1000 = (index_of_zero + 1000) % len(orig_list)
ind_2000 = (index_of_zero + 2000) % len(orig_list)
ind_3000 = (index_of_zero + 3000) % len(orig_list)
print(f'The 1000th number after 0 is {final_list[ind_1000]}')
print(f'The 3000th number after 0 is {final_list[ind_2000]}')
print(f'The 2000th number after 0 is {final_list[ind_3000]}')

print(f'The result is: {final_list[ind_1000] + final_list[ind_2000] + final_list[ind_3000]}')

print(f"Elapsed time is {time.time() - start_time} s.")

# 3552 too low
# 3552 too low
# 2589 too low
# 5962 ok
