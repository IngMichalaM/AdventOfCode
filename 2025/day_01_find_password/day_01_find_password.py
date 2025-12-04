# https://adventofcode.com/2025/day/1

with open("input_example.txt") as f:
# with open("real_input.txt") as f:
    my_input = [line.strip('\n') for line in f.readlines()]


def find_password(my_input: list[str], position: int = 50) -> tuple[int, int]:
    zero_counter = 0

    for i in my_input:
        direction = i[0]
        distance = int(i[1:])

        if direction == 'L':
            if position - distance < 0:
                position = position - distance + 100
                while position < 0:
                    position += 100
            else:
                position -= distance
        else:  # direction == 'R'
            if position + distance > 99:
                position = (position + distance) - 100
                while position > 99:
                    position -= 100
            else:
                position += distance
        if position == 0:
            zero_counter += 1

    return zero_counter, position


zero_counter, position = find_password(my_input, 50)


print(f'Final position: {position}')
print(f'Number of zero positions: {zero_counter}')
