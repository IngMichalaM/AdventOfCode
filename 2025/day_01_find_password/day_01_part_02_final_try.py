# with open("input_example.txt") as f:
with open("real_input.txt") as f:
    my_input = [line.strip('\n') for line in f.readlines()]


def find_password(my_input: list[str], position: int = 50) -> tuple[int, int]:
    zeros_counter = 0

    for dial in my_input:
        direction = dial[0]
        distance = int(dial[1:])

        if direction == 'R':
            zeros_counter += (position + distance)//100
            position = (position + distance) % 100
        else:
            if position == 0:
                zeros_counter -= 1
            zeros_counter += (distance - position + 99) // 100
            position = (position - distance) % 100
            if position == 0:
                zeros_counter += 1

    return zeros_counter, position


print(find_password(my_input))
