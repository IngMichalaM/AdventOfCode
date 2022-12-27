""" The snake """

import os
import time
import math


filename = os.path.join('inputs', 'day_09_a.txt')
#filename = os.path.join('inputs', 'day_09_trial.txt')
start_time = time.time()

# read all the data
with open(filename) as f:
    all_data = [line.strip('\n') for line in f.readlines()]


def display_canvas(head_position, tail_position):
    """ Just for testing purposes. Just pure display of the list of lists. """
    return
    adj_zero = 10
    canvas = []
    for i in range(20):  # raDKY
        line = []
        for j in range(20):
            if j == adj_zero:
                line.append('|')
            elif i == adj_zero:
                line.append('-')
            else:
                line.append('.')
        canvas.append(line)

    head_x, head_y = head_position
    tail_x, tail_y = tail_position
    print(f'Head coor is [{head_x},{head_y}], tails coor is [{tail_x},{tail_y}].')

    canvas[head_y+adj_zero][head_x+adj_zero] = 'H'
    canvas[tail_y+adj_zero][tail_x+adj_zero] = 'T'

    for i in canvas:
        print(i)

    input('press something ... ')

class Tail():
    """ Class Tail contains the definition of the tail, its x and y coordinates.
        Methods to move up, down, left, right and diagonally, each call by one.
        Method distance - calculates the distance between head and tail. """
    def __init__(self):
        self.x = 0
        self.y = 0
        self.visited_nodes = []

    def distance(self, head_position:list):
        """ Calculate abolute distance between head and tail. """
        head_x, head_y = head_position
        return math.sqrt((head_x-self.x)**2+(head_y-self.y)**2)

    # tail always moves only by one (or diagonaly one)
    def moveR(self):
        self.x += 1
    def moveRU(self):
        self.x += 1
        self.y += 1
    def moveRD(self):
        self.x += 1
        self.y -= 1
    def moveL(self):
        self.x -=1
    def moveLU(self):
        self.x -= 1
        self.y +=1
    def moveLD(self):
        self.x -= 1
        self.y -= 1
    def moveU(self):
        self.y += 1
    def moveD(self):
        self.y -= 1


class Head():
    """ Class Head contains the definition of the head, its x and y coordinates.
        Methods to move up, down, left, right, each call by one. """

    def __init__(self):
        self.x = 0
        self.y = 0

    def move(self, direction_of_move):
        """ Move by one in the given direction. """

        if direction_of_move == 'R':           # right
            self.x += 1
        elif direction_of_move == 'L':         # left
            self.x -= 1
        elif direction_of_move == 'U':         # up
            self.y += 1
        elif direction_of_move == 'D':    # down
            self.y -= 1
        else:
            raise ValueError('Unknown direction')


tail = Tail()
head = Head()
for line in all_data:
    # print(f'-------------- line: {line} ------------' )
    # head.move(line)
    # head.move('R 4')
    direction, num_steps = line.split();
    num_steps = int(num_steps)

    if direction == 'R':   # right
        x_head_start = head.x
        x_head_end = x_head_start + num_steps
        head_nodes = [[i, head.y] for i in list(range(x_head_start, x_head_end + 1))]

        for coor in head_nodes:
            # for each move of the head check that the distance of the head and tail is <= 1
            # it can be 0, 1 or bigger. When it is bigger, the tail needs to move
            # print(f'Head coor is [{coor[0]},{coor[1]}], tails coor is [{tail.x},{tail.y}].')
            dist_tail_head = tail.distance(coor)

            if dist_tail_head <= 1.5: # (to include the diagonal position, which is still ok )
                #  print('The tail does not need to move ')
                pass
            else:
                # print('The tail NEEDS to move ')
                if coor[1] > tail.y:
                    # the tail needs to move diagonally up
                    tail.moveRU()
                elif coor[1] == tail.y:
                    # the tail is on the same y level as head, only needs to move to the right straight
                    tail.moveR()
                else:
                    # move diagonally down
                    tail.moveRD()
            #     print(f'\tTail moved to [{tail.x},{tail.y}]')
            # print('Tails visited nodes ')
            tail.visited_nodes.append((tail.x, tail.y))
            display_canvas(coor, [tail.x, tail.y])

        # move the head as well
        head.x, head.y = coor

    elif direction == 'L':    # left
        x_head_start = head.x
        x_head_end = x_head_start - num_steps
        head_nodes = [[i, head.y] for i in list(range(x_head_start, x_head_end -1, -1))]
        #   print(head_nodes)
        for coor in head_nodes:
            #     print(f'Head coor is [{coor[0]},{coor[1]}], tails coor is [{tail.x},{tail.y}].')
            dist_tail_head = tail.distance(coor)
            if dist_tail_head <= 1.5: # (to include the diagonal position, which is still ok )
                #   print('The tail does not need to move ')
                pass
            else:
                #  print('The tail NEEDS to move ')
                if coor[1] > tail.y:
                    # the tail needs to move diagonally up
                    tail.moveLU()
                elif coor[1] == tail.y:
                    # the tail is on the same y level as head, only needs to move to the right straight
                    tail.moveL()
                else:
                    # move diagonally down
                    tail.moveLD()
            #    print(f'\tTail moved to [{tail.x},{tail.y}]')
            tail.visited_nodes.append((tail.x, tail.y))
            display_canvas(coor, [tail.x, tail.y])

       # move the head as well
        head.x, head.y = coor

    elif direction == 'U':         # up
        y_head_start = head.y
        y_head_end = y_head_start + num_steps
        head_nodes = [[head.x, i] for i in list(range(y_head_start, y_head_end +1))]
        for coor in head_nodes:
            #     print(f'Head coor is [{coor[0]},{coor[1]}], tails coor is [{tail.x},{tail.y}].')
            dist_tail_head = tail.distance(coor)
            if dist_tail_head <= 1.5:  # (to include the diagonal position, which is still ok )
                #        print('The tail does not need to move ')
                pass
            else:
                #     print('The tail NEEDS to move ')
                if coor[0] > tail.x:
                    # the tail needs to move diagonally up
                    tail.moveRU()
                elif coor[0] == tail.x:
                    # the tail only needs to go up
                    tail.moveU()
                else:
                    # move diagonally up right
                    tail.moveLU()
             #  print(f'\tTail moved to [{tail.x},{tail.y}]')
            tail.visited_nodes.append((tail.x, tail.y))
            display_canvas(coor, [tail.x, tail.y])

        # move the head as well
        head.x, head.y = coor

    elif direction == 'D':          # down
        y_head_start = head.y
        y_head_end = y_head_start - num_steps
        head_nodes = [[head.x, i] for i in list(range(y_head_start, y_head_end - 1, -1))]
       # print(head_nodes)
        for coor in head_nodes:
            #      print(f'Head coor is [{coor[0]},{coor[1]}], tails coor is [{tail.x},{tail.y}].')
            dist_tail_head = tail.distance(coor)
            if dist_tail_head <= 1.42:  # check  (to include the diagonal position, which is still ok )
                #       print('The tail does not need to move ')
                pass
            else:
                #       print('The tail NEEDS to move ')
                if coor[0] > tail.x:
                    # the tail needs to move diagonally down
                    tail.moveRD()
                elif coor[0] == tail.x:
                    # the tail only needs to go down
                    tail.moveD()
                else:
                    # move diagonally down rleft
                    tail.moveLD()
             #   print(f'\tTail moved to [{tail.x},{tail.y}]')
            tail.visited_nodes.append((tail.x, tail.y))
            display_canvas(coor, [tail.x, tail.y])

        # move the head as well
        head.x, head.y = coor # do not go the the last coordinates ()
    else:
        raise ValueError('Unknown direction')

# ----------------------------------
# print('All visited nodes')
# print(tail.visited_nodes)
unique_nodes = set(tail.visited_nodes)
# print('unique nodes:')
# print(unique_nodes)
print(f'There are {len(unique_nodes)} unique nodes ')
