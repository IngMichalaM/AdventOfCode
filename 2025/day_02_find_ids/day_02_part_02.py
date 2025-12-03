import re

# with open("input_example.txt") as f:
with open("real_input.txt") as f:
    my_input = f.readline().strip().split(',')


def is_valid_id(in_num: int) -> bool:
    in_num = str(in_num)
    pattern = ''
    for char in in_num:
        pattern += char
        matches = re.findall(pattern, in_num)
        len_matches = 0
        for match in matches:
            len_matches += len(match)
        if len_matches == len(in_num) and len(matches) >= 2:
            return True
    return False


my_ids = 0
for my_range in my_input:
    start, end = map(int, my_range.split('-'))
    for i in range(start, end + 1):
        if is_valid_id(i):
            my_ids += int(i)

print(f'Sum of the found IDs: {my_ids}')
