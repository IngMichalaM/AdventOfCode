MAPPERS = ['seed-to-soil map', 'soil-to-fertilizer map', 'fertilizer-to-water map',
           'water-to-light map', 'light-to-temperature map', 'temperature-to-humidity map',
           'humidity-to-location map']

with open("input_test.txt") as infile:
    data = infile.read()

data = data.split("\n\n")

mappers_dict = dict()
def parse_input_data(data):
    for section in data:
        if section.startswith('seeds'):
            seeds = list(map(int, section.split(": ")[1].split()))
            print(f'{seeds=}')
        else:
            for curr_mapper in MAPPERS:
                if section.startswith(curr_mapper):
                    mapper_ranges = []
                    for line in section.split(":\n")[1].split("\n"):
                        mapper_ranges.append(list(map(int, line.split())))

                    mappers_dict[curr_mapper] = mapper_ranges

    return mappers_dict, seeds

mappers_dict, seeds = parse_input_data(data)

final_seeds_locations = []
for what_we_are_looking_for in seeds:
    for mapper in MAPPERS:
        for mapper_line in mappers_dict[mapper]:
            if what_we_are_looking_for in range(mapper_line[1], mapper_line[1]+mapper_line[2]+1):
                what_we_are_looking_for = mapper_line[0] + (what_we_are_looking_for - mapper_line[1])
                break

    final_seeds_locations.append(what_we_are_looking_for)

# print(f'{final_seeds_locations=}')
print(f'Minimum from the locations is {min(final_seeds_locations)}')
