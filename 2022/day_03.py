
import os
import time
from icecream import ic

# https://adventofcode.com/2022/day/3

# import string
# string.ascii_uppercase
# string.ascii_lowercase

filename = os.path.join('inputs', 'day_03_a.txt')
# filename = os.path.join('inputs', 'day_03_trial.txt')
start_time = time.time()

############### COMMON FUNC ##############################################

def get_letter_priority(letter):
    try:
        lower_case_letters = 'abcdefghijklmnopqrstuvwxyz'
        return lower_case_letters.index(letter)+1
    except ValueError:
        upper_case_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        return upper_case_letters.index(letter) + 1 + 26
    except:
        print('Unknown character ')

############### PRVNI CAST ###############################################

def part1():
    total_value = 0
    with open(filename) as f:
        for line in f:
            line = line.strip()

            len_line = len(line)

            string1 = line[0:len_line//2]
            string2 = line[len_line//2:]

            commont_letter = ''.join(set(string1).intersection(string2))

            total_value += get_letter_priority(commont_letter)

    return total_value


############### DRUHA CAST ###############################################

def part2():
    total_value = 0
    with open(filename) as f:
        for counter, line in enumerate(f):

            if counter%3 == 0:
                group_of_3_elfs = []
                group_of_3_elfs.append(line.strip())
            else:
                group_of_3_elfs.append(line.strip())

            if counter%3 == 2: # group of three
                common_letters = ''.join(set(group_of_3_elfs[0]).intersection(group_of_3_elfs[1]))
                common_letter = ''.join(set(group_of_3_elfs[2]).intersection(common_letters))
                total_value += get_letter_priority(common_letter)

    return total_value

# =============== JINE RESENI ============================================================

def part2b():
    with open(filename) as f:
        all_data = [i for i in f.read().split('\n')]

    total = 0
    for i in range(len(all_data)//3):
        current_triplet = all_data[i*3:i*3+3]
        common_letter = ''.join(set(current_triplet[0]).intersection(current_triplet[1]).intersection(current_triplet[2]))
        total += get_letter_priority(common_letter)

    return(total)

# ===========================================================================
# print(f'Result from part 1 is: {part1()}.')  # Elapsed time is 0.0005071163177490234 s.
# print(f'Result from part 2 is: {part2()}.') # Elapsed time is 0.001056671142578125 s.
print(f'Result from part 2b is: {part2b()}.') #  Elapsed time is 0.0 s.
print(f"Elapsed time is {time.time() - start_time} s.")
