# https://adventofcode.com/2025/day/9
# There are some red tiles in the grid
# In between on the same line and/or column, they are green tiles (needs to be found)
# This creates a closed loop, inside is also full of green tiles
# Find the biggest rectangle that have two red tiles in the opposite corners and inside only green tiles

import matplotlib.pyplot as plt
from shapely.geometry import Polygon, box
from matplotlib.patches import Rectangle as MPLRect

# 1. Read red coordinates
# 2. Create a python Polygon from the points (closed loop)
# 3. Rectangle search

print('#################  1. Read input and prepare red coordinates')

with open("real_input.txt") as f:
    my_input = [line.strip('\n') for line in f.readlines()]

red_coordinates = []
for coor in my_input:
    col_coor, row_coor = coor.split(',')
    red_coordinates.append((int(col_coor), int(row_coor)))

print('#################  2. Create a python Polygon')
polygon = Polygon(red_coordinates)

print('#################  3. Rectangle search')
max_rectangle = 0
max_rectangle_coordinates = []
green_tiles = []

while red_coordinates:
    current_coordinate = red_coordinates.pop(0)

    for other_coordinate in red_coordinates:
        min_x = min(current_coordinate[0], other_coordinate[0])
        max_x = max(current_coordinate[0], other_coordinate[0])
        min_y = min(current_coordinate[1], other_coordinate[1])
        max_y = max(current_coordinate[1], other_coordinate[1])

        current_rectangle = box(min_x, min_y, max_x, max_y)

        rectangle_size = abs(current_coordinate[0] - other_coordinate[0] + 1) * abs(
            current_coordinate[1] - other_coordinate[1] + 1)

        if rectangle_size > max_rectangle and polygon.contains(current_rectangle):
            max_rectangle = rectangle_size
            max_rectangle_coordinates = [current_coordinate, other_coordinate]

print("Max rectangle size:", max_rectangle)
print("Max rectangle coordinates:", max_rectangle_coordinates)

print('#################  4. Display')
fig, ax = plt.subplots(figsize=(10, 10))

# Plot polygon
x, y = polygon.exterior.xy
ax.fill(x, y, alpha=0.3, fc='lightgreen', ec='green', linewidth=2)

# Plot rectangle
x1 = max_rectangle_coordinates[0][0]
y1 = max_rectangle_coordinates[0][1]
x2 = max_rectangle_coordinates[1][0]
y2 = max_rectangle_coordinates[1][1]

rect_patch = MPLRect((x1, y1), x2-x1, y2-y1, linewidth=2, edgecolor='blue', facecolor='none')
ax.add_patch(rect_patch)

ax.set_aspect('equal')
plt.show()

#  Comments
#  Most time consuming was using grid for the visualisation
#  With Polygon it is neither needed to look for the green edge tiles, nor to mark the inside green tiles
#  We are not calculating the area as in math, but counting the tiles, so cannot use area() method of Polygon

print('#################  5. Done')
