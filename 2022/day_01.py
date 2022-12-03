
import os
import time

filename = os.path.join('inputs', 'day_01_a.txt')
# filename = os.path.join('inputs', 'day_01_trial.txt')

print('============= DRUHE RESENI =======================================')
start_time = time.time()

with open(filename) as f:
    bags_of_snacks = [i.split('\n') for i in f.read().split('\n\n')]

elves_snack_pockets = [sum(map(int, i)) for i in bags_of_snacks]

print('Most calorical bag of snack has ', max(elves_snack_pockets), 'calories.')

elves_snack_pockets.sort(reverse=True)

print(f'The sum of top three amounts is: {sum(elves_snack_pockets[:3])} ')
print(f"Elapsed time is {time.time() - start_time} s.")

print('============= PRVNI RESENI =======================================')

start_time = time.time()

with open(filename) as f:
    bags_of_snacks = [line.strip() for line in f.readlines()]

total_counts = []
a = 0
for snack in bags_of_snacks:
    if snack:
        a += int(snack)
    else:
        total_counts.append(a)
        a = 0
total_counts.append(a)

print('Most calorical bag of snack has', max(total_counts), 'calories.')

total_counts.sort(reverse=True)
print(f'The sum of top three amounts is: {sum(total_counts[:3])} ')

print(f"Elapsed time is {time.time() - start_time} s.")