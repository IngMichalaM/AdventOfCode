"""
Solution for Day 16 Part A

Walk through the maze - based on depth-first search (DFS)
or breadth-first search (BFS) as basic algorithms.

I did today´s solution with the help of chatGPT :-)
Lessons learned:
 - depth-first search (DFS) algorithm
 - breadth-first search (BFS) algorithm
 - chaining return statement
 - easy copy of a list
 - deque vs list
 - stack vs queue

 -> The BFS works fine for the two examples, but is too costly for the full-scale problem. Could not return result
    even after 1 hour :D
 -> switch to Dijkstra algorithm instead, but this one is beyond my knowledge :-), so chatGPT helped a lot.
"""
import time
from collections import deque
from typing import List, Tuple

# get the settings
file_path = "input/example2.txt"  # small example: "input/input_test.txt",  example 2: "input/example2.txt", full scale: "input/inputA.txt"
with open(file_path) as f:
    maze = [list(line.strip('\n')) for line in f.readlines()]


def display_grid(grid):
    print()
    for row in grid:
        print(' '.join(row))


def get_start_end(grid: List[str]):
    """ Find the starting position of the raindeer (S) and the target position (E). """
    for row_index, row in enumerate(grid):
        for col_index, char in enumerate(row):
            if char == "S":
                start_position = (row_index, col_index)
            elif char == "E":
                end_position = (row_index, col_index)

    return start_position, end_position


def is_valid_move(maze, x, y, current_path):
    """
    Check if the move is valid.

    maze: 2D list that represents the maze.
            '.' - navigable paths
            '#' - walls (or any other char)
    x and y: cell in the maze to be validated.
            x - row index
            y - column index
    Verifies that:
        - The cell is within bounds of the maze (0 <= x < len(maze) and 0 <= y < len(maze[0])).
        - The cell is a path (maze[x][y] == '.').
        - The cell has not been visited in the current path.
    """
    return (
            0 <= x < len(maze) and
            0 <= y < len(maze[0]) and
            maze[x][y] == '.' and
            (x, y) not in current_path
    )


def calculate_price(path: List[Tuple[int]]):
    """
    Calculate the price of a given path.
    - Moving straight: price = 1
    - Turning: price = 1000 (turn and move = 1001)
    """

    # starting facing east (right) - if the path does not start to the right, need to turn
    orig_dir = (0, 1)  # east / right
    first_step_dir = (path[1][0] - path[0][0], path[1][1] - path[0][1])

    if orig_dir == first_step_dir:
        price = 0
    else:
        price = 1000

    for i in range(1, len(path) - 1):
        prev = path[i - 1]
        curr = path[i]
        next_ = path[i + 1]

        # Determine direction of movement
        prev_dir = (curr[0] - prev[0], curr[1] - prev[1])
        next_dir = (next_[0] - curr[0], next_[1] - curr[1])

        if prev_dir == next_dir:
            price += 1  # Straight move
        else:
            price += 1001  # Turn + move

    price += 1  # Add price for the final move to the end
    return price


def find_all_paths_bfs(maze: List[List[int]], start: Tuple[int], end: Tuple[int]):
    """
    Finds all possible paths through the maze using BFS. TOO COSTLY FOR A BIGGER AND COMPLEX MAZE !!!
    :param maze: 2D list representing the maze
    :param start: Starting position (x, y)
    :param end: Ending position (x, y)
    :return: List of all paths found along with their prices.

    Used visited to keep track of the visited cells, but doing that we omitted some of the possible paths
    that have same parts with other paths. Need to check in is_valid_move whether the cell is already in
    this particular path.
    """
    queue = deque([[start]])  # Queue of paths
    all_paths_with_prices = []
    all_prices = []

    while queue:
        path = queue.popleft()
        x, y = path[-1]  # Current position

        if (x, y) == end:
            price = calculate_price(path)
            all_prices.append(price)
            all_paths_with_prices.append((path, price))
            continue

        # Explore neighbors
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid_move(maze, nx, ny, path):
                new_path = path + [(nx, ny)]
                queue.append(new_path)

    return all_paths_with_prices, all_prices


def path_with_color(maze, path):
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

# -----------------------------------------

start, end = get_start_end(maze)
print(f"{start=}")
print(f"{end=}")
# display_grid(maze)

# substitute E and S with empty space '.'
maze[start[0]][start[1]] = '.'
maze[end[0]][end[1]] = '.'
# display_grid(maze)
# input("press enter to contitnue ")

all_paths_with_prices, all_prices = find_all_paths_bfs(maze, start, end)
min_price = min(all_prices)
print(f"The best price is {min_price}")

if all_paths_with_prices:
    print(f"Found {len(all_paths_with_prices)} paths:")
    for i, (path, price) in enumerate(all_paths_with_prices, 1):
        # print(f"Path {i}: {path}, Price: {price}")
        if price == min_price:
            colored_path = path_with_color(maze, path)
            display_grid(colored_path)
else:
    print("No paths found.")