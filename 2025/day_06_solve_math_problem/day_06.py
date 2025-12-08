# https://adventofcode.com/2025/day/6

from functools import reduce
import operator

# with open("input_example.txt") as f:
with open("real_input.txt") as f:
    my_input = [line.strip('\n') for line in f.readlines()]

ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}


def clean_input(my_input):
    list_of_signs = []
    default_clean_lines = []
    for counter, line in enumerate(my_input):
        default_clean_line_arrangement = []
        # clean the lines
        for i in line.split(' '):
            if i.strip() != '':
                try:
                    default_clean_line_arrangement.append(int(i.strip()))
                except ValueError:
                    # expect the signs
                    list_of_signs.append(i.strip())
        default_clean_lines.append(default_clean_line_arrangement)

    return default_clean_lines[:-1], list_of_signs


def rearrange_expressions(clean_input):
    return list(zip(*clean_input))


def do_the_math(arranged_input, signs):
    results = []
    for counter, math_problem in enumerate(arranged_input):
        result = reduce(ops[signs[counter]], math_problem)
        results.append(result)

    return results


# clean the input
default_clean_input, signs = clean_input(my_input)

# rearrange the expressions
arranged_clean_input = rearrange_expressions(default_clean_input)

# do the math
res = do_the_math(arranged_clean_input, signs)

# the result we want
print(f'The final result is: {sum(res)}')
