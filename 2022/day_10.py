""" Summing values based on the instructions.
    Only tricky part is, that some instructions take one round, some two. """

import os
import time

filename = os.path.join('inputs', 'day_10_a.txt')
#filename = os.path.join('inputs', 'day_10_trial.txt')
start_time = time.time()

#  whole file at once
with open(filename) as f:
    all_data = [line.strip('\n') for line in f.readlines()]

cycles_to_count = [20, 60, 100, 140, 180, 220]
start = 1
counter = 0 # counter does not count the lines , but te commands
register_value = 1 # counts for each cycle
total_register = 0 # counts only for cycles_to_count

# there are sometimes 2 commands on one line
chekcup = ['1']
checkupsum = []
for line in all_data:
    try:
        part1, value = line.split()
        chekcup.append(value)
    except ValueError:
        part1 = line

    if part1 == 'addx':
        counter += 1

        if counter in cycles_to_count:
            partialregister =  counter*register_value
            total_register += partialregister
            checkupsum.append(partialregister)

        counter += 1

        if counter in cycles_to_count:
            #     print(f'Counter = {counter}, line = {part1} {value}')

            partialregister = counter * register_value
            total_register += partialregister
            checkupsum.append(partialregister)

        register_value += int(value)

    elif part1 == 'noop':
        counter += 1
        #print(f'Counter = {counter}, line = {part1} ')

        if counter in cycles_to_count:
            partialregister = counter * register_value
            total_register += partialregister
           # print(f'Register value = {register_value}, total register value = {total_register}')
            checkupsum.append(partialregister)


print('----------------')
print(f'Total register value = {total_register}')
print(f'checkupsum is {checkupsum}')
# file1.close()
print(f"Elapsed time is {time.time() - start_time} s.")
