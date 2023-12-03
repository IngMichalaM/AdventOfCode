# day 1, part 1 - find first and last number in a strings

filename = 'input.txt'

with open(filename) as f:
    input = [line.strip('\n') for line in f.readlines()]

res_num = []
for line in input:
    num = ""

    for c in line:
        if c.isdigit():
            num = num + c

    num2 = num[0] + num[-1]
    res_num.append(int(num2))

print(sum(res_num))
