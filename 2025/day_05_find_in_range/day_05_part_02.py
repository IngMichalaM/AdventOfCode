# https://adventofcode.com/2025/day/5
# Merge the overlapping ranges (as in TODO from part 1 :D) and count the total number of fresh food IDs

with open("input_part1.txt") as f:
    my_input = [line.strip('\n') for line in f.readlines()]

list_of_ranges = []
list_of_ids = []

for line in my_input:
    food_range = my_input.pop(0)

    if food_range == '':
        break

    range_start, range_end = map(int, food_range.split('-'))
    list_of_ranges.append((range_start, range_end))

# sort the list of ranges by their start values
ranges = sorted(list_of_ranges, key=lambda x: x[0])

# merge overlapping ranges
merged = []  # will hold the merged intervals
for start, end in ranges:
    if not merged or start > merged[-1][1] + 1:
        # just add first interval
        # no overlap and not touching -> new interval
        merged.append([start, end])
    else:
        # overlaps or touches -> merge - extend last interval
        # the second interval can be within the first one or extend it
        merged[-1][1] = max(merged[-1][1], end)  # the end is the bigger number
                # of the last interval and the last number of the new interval

total_fresh_food_ids = 0
for start, end in merged:
    total_fresh_food_ids += (end - start + 1)

print(f'There are {total_fresh_food_ids} fresh food IDs.')
