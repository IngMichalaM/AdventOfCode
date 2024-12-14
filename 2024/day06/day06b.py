# Solution for Day 06 Part B
# https://adventofcode.com/2024/day/6#part2
import time
import itertools
from guard import Guard
from get_playground import guard_starting_position, ROWS, COLUMNS, obstacles

guard = Guard(*guard_starting_position, "U", obstacles, (COLUMNS, ROWS))
print(f"initial position: {guard.position()}")
print(str(guard))

a = 0
guard.display_grid()
# input("enter...")
# part 1 - count how many unique position the guard goes through
while guard.off_ground is False:
    guard.move()
    a += 1

# guard.display_grid()
print(f"Unique visited positions {guard.unique_visits} (result for part 1).")

################ Part B ###################################
#  Where to put new obstacles to catch the guard in a loop
#  brute force - place the obstacles one by one on the already visited points

# Assign to a new variable (create a copy)
visited_positions = set(guard.visited)
loops_counter = 0

final_new_obstacles = []

# ! the new obstacle cannot be placed on the the guard's starting position!

for index, theoretically_new_obstacle in enumerate(visited_positions):
    # print(f" *********** {index} - Adding new obstacle to {theoretically_new_obstacle} ************************")
    # theoretically_new_obstacle = item[0]  # Extract the coordinates (the first element of the tuple)
    new_obstacles = obstacles.copy()  # shallow copy of th list
    new_obstacles.append(theoretically_new_obstacle)

    guard = Guard(*guard_starting_position, "U", new_obstacles, (COLUMNS, ROWS))

    a = 0

    # part 1 - count how many unique position the guard goes through
    while (guard.off_ground is False and guard.guard_in_loop is False):
        guard.move()
        # guard.display_grid()
        # input("enter ... ")
        a += 1

        if guard.guard_in_loop is True:
            # print(f"yes - this position {index} - {theoretically_new_obstacle} leads to a loop.")
            loops_counter += 1
            # guard.display_grid()
            final_new_obstacles.append(theoretically_new_obstacle)
            # input("enter...")
            break

print(' ---------- res -------------')
print()
print(f"There are {loops_counter} possibilities, where to put the obstacle, so that the guard is walking in a loop.")
# print(f"All new obstacles are: {final_new_obstacles}")