# day 2, part 2 - count colors, define max value for each color, so that the game is valid, map in dictionary

# filename = 'input.txt'
filename = 'input_test.txt'

with open(filename) as f:
    input = [line.strip('\n') for line in f.readlines()]

the_power = 0
game_id_sum = 0
for line in input:

    maxima_barev = {"red": 0, "green": 0, "blue": 0}
    game, vsechny_tahy = line.split(":")
    _, game_id = game.split()

    for tah in vsechny_tahy.split(";"):

        for jednotlive_barvy in tah.split(","):
            hodnota, barva = jednotlive_barvy.split()
            hodnota = int(hodnota)

            if int(hodnota) > maxima_barev[barva]:
                maxima_barev[barva] = hodnota

    the_power += maxima_barev["red"]*maxima_barev["blue"]*maxima_barev["green"]

print(the_power)