""" From the provided map of elevations find the shortest path to the top element.
    Kind of shortest path algorithm, but with a pinch of brute force. """


import os
import time
from icecream import ic


# filename = os.path.join('inputs', 'day_0x_a.txt')
filename = os.path.join('inputs', 'day_12_trial.txt')
start_time = time.time()

############### PART 1 ###############################################
with open(filename) as f:
    all_data = [line.strip('\n') for line in f.readlines()]

print(all_data)
num_row = len(all_data)
num_cols = len(all_data[0])
print(f'The size of the map is {num_row} rows and {num_cols} columns.')

def get_letter_number(letter):
    """ Convert the map of letters to map of numbers  """

    if letter == 'S':
        return 0
    elif letter == 'E':
        return 27
    try:
        lower_case_letters = 'abcdefghijklmnopqrstuvwxyz'
        return lower_case_letters.index(letter)+1
    except:
        print('Unknown character ')

def from_num_get_str_repr(row:int, col:int):
    """ Coordinates are represented as a string of the coordinates;
        used as the key in the dict """

    return '-'.join([str(row), str(col)])

def get_neighbours(row:int, col:int) -> list:
    """ Return the neighbours of the given coordinates. """

    my_neighbours = []
    #left
    if col>0:
        left_neight = [row, col-1]
        my_neighbours.append(left_neight)
    # right
    if col< (num_cols-1):
        right_neigh = [row, col+1]
        my_neighbours.append(right_neigh)
    # up
    if row > 0:
        up_neigh = [row-1, col]
        my_neighbours.append(up_neigh)
    # down
    if row < (num_row-1):
        down_neigh = [row+1, col]
        my_neighbours.append(down_neigh)

    return my_neighbours

class Pos():
    """ For each coordinates (position) create an instance containing its
        - position
        - height
        - shortest path to the start point
        - list of neighbours
        - name (string of the coordinates, unique)
        - repr method """

    def __init__(self, position:list[int, int], height:int):
        self.position = position
        self.height = height
        if height == 0:
            self.shorthest_path_to_start = 0
        else:
            self.shorthest_path_to_start = 9999999 # pick a really big number
        self.neighbours = get_neighbours(*position)
        self.name = from_num_get_str_repr(*position)

    def __str__(self):
        return f"""\n\t The node "{self.name}" has positioin {self.position} and height of {self.height}.
        This node has {len(self.neighbours)} neighbours: {self.neighbours}
        Its distance from start is {self.shorthest_path_to_start}."""

# prepare the new matrix
all_data_obj = dict()

# list of lists of strings to list of list of numbers
for row_counter, line in enumerate(all_data):
    line_num = []
    for col_counter, letter in enumerate(line):
        current_node = Pos([row_counter, col_counter], get_letter_number(letter))
        all_data_obj[current_node.name] = current_node


def through_hell(current_node_name):
    current_node = all_data_obj[current_node_name]

    while  current_node.neighbours:
     # for neighbour_node_pos in current_node.neighbours:
        neighbour_node_pos = current_node.neighbours.pop()

        neighbour_node_name = from_num_get_str_repr(*neighbour_node_pos)
        print(neighbour_node_name)
        # input('press something ... ')
        neighbour_node = all_data_obj[neighbour_node_name]

        # check the height , if I can go there
        if neighbour_node.height <= current_node.height+1:
            print(f'The neighbour node is max by one bigger. Neighbour node height {neighbour_node.height}, current height {current_node.height}')
            # than I can go there

            # check that mine distance is shorter than the distance on that node
            if current_node.shorthest_path_to_start < neighbour_node.shorthest_path_to_start:
                # it is ok to go there
                neighbour_node.shorthest_path_to_start = current_node.shorthest_path_to_start + 1
                current_node_name = neighbour_node.name
                through_hell(current_node_name)
        else:
            # I cannot continue in this direction
            return

current_node_name = '0-0'
# print(all_data_obj[start])

through_hell(current_node_name)

for name, theobj in all_data_obj.items():
    print(theobj)


print(f"Elapsed time is {time.time() - start_time} s.")
