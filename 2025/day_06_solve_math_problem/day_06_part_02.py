# https://adventofcode.com/2025/day/6
# Read the expressions from right to left

from functools import reduce
import operator

# with open("input_example.txt") as f:
with open("real_input.txt") as f:
    my_input = [line for line in f]

signs = [sign.strip(' ') for sign in my_input[-1].split(' ') if sign.strip(' ') != '']

columns = list(zip(*my_input[:-1]))

ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}


def clean_input(my_input):
    sets_of_numbers_for_equations = []
    numbers_belonging_to_one_equation = []
    for counter, current_tuple in enumerate(my_input):
        try:
            numbers_belonging_to_one_equation.append(int(''.join(current_tuple)))
        except ValueError:
            # expect the gaps
            sets_of_numbers_for_equations.append(numbers_belonging_to_one_equation)
            numbers_belonging_to_one_equation = []
    sets_of_numbers_for_equations.append(numbers_belonging_to_one_equation)  # the last one

    return sets_of_numbers_for_equations


def do_the_math(arranged_input, signs):
    results = []
    for counter, math_problem in enumerate(arranged_input):
        result = reduce(ops[signs[counter]], math_problem)
        results.append(result)

    return results


# clean the input
clean_input = clean_input(columns)
print(clean_input, signs)

# do the math
res = do_the_math(clean_input, signs)
print(res)

# the result we want
print(f'The final result is: {sum(res)}')
