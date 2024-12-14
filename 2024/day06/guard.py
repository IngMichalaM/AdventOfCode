

def guard_repr_sign(direction):
    guard_signs = {'U': '^',
                   'R': '>',
                   'D': 'v',
                   'L': '<'}

    return guard_signs[direction]


class Guard:
    def __init__(self, x, y, direction, obstacles, grid_size):
        """
        x: axtual position, along column
        y: actual position, along rows
        direction: direction of the guard Up, Right, Down, Left

        """

        self.x = x
        self.y = y
        self.direction = direction
        self.guard = guard_repr_sign(direction)  # '^', '>', 'v','<'
        self.obstacles = obstacles
        self.obstacle_hits = {obstacle: {'U': 0, 'R': 0, 'D': 0, 'L': 0} for obstacle in obstacles}
        self.grid_size = grid_size  # tuple width-x (column wise), heigh -y (row wise)
        self.off_ground = False  # track if the guard has left the ground
        self.visited = set()  # track all visited position
        self.unique_visits = 0  # unique visited positions
        self._update_visited()
        self.visited_states = set()  # track visited positions together with the direction in which they were visited
        self.grid = [['.' for _ in range(grid_size[0])] for _ in range(grid_size[1])]
        self._initialize_grid()
        self.guard_in_loop = False

    def __str__(self):
        return f"Guard is at the position ({self.x},{self.y}), heading {self.direction} ({self.guard})."

    def display_grid(self):

        for row in self.grid:
            print(''.join(row))

    def _initialize_grid(self):
        for obstacle in self.obstacles:
            x, y = obstacle
            self.grid[y][x] = '#'  # obstacles

        self.grid[self.y][self.x] = self.guard  # guard's initial position

    def _update_grid(self):
        self.grid[self.y][self.x] = 'X'  # visited

    def _update_guard(self):
        self.grid[self.y][self.x] = self.guard

    def move(self):
        """ Move the guard one step in the current direction """
        self.grid[self.y][self.x] = self.guard

        if self.off_ground:
            print("Guard cannot move. He is off the ground.")
            return

        # check the loop before moving
        current_state = ((self.x, self.y), self.direction)
        if current_state in self.visited_states:
            self.guard_in_loop = True
            # print(f"guard is stuck in a loop ... yes!")
            return
        else:
            self.visited_states.add(current_state)

        next_x, next_y = self.x, self.y

        if self.direction == 'U':
            next_y -= 1
        elif self.direction == 'R':
            next_x += 1
        elif self.direction == 'D':
            next_y += 1
        elif self.direction == 'L':
            next_x -= 1

        # check if the next position is off the ground
        if next_x < 0 or next_y < 0 or next_x >= self.grid_size[0] or next_y >= self.grid_size[1]:
            # print("Guard is leaving the ground ")
            self.off_ground = True
        elif (next_x, next_y) in self.obstacles:
            # print(f"Obstacle in the way")
            # print(f"Turn right")
            self.turn_right()
        else:
            self._update_grid()
            self.x, self.y = next_x, next_y
            self._update_guard()

        self._update_visited()

    def _update_visited(self):
        current_position = (self.x, self.y)
        if current_position not in self.visited:
            self.visited.add(current_position)
            self.unique_visits += 1

    def turn_right(self):
        """ Turn right after hiting the obstacle """

        directions = ['U', 'R', 'D', 'L']
        current_index = directions.index(self.direction)
        self.direction = directions[(current_index + 1) % 4]
        self.guard = guard_repr_sign(self.direction)

    # not used in the end
    # def change_direction(self, new_direction):
    #     """ new_direction U, R, D, L """
    #
    #     valid_direction = {'U', 'R', 'D', 'L'}
    #
    #     if new_direction in valid_direction:
    #         self.direction = new_direction
    #     else:
    #         print("Invalid direction.")

    def position(self):
        """ Return the actual position of the guard """
        return self.x, self.y
