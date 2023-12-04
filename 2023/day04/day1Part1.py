# day 4, part 1 - counting content of one list of numbers in another list of numbers
import re

with open("input_test.txt") as f:
    input = [line.strip('\n') for line in f.readlines()]

Winning_points = 0

for line in input:

    [card_num, winning_numbers_str, my_numbers_str] = re.split(r'[:|]', line)

    winning_numbers = list(map(int, winning_numbers_str.split()))
    my_numbers = list(map(int, my_numbers_str.split()))
    num_winners = len([num for num in my_numbers if num in winning_numbers])

    if num_winners > 0:
        Winning_points += 2**(num_winners-1)

print(Winning_points)
