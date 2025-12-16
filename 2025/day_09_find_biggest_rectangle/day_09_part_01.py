# https://adventofcode.com/2025/day/9

with open("real_input.txt") as f:
    my_input = [line.strip('\n') for line in f.readlines()]

coordinates = []
for coor in my_input:
    col_coor, row_coor = coor.split(',')
    coordinates.append((int(col_coor), int(row_coor)))

max_rectangle = 0
max_rectangle_coordinates = []
while coordinates:
    current_coordinate = coordinates.pop(0)

    for other_coordinate in coordinates:

        rectangle_size = abs(current_coordinate[0] - other_coordinate[0] + 1) * abs(current_coordinate[1] - other_coordinate[1] + 1)
        if rectangle_size > max_rectangle:
            max_rectangle = rectangle_size
            max_rectangle_coordinates = [current_coordinate, other_coordinate]

print("Max rectangle size:", max_rectangle)
print("Max rectangle coordinates:", max_rectangle_coordinates)
