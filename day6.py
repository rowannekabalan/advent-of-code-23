import math


def distance_travelled(hold_time, race_time):
    return hold_time * (race_time - hold_time)


def min_to_win(race_time, record):
    min = 1
    for ms in range(1, math.floor(race_time / 2) + 1):
        if distance_travelled(ms, race_time) > record:
            min = ms
            break
    return min


def ways_to_win(race_time, record):
    min = min_to_win(race_time, record)
    return (race_time + 1) - (min * 2)
