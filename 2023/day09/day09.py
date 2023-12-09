# basically a binary tree, but solved only using for if :-)

def calc_diff(in_list):
  return [(in_list[i+1]-in_list[i]) for i in range(len(in_list)-1)]

def count_backwards(in_list: list, counter: int):
    new_num = 0
    list_out = [] # do not modify the list over which you are looping
    list_out.append(new_num)

    for i in range(counter-1, -1, -1):  # aby to slo az do nuly
        new_num = in_list[i][-1] + list_out[-1]  # last number from current list + last element from previous list
        list_out.append(new_num)
    return list_out[-1]


with open("input.txt") as f:
    input = [line.strip('\n') for line in f.readlines()]

input_num = [list(map(int, line.split())) for line in input]

# ------------------------------------
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
