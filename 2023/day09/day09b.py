def calc_diff(in_list: list):
    """ Calculate differences between two adjacent number in th input list """
    return [(in_list[i+1]-in_list[i]) for i in range(len(in_list)-1)]

def count_backwards(in_list: list[list], counter: int):
    """ """
    new_num = 0
    list_out = [] # do not modify the list over which you are looping,
                  # only save the new extrapolated values
                  # not a list of lists, only a plain list
    list_out.append(new_num)

    for i in range(counter-1, -1, -1):  # aby to slo az do nuly (start, krok, end)
        new_num = in_list[i][0] - list_out[-1]  # from the first number in current list subtract
                                                # the new  first element from the previous list, which
                                                # is stored as last element in the list_out list
        list_out.append(new_num)
    return list_out[-1]  # return only the firt number of the foremost line, rest is tored for check


with open("input_test.txt") as f:
    input = [line.strip('\n') for line in f.readlines()]

input_num = [list(map(int, line.split())) for line in input]

res_for_each_input_line = []
for curr_line in input_num:
    new_list_from_current_line = []
    new_list_from_current_line.append((curr_line))

    counter = 0
    while True:
        counter += 1
        new_line_with_differences = calc_diff(curr_line)
        new_list_from_current_line.append(new_line_with_differences)

        if not any(new_line_with_differences):
            res_curr_line = count_backwards(new_list_from_current_line, counter)
            break
        else:
            curr_line = new_line_with_differences

    res_for_each_input_line.append(res_curr_line)

print(sum(res_for_each_input_line))