import math
import os
import time

# https://adventofcode.com/2022/day/11

filename = os.path.join('inputs', 'day_11_a.txt')
# filename = os.path.join('inputs', 'day_11_trial.txt')
start_time = time.time()

############### PART 1 ###############################################
with open(filename) as f:
    all_data = f.readlines()

# choose the part to solve
# partnum = 'part1'
partnum = 'part2'

# print(f'there are {math.floor(len(all_data)/6)} monkeyes ')
monkeys = []
step = 7

# get the instructions from the input file
for counter in range(0, len(all_data), step):
    monkeys.append(all_data[counter:counter+step])

class Monkey():
    """ Each monkey is represented by an instance of Monkye class.
        Monkey has a name, list of items she posses, the operation she does with the operand,
        what is her test to do, etc. """
    def __init__(self, name, items, operation_type, operation_value, test_divisible_by,
                 T_throw_to_monkey_num, F_throw_to_monkey_num):
        self.name = name
        self.items = items
        self.operation_type = operation_type
        self.operation_value = operation_value
        self.test_divisible_by = test_divisible_by
        self.if_test_true_throw_to = T_throw_to_monkey_num
        self.it_test_false_throw_to = F_throw_to_monkey_num
        self.num_of_inspected_items = 0 # len(items)

    def __str__(self):
        return f"""  ----   ----   ---- {self.name} ---   ----   ----
                    Items: {self.items}
                    Operation_type: {self.operation_type}
                    Operation_value: {self.operation_value}
                    Divisible by: {self.test_divisible_by}
                    If test true throw to: {self.if_test_true_throw_to}
                    If test false throw to: {self.it_test_false_throw_to}
                    Number of inspected items: {self.num_of_inspected_items}
                        ---- """

    def operation(self, old_item):
        # carefull with operation value 'old' - that would be multiplication of the old
        if self.operation_value == 'old':
            if self.operation_type == '*':
                return old_item * old_item
            elif self.operation_type == '+':
                return old_item + old_item

        if self.operation_type == '*':
            new_item = old_item * self.operation_value
        elif self.operation_type == '+':
            new_item = old_item + self.operation_value

        return new_item

# create a dict of monkeys
all_monkeys_dict_of_obj = dict()

for monkey in monkeys:
    for line in monkey:
        line = line.strip()
        if 'Monkey' in line:
            monkey_name = line.strip(":")
        elif 'Starting items:' in line:
            # expect at least one item (checked visually that thera are)
            _, items_strings = line.split(":")
            items_num = [int(i) for i in items_strings.split(",")]
        elif 'Operation' in line:
            the_operation_type_line = line.split()
            operation_type = the_operation_type_line[-2]
            value_for_operation =  the_operation_type_line[-1]
            if value_for_operation != 'old':
                value_for_operation = int(value_for_operation)
        elif 'Test' in line:
            # always divisible (checked visualy)
            _, _, _, divisible_by_num = line.split()
        elif 'If true' in line:
            line_splited = line.split()
            T_throw_to_monkey_num =  ' '.join(line_splited[-2:]).capitalize()
        elif 'If false' in line:
            line_splited = line.split()
            F_throw_to_monkey_num =  ' '.join(line_splited[-2:]).capitalize()

    all_monkeys_dict_of_obj[monkey_name] = Monkey(monkey_name, items_num, operation_type, value_for_operation, int(divisible_by_num),
                                                  (T_throw_to_monkey_num), (F_throw_to_monkey_num))

list_of_monkeys = [monkey_name for monkey_name, _ in all_monkeys_dict_of_obj.items()]
# print(list_of_monkeys) # - do the for loop over  this

# najit spolecenho nemjmensio nasobku toho testu
list_of_test_val = [monk_obj.test_divisible_by for _, monk_obj in all_monkeys_dict_of_obj.items()]
print(list_of_test_val)
spolecny_nasobek = 1
for i in list_of_test_val:
    spolecny_nasobek = spolecny_nasobek*i
print(f'spolecny_nasobek={spolecny_nasobek}')

# def_num_rounds = 20 # for part 1
def_num_rounds = 10000  # for part 2 (and no division by 3)

for round_counte in range(1,def_num_rounds+1):
    # print()
    # if round_counte in [1,2,20,21,1000, 1001, 2000] or round_counte%100==0:
        # print(f'=============== Round {round_counte} =========================')
        # print()
        # print(f'-- list of items for individual monkeys in teh beginning of {round_counte} round ---')
        # print()
        # for mmmm in list_of_monkeys:
        #     print(f'{mmmm} has items: {all_monkeys_dict_of_obj[mmmm].items}')
        #     print(f'\t Number of inspected items: {all_monkeys_dict_of_obj[mmmm].num_of_inspected_items} ')
        # input('press ... ')

    for monkey_name, monkey_object in all_monkeys_dict_of_obj.items():
       # print(monkey_object)
        # loop over teh items in the items_list
        # for item in monkey_object.items:
        while monkey_object.items: # until it is empty
            item = monkey_object.items.pop(0)
          #  print(f'Current item that was removed {item}')
            # now we have the first item in the list - do
            operation_res = monkey_object.operation(item)
            monkey_object.num_of_inspected_items += 1
           # print(f'Result after the operations: {operation_res}')
            if partnum == 'part1':
                operation_res = math.floor(operation_res/3)
                # we dont do this for part2

           # print(f'Result after the division by 3: {operation_res}')
            if operation_res > spolecny_nasobek:
                # print(f'===== Round {round_counte} =========================')
                # print(f'operation_res before adjustment: {operation_res}')

               # if operation_res%spolecny_nasobek==0:
                operation_res = operation_res%spolecny_nasobek
                # else:
                #     operation_res = operation_res-spolecny_nasobek

                # print(f'operation_res after adjustment: {operation_res}')

            if operation_res%monkey_object.test_divisible_by == 0: # it is divisible
                # do the if true - append the value to the defined monkey
                all_monkeys_dict_of_obj[monkey_object.if_test_true_throw_to].items.append(operation_res)
                #print(f'The worry level {operation_res} goes to the monkey {monkey_object.if_test_true_throw_to}, who has now these items: {all_monkeys_dict_of_obj[monkey_object.if_test_true_throw_to].items}')
                # count the item
                # all_monkeys_dict_of_obj[monkey_object.if_test_true_throw_to].num_of_inspected_items+=1
            else:
                # do the if false
                all_monkeys_dict_of_obj[monkey_object.it_test_false_throw_to].items.append(operation_res)
                #print(f'The worry level {operation_res} goes to the monkey {monkey_object.it_test_false_throw_to} , who has now these items: {all_monkeys_dict_of_obj[monkey_object.it_test_false_throw_to].items}')
                # all_monkeys_dict_of_obj[monkey_object.if_test_true_throw_to].num_of_inspected_items += 1

print()
print(f'-- list of items for individual monkeys after {round_counte} rounds ---')
print()
for mmmm in list_of_monkeys:
    print(f'{mmmm} has items: {all_monkeys_dict_of_obj[mmmm].items}')
    print(f'\t Number of inspected items: {all_monkeys_dict_of_obj[mmmm].num_of_inspected_items} ')
# input('press ... ')

list_of_howmoc_inspected = [all_monkeys_dict_of_obj[mmmm].num_of_inspected_items for mmmm in list_of_monkeys]
print((list_of_howmoc_inspected))
list_of_howmoc_inspected.sort(reverse=True)
print(list_of_howmoc_inspected)
print(' Multiply the two most acive monkeys.')
print(f'The res: {list_of_howmoc_inspected[0]*list_of_howmoc_inspected[1]}')
print(f"Elapsed time is {time.time() - start_time} s.")
