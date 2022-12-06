
from collections import defaultdict
import os
import time
from icecream import ic


filename = os.path.join('inputs', 'day_05_a.txt')
# filename = os.path.join('inputs', 'day_05_trial.txt')
start_time = time.time()

# ==============================  both at once ==========================================
def assignment_1_2(assignment_no):
    with open(filename) as f:
        all_data = [line.strip('\n') for line in f.readlines()]

    rows = []
    step = 4
    part_of_file = 1
    instructions = []
    occurence_num_line = 1
    for counter, i in enumerate(all_data):
        if part_of_file == 1:
            if ('[' not in i) and occurence_num_line:
                columns_header = i
                part_of_file = 2
                continue
            end_of_line = len(i)

            new_line_list = []
            for j in range(0, end_of_line, step):
                chunk = i[j:j+step]
                new_line_list.append(chunk)
            rows.append(new_line_list)
        else:
            if i: # if not empty
                instructions.append(i)

    headers=[]
    for m in columns_header:
        if m in '0123456789':
            headers.append(m)

    columnwise_data = {key: [] for key in headers}

     # get rid of the empty space and the [ ] ')
    for i in rows:
        for counter, j in enumerate(i):
            if '['in j: #  in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ': # not mepty
                columnwise_data[str(counter+1)].append(j.strip('[ ] '))

    # print('--- follow the instructions -------')
    for i in instructions:
        _, amount, _, col_from, _, col_to = i.split()
        for p in range(int(amount)):
            # looping over the amount of pieces removed from one column
            removed_item = columnwise_data[col_from].pop(0)  # pop( ) if the argument not passed, takes the last one
            if assignment_no == 1:
                columnwise_data[col_to].insert(0, removed_item)
            elif assignment_no == 2:
                columnwise_data[col_to].insert(p, removed_item)
            else:
                raise ValueError('Unkwnon number of assignment.')

    print('----- read the results ---')
    for key, values in columnwise_data.items():
        print(values[0], end ="")

start_time = time.time()
assignment_1_2(2)

print(f"\n Elapsed time is {time.time() - start_time} s.") #  0.0009989738464355469 s.
