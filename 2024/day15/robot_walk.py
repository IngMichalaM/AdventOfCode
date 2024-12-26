
class Robot:
    def __init__(self, robot_position, robot_direction, walls, boxes, grid_size):

        self.x = robot_position[0]
        self.y = robot_position[1]
        self.direction = robot_direction
        self.walls = walls
        self.boxes = boxes
        self.grid_size = grid_size  # tuple width-x (column wise), heigh -y (row wise)
        self.grid = [['.' for _ in range(grid_size[0])] for _ in range(grid_size[1])]
        self._initialize_grid()
        self.robot_can_move = False
        self.box_can_move = False

    def __str__(self):
        return f"Robot is at the position ({self.x},{self.y}), heading '{self.direction}'."

    def display_grid(self):
        print()
        for row in self.grid:
            print(''.join(row))

    def _initialize_grid(self):

        for box in self.boxes:
            x, y = box
            self.grid[y][x] = 'O'

        for wall in self.walls:
            x, y = wall
            self.grid[y][x] = '#'

        self.grid[self.y][self.x] = "@"

    def _can_box_move(self, box_x, box_y):
        """ For the current position [box_x, box_y] of the box
            check if in the current direction there is a box or a wall or an empty space """

        next_x_box, next_y_box = self.next_position(box_x, box_y)

        if (next_x_box, next_y_box) in self.walls:
            #   print('There is a wall in front of the box. Cannot move the box and neither can the robot itself.')
            return False
        elif (next_x_box, next_y_box) in self.boxes:
            #   print('There is a box in front of the box. What now?')

            can_box_move = self._can_box_move(next_x_box, next_y_box)

            if can_box_move:
                # if the box can move, then all the boxes can move and the robot as well
                #   print(f"Moving the box from {box_x, box_y} to {next_x_box, next_y_box}")
                self._update_grid((box_x, box_y), (next_x_box, next_y_box), 'O')
                return True
            else:
                return False
        else:
            #  print("There is a free space, the box can be moved.")
            #  print(f"Moving the box from {box_x, box_y} to {next_x_box, next_y_box}")
            self._update_grid((box_x, box_y), (next_x_box, next_y_box), 'O')
            return True

    def position(self):
        """ Return the actual position of the robot """
        return self.x, self.y

    def change_direction(self, new_direction):
        """ new_direction >, <, v, ^ """

        valid_direction = {'>', '<', 'v', '^'}

        if new_direction in valid_direction:
            self.direction = new_direction
        else:
            print("Invalid direction.")

    def next_position(self, position_x, position_y):
        # print(f"current position {position_x, position_y}")
        if self.direction == '^':
            position_y -= 1
        elif self.direction == '>':
            position_x += 1
        elif self.direction == 'v':
            position_y += 1
        elif self.direction == '<':
            position_x -= 1
        # print(f"next position {position_x, position_y}")
        return position_x, position_y

    def move_robot(self):
        """ Move the robot one step in the current direction """

        next_x, next_y = self.x, self.y
        next_x, next_y = self.next_position(next_x, next_y)

        if (next_x, next_y) in self.walls:
            # print('There is a wall in front of the robot. Cannot move')
            self.robot_can_move = False
        elif (next_x, next_y) in self.boxes:
            # print('There is a box in front of the robot. What now?')

            can_box_move = self._can_box_move(next_x, next_y)
            if can_box_move:
                self.robot_can_move = True
            else:
                self.robot_can_move = False
        else:
            self.robot_can_move = True

        if self.robot_can_move:
            self._update_grid((self.x, self.y), (next_x, next_y), '@')
            self.x, self.y = next_x, next_y

    def _update_grid(self, old_position, new_position, sign_char):

        if sign_char == 'O':
            self.boxes.remove(old_position)
            self.boxes.add(new_position)

        self.grid[old_position[1]][old_position[0]] = '.'
        self.grid[new_position[1]][new_position[0]] = sign_char