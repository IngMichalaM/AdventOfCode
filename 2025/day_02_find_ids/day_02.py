# with open("input_example.txt") as f:
with open("real_input.txt") as f:
    my_input = f.readline().strip().split(',')

my_ids = 0
for my_range in my_input:
    start, end = map(int, my_range.split('-'))

    for i in range(start, end + 1):
        i = str(i)
        if len(i) % 2 == 0:
            mid = len(i) // 2
            left = i[:mid]
            right = i[mid:]
            if left == right:
                my_ids += int(i)

print(f'Sum of the found IDs: {my_ids}')
