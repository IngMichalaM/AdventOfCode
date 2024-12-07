# Solution for Day 07 Part 1 and 2
# https://adventofcode.com/2024/day/7

import re
from itertools import product
from typing import List, Tuple
import operator


def combinations(number_of_char: int) -> List[Tuple[str, ...]]:
    characters = ['*', '+', '||']
    return list(product(characters, repeat=number_of_char))


def my_concatenation(a: int, b: int) -> int:
    return int(str(a)+str(b))


def do_calculation(math_operation: Tuple[str, ...], numbers: List[int]):
    """ For tuple of operations and list of numbers return the result."""

    operation_map = {
        "+": operator.add,
        "*": operator.mul,
        '||': my_concatenation,
    }

    for counter, operation in enumerate(math_operation):

        if counter == 0:
            res = operation_map[operation](numbers[counter], numbers[counter+1])
        else:
            res = operation_map[operation](res, numbers[counter+1])

    return res


def feasible_combination(A: List[int]) -> bool:
    """ Take a list of integers.
        First number is the target value. 
        Find if using the given operations one can put togetehr the rest of the integers to get the target value. """

    target = A[0]
    numbers_available = A[1:]

    char_combinations = combinations(len(numbers_available)-1)  # for three numbers, there are 2 places for the operators

    for current_operation_combination in char_combinations:
        res = do_calculation(current_operation_combination, numbers_available)

        if res == target:
            return True  # there is a combination of operation to make the equation OK
    else:
        return False


with open("input/inputA.txt") as f:
# with open("input/input_test.txt") as f:
    aoc_input = [line.strip('\n') for line in f.readlines()]

clean_input = []
for item in aoc_input:
    a = [x for x in re.split(r'[: ]', item) if x.strip()]
    clean_input.append(list(map(int, a)))

total = 0  # count all the "target" values for the successful equations
for line in clean_input:

    if feasible_combination(line):
        total += line[0]

print(total)