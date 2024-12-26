"""
Solution for Day 14 Part 1
Robot follows the moving instructions, pushes the boxes if necessary.
Robot and boxes stop at the walls.
Recursion.
In the final state, after performing all the moves, sum all boxes' GPS coordinates
"""

from get_input import ROWS, COLUMNS, directions_input, coor_walls, coor_robot, coor_boxes
from robot_walk import Robot

current_direction = directions_input[0]

robot = Robot(*coor_robot, current_direction, coor_walls, coor_boxes, (COLUMNS, ROWS))
print(f"initial position of the robot: {robot.position()}")
print(f"initial grid: ")
robot.display_grid()

for pos in directions_input:
    robot.change_direction(pos)
    robot.move_robot()
    # robot.display_grid()
    # input("enter ...")
    # time.sleep(0.05)

print(f"End position of the boxes: ")

robot.display_grid()

total = 0
for box in robot.boxes:
    total += 100 * box[1] + box[0]

print(f"The total GPS is {total}.")
