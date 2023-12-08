Time = [7, 15, 30]
Distance = [9, 40, 200]

winning_race_counter_tot = 1

for t, dist in zip(Time, Distance):
    winning_race_counter = 0

    for tt in range(t+1):
        speed = tt  # *1 mm/s
        time_left = t-tt
        distance_traveled = time_left*speed
        if distance_traveled > dist:
            winning_race_counter += 1

    winning_race_counter_tot *= winning_race_counter

print(winning_race_counter_tot)