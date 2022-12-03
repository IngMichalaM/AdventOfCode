
import os
import time

filename = os.path.join('inputs', 'day_02_a.txt')
# filename = os.path.join('inputs', 'day_02_trial.txt')
start_time = time.time()

############### PART 1  ##########################################################################

# (1 for Rock, 2 for Paper, and 3 for Scissors)
#  (0 if you lost, 3 if the round was a draw, and 6 if you won).

res_strateg_table = {'A X': 3 + 1,
                     'A Y': 6 + 2,
                     'A Z': 0 + 3,
                     'B X': 0 + 1,
                     'B Y': 3 + 2,
                     'B Z': 6 + 3,
                     'C X': 6 + 1,
                     'C Y': 0 + 2,
                     'C Z': 3 + 3}

def part1():
    with open(filename) as f:
        # the_strateg = [line.strip() for line in f.readlines()]
        total_score = 0
        for line in f:
            total_score += res_strateg_table[line.strip()]

    return total_score

# print(' ================ PART 2 =======================')

def part2():
    total_score = 0
    with open(filename) as f:
        # the_strateg = [line.strip() for line in f.readlines()]

        for line in f:
            # print(line.strip())
            # elf_choise, mine_goal = f.readline().strip().split()
            elf_choise, mine_goal = line.strip().split()
            # print(elf_choise)
            # print(mine_goal)

            if mine_goal == 'X':
                # need to lose
                if elf_choise == 'A':
                    total_score += 3
                elif elf_choise == 'B':
                    total_score += 1
                else:
                    total_score += 2
            elif mine_goal == 'Y':
                # need to draw
                if elf_choise == 'A':
                    total_score += 3+1
                elif elf_choise == 'B':
                    total_score += 3+2
                else:
                    total_score += 3+3
            elif mine_goal == 'Z':
                # need to  win
                if elf_choise == 'A':
                    total_score += 6+2
                elif elf_choise == 'B':
                    total_score += 6+3
                else:
                    total_score += 6+1

    return total_score

# =====================================
total_score = part1()
print(f'Total score in part 1 is {total_score}.')
# total_score = part2()
# print(f'Total score in part 2 is {total_score}.')
#
print(f"Elapsed time is {time.time() - start_time} s.")

# ==========================================================
# part 1
# the_strateg = [line.strip() for line in f.readlines()]
# Total score is 12156.
# Elapsed time is 0.00133 s.
# Part 1, line by line
# Total score is 12156.
# Elapsed time is 0.00048 s.

# part 2
# Total score is 10835.
# Elapsed time is 0.00101 s.
# ==========================================================
