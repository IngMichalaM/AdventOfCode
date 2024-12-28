"""
 - The BFS works fine for the two examples, but is too costly for the full-scale problem. Could not return result
    even after 1 hour :D
 - Switched to Dijkstra algorithm instead, but this one is beyond my knowledge :-), so chatGPT helped a lot.
 - From the chatGPT solution I needed to adjust the start and end point to be parametrized, corrected the price counting
    during the turn, added the display method.
 - This solution does not calculate properly the cost of turning 180 degrees. Would need some more adjustments.
        But this situation does not occur in the given example, so I am not doing it now.
"""

import heapq
from typing import List, Tuple

# get the settings
# small example: "input/input_test.txt",  example 2: "input/example2.txt", full scale: "input/inputA.txt"
file_path = "input/example2.txt"
with open(file_path) as f:
    maze = [list(line.strip('\n')) for line in f.readlines()]


def get_start_end(grid: List[str]):
    """ Find the starting position of the raindeer and the target position. """
    for row_index, row in enumerate(grid):
        for col_index, char in enumerate(row):
            if char == "S":
                start_position = (row_index, col_index)
            elif char == "E":
                end_position = (row_index, col_index)

    return start_position, end_position


# Directions: [Up, Right, Down, Left]
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # (dx, dy)
DIRECTION_NAMES = ["Up", "Right", "Down", "Left"]


# Function to check if the position is within the maze bounds
def in_bounds(x, y, maze):
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == '.'


# Dijkstra's algorithm to find the cheapest path from start to the end
def dijkstra_with_path(maze, start, end):
    # Rows and columns of the maze
    rows, cols = len(maze), len(maze[0])

    # Unpack the start and end positions
    start_x, start_y, start_direction = start  # Starting position and direction

    # Priority queue: stores (cost, x, y, direction)
    pq = []

    # Start
    heapq.heappush(pq, (0, start_x, start_y, start_direction))  # (cost, x, y, direction)

    # Cost map: a 3D array to store the minimum cost to reach (x, y) with a specific direction
    cost = [[[float('inf')] * 4 for _ in range(cols)] for _ in range(rows)]
    cost[start_x][start_y][start_direction] = 0

    # Parent map: to reconstruct the path
    parent = {}

    while pq:
        current_cost, x, y, direction = heapq.heappop(pq)

        # If we reached the end position, reconstruct and return the path
        if (x, y) == end:
            return reconstruct_path(parent, start_x, start_y, x, y, direction), current_cost

        # 1. Check moving straight (no rotation)
        dx, dy = DIRECTIONS[direction]
        nx, ny = x + dx, y + dy

        if in_bounds(nx, ny, maze) and current_cost + 1 < cost[nx][ny][direction]:
            cost[nx][ny][direction] = current_cost + 1
            heapq.heappush(pq, (cost[nx][ny][direction], nx, ny, direction))
            parent[(nx, ny, direction)] = (x, y, direction)  # Track parent

        # 2. Check rotating to a new direction (rotation costs 1000)
        for new_direction in range(4):
            if new_direction != direction:  # Don't rotate to the same direction
                dx, dy = DIRECTIONS[new_direction]
                nx, ny = x + dx, y + dy
                if in_bounds(nx, ny, maze) and current_cost + 1000 < cost[nx][ny][new_direction]:
                    cost[nx][ny][new_direction] = current_cost + 1001
                    heapq.heappush(pq, (cost[nx][ny][new_direction], nx, ny, new_direction))
                    parent[(nx, ny, new_direction)] = (x, y, direction)  # Track parent

    # If there's no path, return None
    return None, -1


# Function to reconstruct the path from the parent map
def reconstruct_path(parent, start_x, start_y, end_x, end_y, end_direction):
    path = []
    current = (end_x, end_y, end_direction)

    # Backtrack from end to start using the parent dictionary
    while current in parent:
        path.append((current[0], current[1], DIRECTION_NAMES[current[2]]))
        current = parent[current]

    # Add the starting position explicitly
    path.append((start_x, start_y, DIRECTION_NAMES[1]))  # Start facing right
    path.reverse()  # Reverse the path to get the correct order
    return path


def path_with_color(maze, path):
    """ For a colorful display of the maze with the path. """
    # ANSI escape codes for colors
    COLOR_X = '\033[92m'  # Green
    COLOR_RESET = '\033[0m'  # Reset to default

    # Create a new representation of the maze with colors
    colored_path = []

    for i in range(len(maze)):
        colored_row = []
        for j in range(len(maze[0])):
            if (i, j) in path:
                colored_row.append(f"{COLOR_X}x{COLOR_RESET}")  # Add colored 'x'
            else:
                colored_row.append(maze[i][j])  # Keep walls and unvisited cells unchanged
        colored_path.append(colored_row)

    return colored_path

def display_grid(grid):
    print()
    for row in grid:
        print(' '.join(row))

start_position, end_position = get_start_end(maze)
start_position = start_position + (1,)  # add the starting direction - heading east/right
print(f"{start_position=}")
print(f"{end_position=}")

# substitute E and S with empty space '.'
maze[start_position[0]][start_position[1]] = '.'
maze[end_position[0]][end_position[1]] = '.'
display_grid(maze)
input("Enter ...")

# Few words about the directions (for slower learners :D), Luckily, chatGPT does not judge.
# See DIRECTIONS and DIRECTION_NAMES
# This defines the possible movement directions in the maze:
# Index 0: (-1, 0) represents moving "Up" (decrease row index).
# Index 1: (0, 1) represents moving "Right" (increase column index).
# Index 2: (1, 0) represents moving "Down" (increase row index).
# Index 3: (0, -1) represents moving "Left" (decrease column index).

path, cost = dijkstra_with_path(maze, start_position, end_position)
print(f"Cheapest Path Cost: {cost}")
print("Path Taken:")

path_cells = []
for step in path:
    x, y, direction = step
    path_cells.append((x, y))

colored_path = path_with_color(maze, path_cells)
display_grid(colored_path)

# Cheapest Path Cost: 72400