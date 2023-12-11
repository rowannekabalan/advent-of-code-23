import itertools
import time

universe = []
galaxies = dict()


# /********* Part 1 *******/

def build_universe_and_expand_rows():
    with open("input.txt") as file:
        for line in file:
            line = line.strip()
            universe.append(list(line))
            if check_universe_line(line):
                universe.append(list(line))

    return universe


def expand_universe_columns():
    size = len(universe[0])
    i = 0
    while i < size:
        column_values = [row[i] for row in universe]
        if check_universe_line(column_values):
            for row in universe:
                row.insert(i, '.')
            size += 1
            i += 2
        else:
            i += 1
    return universe


def check_universe_line(line):
    return line.count('.') == len(line)


def fill_galaxies():
    galaxy_counter = 1
    for row, val in enumerate(universe):
        for col, v in enumerate(val):
            if universe[row][col] == "#":
                galaxies[galaxy_counter] = (row, col)
                galaxy_counter += 1
    return galaxies


def manhattan_distance(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])


def sum_distances():
    sum_distance = 0
    for (i, x_i), (j, y_j) in itertools.combinations(galaxies.items(), 2):
        d = manhattan_distance(x_i, y_j)
        sum_distance += d
    return sum_distance


# /********** Part 2 ****** /

old_galaxies = dict()


def get_unexpanded_galaxies():
    global old_galaxies
    with open("input.txt") as file:
        for row, line in enumerate(map(str.strip, file)):
            for col, char in enumerate(line):
                if char == "#":
                    old_galaxies[len(old_galaxies) + 1] = (row, col)
    return old_galaxies


def shift_galaxy_coordinates(shift_by):
    global galaxies
    for g in old_galaxies:
        x_shift = galaxies[g][0] - old_galaxies[g][0]
        y_shift = galaxies[g][1] - old_galaxies[g][1]
        new_x = old_galaxies[g][0] + (x_shift * shift_by)
        new_y = old_galaxies[g][1] + (y_shift * shift_by)
        galaxies[g] = (new_x, new_y)


def sum_distances_with_shift():
    get_unexpanded_galaxies()
    shift_galaxy_coordinates(999999)
    return sum_distances()

