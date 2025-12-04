# with open("example_input.txt") as f:
with open("real_input.txt") as f:
    my_input = [line.strip('\n') for line in f.readlines()]


def find_combo_lenght(my_input: list[str], target_length=2):
    total_joltage = 0

    for counter, str_number in enumerate(my_input):
        if len(str_number) < target_length:
            continue

        can_remove = len(str_number) - target_length
        list_of_digits = [int(d) for d in str(str_number)]
        current_joltage = []

        for d in list_of_digits:
            while current_joltage and can_remove > 0 and d > current_joltage[-1]:
                current_joltage.pop()
                can_remove -= 1
            current_joltage.append(d)

        joltage = int(''.join([str(d) for d in current_joltage[: target_length]]))
        total_joltage += joltage

    return total_joltage


print(f"Sum of the joltages is: {find_combo_lenght(my_input, 12)}")
