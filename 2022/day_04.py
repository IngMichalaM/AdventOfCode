
import os
import re
import time

# https://adventofcode.com/2022/day/4

filename = os.path.join('inputs', 'day_04_a.txt')
# filename = os.path.join('inputs', 'day_04_trial.txt')
start_time = time.time()

############### Part 1 attempt 1 ###############################################

def part1():
    with open(filename) as f:
        all_data = [i.split(',') for i in f.read().split('\n')]

    total = 0
    for elf1r, elf2r in all_data:
        elf1= list(map(int, elf1r.split('-')))
        elf2 = list(map(int, elf2r.split('-')))

        if ((elf1[0] <= elf2[0]) and (elf1[1]>=elf2[1])):
            total+=1
        elif (elf1[0] >= elf2[0]) and (elf1[1]<=elf2[1]):
            total+=1

    return total

############### Part 1 attempt 2 ###############################################
# # the whole range of one is included in the other, or wice versa
def part12():

    with open(filename) as f:
        all_data = [list(map(int, (re.split(',|-', i)))) for i in f.read().split('\n')]

    total = 0
    for elf_1_start, elf_1_end, elf_2_start, elf_2_end in all_data:

        elf1range = set(range(elf_1_start, elf_1_end+1))
        elf2range = set(range(elf_2_start, elf_2_end+1))

        if ((elf1range & elf2range) == elf1range ) or ((elf1range & elf2range) == elf2range ):
            total += 1

    return total


############### Part 2 attemt 1 ###############################################
def part2():
    with open(filename) as f:
        all_data = [i.split(',') for i in f.read().split('\n')]

    total = 0
    total_not_inter = 0

    all_couples = len(all_data)
    # find those that do not overlap at all and subtract from the total

    for elf1r, elf2r in all_data:
        elf1= list(map(int, elf1r.split('-')))
        elf2 = list(map(int, elf2r.split('-')))

        if (elf1[1] < elf2[0]) or (elf1[0] > elf2[1]):
            total_not_inter += 1

    # print(f'There are {all_couples} elfpairs in total. {total_not_inter} do not overlap at all. {all_couples-total_not_inter} overlap.')
    return all_couples-total_not_inter

############### Part 2 attemt 2 ###############################################
def part22():
    with open(filename) as f:
        all_data = [list(map(int, (re.split(',|-', i)))) for i in f.read().split('\n')]

    total = 0
    total_not_inter = 0
    all_couples = len(all_data)

    # find those that do not overlap at all and subtract from the total
    for elf_1_start, elf_1_end, elf_2_start, elf_2_end in all_data:

        if (elf_1_end < elf_2_start) or (elf_1_start > elf_2_end):
            total_not_inter += 1

    return all_couples-total_not_inter


# ===========================================================================
start_time = time.time()
print(f'Result from part 1 is: {part1()}. Elapsed time is {time.time() - start_time} s.)') #  Result from part 1 is: 511. Elapsed time is 0.002008676528930664 s.)
                                                                                            # Result from part 1 is: 511. Elapsed time is 0.0014684200286865234 s.)
start_time = time.time()
print(f'Result for the second attempt is {part12()}. Elapsed time is {time.time() - start_time} s.)')

start_time = time.time()
print(f'Result from part 2 is: {part2()}. Elapsed time is {time.time() - start_time} s.)') # Result from part 2 is: 821. Elapsed time is 0.0019843578338623047 s.)

start_time = time.time()
print(f'Result from part 2b is: {part22()}. Elapsed time is {time.time() - start_time} s.)') # R
