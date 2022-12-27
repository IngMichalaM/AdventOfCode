"""  filesystem problem
    In the end solved using a dictionary, names of files held as the whole path name. """

import os
import time

filename = os.path.join('inputs', 'day_07_a.txt')
start_time = time.time()

# read the whole file, go in a foor loop
with open(filename) as f:
    all_data = [line.strip('\n') for line in f.readlines()]

def file_proces(in_line):
    """ Proccess a file.

        Example of a line with a file:
            4060174 j
            8033020 d.log
            5626152 d.ext
        Return name and size
        There are files with same name, but different extension and size.
        Keep the extension. """

    file_size, file_name_w_ext = in_line.split()
    return file_name_w_ext, file_size

def go_back_one_dir(in_path:str) -> str:
    """ Return the string of the path without the last directory. """
    a = in_path.split('/')
    a.pop()
    return '/'.join(a)

dict_all_dir_and_files = dict()
current_dir = ''

# go throught the data one by one
for line in all_data:
    if line == '$ ls':
        print(f'{line}: \t\t list content.')
    elif 'dir' in line:
        # print(f'{line}: \t\t this is a directory. Apend it to the current folder. ')
        a = line.split()
        path_and_file_name = '/'.join([current_dir, a[-1]])
        dict_all_dir_and_files[path_and_file_name] = {'Size': 0, "Type": "Dir"}
    elif line == '$ cd ..':
        # print(f'{line}: \t\t go back up.')
        current_dir = go_back_one_dir(current_dir)
    elif line == '$ cd /':
        # print(f'{line}: \t\t root level.')
        current_dir = 'root'
        dict_all_dir_and_files[current_dir] = {'Size': 0, "Type": "Dir"}
    elif '$ cd' in line:
        # print(f'{line}: \t\t change directory.')
        a = line.split('$ cd')
        current_dir = '/'.join([current_dir, a[-1].strip()])
    else: #   line[0] not in ['$', "dir"]: # file
        # print(f'{line}: \t\t this is a file.  Apend it to the current folder.')
        file_name_w_ext, file_size = file_proces(line)
        len_file_name = len(file_name_w_ext)

        path_and_file_name = '/'.join([current_dir, file_name_w_ext])

        dict_all_dir_and_files[path_and_file_name] = {'Size': 0, "Type": "File"}
        dict_all_dir_and_files[path_and_file_name]['Size'] = int(file_size)

        # add the size to all upper folders
        while path_and_file_name != 'root':
            path_and_file_name = go_back_one_dir(path_and_file_name)
            dict_all_dir_and_files[path_and_file_name]['Size'] += int(file_size)

print(dict_all_dir_and_files)

print('get the sum of the size of directories , each smaller than 100 000: ')
total_desired_sum = 0
for name, value in dict_all_dir_and_files.items():
    if value["Type"]=="Dir"and value['Size'] < 100000:
        print(f'Directory {name} has value smaller than 100000 ({value["Size"]})')
        total_desired_sum += value['Size']
print(f'The desired sum is: {total_desired_sum}')

print('--------------------------------------------')
total_space = 70000000
# print(dict_all_dir_and_files)
current_unused_space = total_space - dict_all_dir_and_files['root']["Size"]
print(f'Currently unused psace: {current_unused_space}.')
we_need_to_clear = 30000000-current_unused_space
print(f'we_need_to_clear: {we_need_to_clear}')

# find which dir are bigger than we_need_to_clear
the_smallest = ['name', 70000000000]
for name, value in dict_all_dir_and_files.items():
    if value["Type"]=="Dir" and value['Size'] > we_need_to_clear:
        print(f'Directory {name} has the value that we need ({value["Size"]})')
        if value["Size"] < the_smallest[1]:
            the_smallest = (name, value["Size"])

print('***************************************')
print(f'We need to delete the folder {the_smallest[0]} of size {the_smallest[1]}')

print(f"Elapsed time is {time.time() - start_time} s.")

