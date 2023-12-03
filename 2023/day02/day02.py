# day 2, part 1 - count colors, check max value for each color, map in dictionary

filename = 'input.txt'

with open(filename) as f:
    input = [line.strip('\n') for line in f.readlines()]

maxima_barev = {"red": 12, "green": 13, "blue": 14}

game_id_sum = 0
for line in input:
    game_ok = 1
    game, vsechny_tahy = line.split(":")
    _, game_id = game.split()

    for tah in vsechny_tahy.split(";"):
        if game_ok == 0:
            continue
        for jednotlive_barvy in tah.split(","):
            hodnota, barva = jednotlive_barvy.split()

            if int(hodnota) > maxima_barev[barva]:
                # print(f"this game numbeer {game_id} is not possible.")
                game_ok = 0
                break
    else:
        if game_ok == 1:
            # print(f"this game number {game_id} is ok.")
            game_id_sum += int(game_id)

print("ids sum ", game_id_sum)