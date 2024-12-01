# Solution for Day 01 Part B
# https://adventofcode.com/2024/day/1#part2

from collections import Counter
import time

start_time = time.perf_counter()

# test "input/input_test.txt"
# input is the same for part 1 (A) and 2 (B)
with open("input/inputA.txt") as f:
    my_input = [line.strip('\n').split() for line in f.readlines()]

L = [int(x) for x, y in my_input]
R = [int(y) for x, y in my_input]

counter = Counter(R)

similarity_scores = []
for x in L:
    # find how many times the x in Left column is in the Right column
    # if there is none, counter = 0
    similarity_scores.append(x * counter[x])

print(f'The similarity score is (Part B): {sum(similarity_scores)}')

end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.5f} seconds")