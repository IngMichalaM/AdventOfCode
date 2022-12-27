""" Brute force approach.
    Check each "a" position and find the shortes path from it.
    In the end select the shortest .
     It really takes some time to finish. """


import os
import time

filename = os.path.join('inputs', 'day_12.txt')
# filename = os.path.join('inputs', 'day_12_trial.txt')
start_time = time.time()

############### PART 2 ###############################################
with open(filename) as f:
    all_data = [line.strip('\n') for line in f.readlines()]

print(all_data)
num_row = len(all_data)
num_cols = len(all_data[0])
print(f'The size of the map is {num_row} rows and {num_cols} columns.')

def get_letter_number(letter):
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
    return '-'.join([str(row), str(col)])


def get_neighbours(row:int, col:int):
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

    def __init__(self, position:list[int, int], height:int):
        self.position = position
        self.height = height
        if height == 0:
            self.shorthest_path_to_start = 0
        else:
            self.shorthest_path_to_start = 9999999
        self.neighbours = get_neighbours(*position)
        self.name = from_num_get_str_repr(*position)


    def __str__(self):
        return f"""\n\t The node "{self.name}" has positioin {self.position} and height of {self.height}.
        This node has {len(self.neighbours)} neighbours: {self.neighbours}
        Its distance from start is {self.shorthest_path_to_start}."""

def initialize_obj_matrix():
    # prepare the new matrix
    all_data_obj = dict()
    # list of lists of strings to list of list of numbers
    for row_counter, line in enumerate(all_data):
        # splitted_line = line.split()
        # print(splitted_line)
        line_num = []
        for col_counter, letter in enumerate(line):
            current_node = Pos([row_counter, col_counter], get_letter_number(letter))
            all_data_obj[current_node.name] = current_node
    return all_data_obj

all_possible_starting_points = []
# find the starting end end point
for name, pobj in initialize_obj_matrix().items():
    if pobj.height == 0 or pobj.height == 1:
        # start_coor = nem
        all_possible_starting_points.append(name)
    elif pobj.height == 27:
        end_coor = name
        print(f'cooroinates for E are {name}')

print(f'There are {len(all_possible_starting_points)} possible starting points:')
print(all_possible_starting_points)
# time.sleep(30)

res = dict()
# def through_hell(current_node_name):
# current_node_name = '0-0' # trial
# current_node_name = '20-0' # part 1
for counter_start_poinst, start_coor in enumerate(all_possible_starting_points):
    all_data_obj = initialize_obj_matrix()
    all_data_obj[start_coor].shorthest_path_to_start = 0 #
    # print(f' --------- for loop number {counter_start_poinst}, the starting point is: {start_coor} ------')
    current_node_name = start_coor # starting coordinates (string name)
    nodes_to_visit = [all_data_obj[current_node_name]]
    # print(f'Type of the "nodes to visit" is "{type(nodes_to_visit)}".')
    # print(f'Type of the element of nodes_to_visit is "{type(nodes_to_visit[0])}".')
    # print('-------------------')

    counter = 0
    steps = 0
    while nodes_to_visit: # while there are still some nodes unvisited
        # print(f'-------------- round {counter} ---------------------------------------')
        # print(f'Thera are {len(nodes_to_visit)} nodes to visit.')
        # print(f'Type of the "nodes to visit" is "{type(nodes_to_visit)}".')
        # print(f'Type of the element of nodes_to_visit is "{type(nodes_to_visit[0])}".')
        # prin('***')
        steps += 1
        current_node = nodes_to_visit.pop()
        # print(f'Current node is: {current_node} and is of type {type(current_node)}')

        # add its neighbours to to_visit list
        list_of_neighb_coor = current_node.neighbours
        # print(f'\t the neighnouts : {list_of_neighbours} are of type {type(list_of_neighbours)}')
        # nodes_to_visit.append(list_of_neighbours)
        # print(f'Thera are {len(nodes_to_visit)} nodes to visit: {nodes_to_visit}')

        # need to append object not the coordinates
        # only append those that have not yet been visited

        for coor in list_of_neighb_coor:
            name = from_num_get_str_repr(*coor)
            other_neighbour = all_data_obj[name]
            if ((other_neighbour.height - 1) <= current_node.height) and \
                    (other_neighbour.shorthest_path_to_start > current_node.shorthest_path_to_start+1):
                    # (other_neighbour.shorthest_path_to_start > steps): blbost
                other_neighbour.shorthest_path_to_start = current_node.shorthest_path_to_start+1
                # other_neighbour.shorthest_path_to_start = steps
                nodes_to_visit.append(other_neighbour)


        # print('nodes to visit are:')
        # for i in nodes_to_visit:
        #     print('name     -   current distance from start --- ')
        #     print(f'{i.name}  - \t\t{i.shorthest_path_to_start}')
        # input('press something ... ')
        counter+=1

    res[start_coor] = all_data_obj[end_coor].shorthest_path_to_start
    # print(f' ---- end of {counter} round ---')
    # print(f'{start_coor}: {res[start_coor]}')


    # # for name, node in all_data_obj.items():
    # for i in range(num_row):
    #     for j in range(num_cols):
    #         print(all_data_obj[from_num_get_str_repr(i,j)].shorthest_path_to_start,  end = ', ')
    #     print('\n')
    #
    # input('press something ... ')

print('For each starting point present the distance to teh target point: ')
for name, cobj in res.items():
    print(f'{name}: {cobj}')

print(f"Elapsed time is {time.time() - start_time} s.")
