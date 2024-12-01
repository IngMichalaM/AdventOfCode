# https://adventofcode.com/2024/day/1

# test "input/input_test.txt"
with open("input/inputA.txt") as f:
    input = [line.strip('\n').split() for line in f.readlines()]

L = [int(x) for x, y in input]
R = [int(y) for x, y in input]

distance = []
for x, y in zip(sorted(L), sorted(R)):
    distance.append(abs(x-y))

print(f'Total distance (Part A): {sum(distance)}')
