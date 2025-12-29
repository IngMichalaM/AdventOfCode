# https://adventofcode.com/2025/day/8
# Input  X,Y,Z coordinates of the boxes - connect all, always the closest boxes first
# Always connect two closest boxes first. Those connections can create a new circuit
# or elongate an already connected circuit.


with open("test_input.txt") as f:
    my_input = [line.strip('\n') for line in f.readlines()]

box_coordinates = []
for coor in my_input:
    box_coordinates.append(list(map(int, coor.split(','))))


def straight_line_square_distance(box_01: list[int, int, int], box_02: list[int, int, int]) -> float:
    """ No need for the square root when just comparing distances """
    return (box_02[0] - box_01[0]) ** 2 + (box_02[1] - box_01[1]) ** 2 + (box_02[2] - box_01[2]) ** 2


# Distances of the boxes. i, j are directly the indexes of the boxes, can be used later for references
all_box_distance = []
for i in range(len(box_coordinates)):
    for j in range(i + 1, len(box_coordinates)):
        dist = straight_line_square_distance(box_coordinates[i], box_coordinates[j])
        all_box_distance.append((dist, i, j))

sorted_boxes_by_dist = sorted(all_box_distance)  # shortes distance first

circuits = []
tag_skipp = False
counter = 0
for box in sorted_boxes_by_dist:
    if counter == 10:
        break
    current_dist, box_01_id, box_02_id = box
    # print(f'Processing boxes {box_01_id} ({box_coordinates[box_01_id]}) and'
    #       f' {box_02_id} ({box_coordinates[box_02_id]}) with distance {current_dist}...')
    if circuits:
        # if not empty, look through different circuits to find out if the current box is in it
        circuit_with_box_01 = None
        circuit_with_box_02 = None
        for inx, circuit in enumerate(circuits):
            if box_01_id in circuit and box_02_id in circuit:
                # print(f'Both boxes {box_01_id} and {box_02_id} are already in circuit {circuit}, skipping...')
                tag_skipp = True
                continue
            if box_01_id in circuit:
                # print(f'Box {box_01_id} found in circuit {circuit}')
                circuit_with_box_01 = circuit
            if box_02_id in circuit:
                # print(f'Box {box_02_id} found in circuit {circuit}')
                circuit_with_box_02 = circuit
        if tag_skipp:
            tag_skipp = False
            counter += 1
            continue
        if circuit_with_box_01 and circuit_with_box_02:
            # print(f'Both boxes are in different circuits, merge them')
            circuits.remove(circuit_with_box_01)
            circuits.remove(circuit_with_box_02)
            circuit_with_box_01.extend(circuit_with_box_02)
            circuits.append(circuit_with_box_01)
        elif circuit_with_box_01:
            # print('Only box 01 found in a circuit')
            circuits.remove(circuit_with_box_01)
            circuit_with_box_01.append(box_02_id)
            circuits.append(circuit_with_box_01)
        elif circuit_with_box_02:
            # print('Only box 02 found in a circuit')
            circuits.remove(circuit_with_box_02)
            circuit_with_box_02.append(box_01_id)
            circuits.append(circuit_with_box_02)
        else:
            # print('None of the two boxes is in any circuit, create a new one.')
            circuits.append([box_01_id, box_02_id])
    else:
        # print('Creating the first circuit...')
        circuits.append([box_01_id, box_02_id])
    counter += 1

print('Calculate length of the circuits')
length_of_circuits = []
for circuit in circuits:
    length_of_circuits.append(len(circuit))

sorted_lengths = sorted(length_of_circuits, reverse=True)
print(sorted_lengths)

res = sorted_lengths[0] * sorted_lengths[1] * sorted_lengths[2]  # multiply the lengths of the three longest circuits
print(f'Result is {res}')
