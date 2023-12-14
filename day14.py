import re
import cache

rocks = []

def parse_input():
    with open("input.txt") as file:
        lines = [line.rstrip() for line in file]
        for line in lines:
            rocks.append(line)
    return list(map(''.join, zip(*rocks[::-1])))

rocks = parse_input()


def calculate_load(rocks):
    total_load = 0
    rolled = roll_all(rocks)

    for line in rolled:
        total_load += sum(i + 1 for i, rock in enumerate(line) if rock == "O")
    return total_load

def roll_all(rocks):
    rolled = []
    for line in rocks:
        rolled.append(split_and_roll(line))
    return rolled

@cache
def split_and_roll(line):
    rolled = []
    for part in re.split('(#)', line):
        rolled.extend(roll_rocks(part)) if part.count('O') else rolled.extend(part)
    return ''.join(rolled)


def roll_rocks(line):
    line = list(line)

    def all_rolled():
        round_rocks = line.count('O')
        end_rocks = set((line[-round_rocks:]))
        return len(end_rocks) == 1 and 'O' in end_rocks

    for i in range(len(line)):
        if line[i] == 'O' and not all_rolled():
            line = insert_rolled_rock(i, line)

    return line


def insert_rolled_rock(rock_i, line):
    for i in reversed(range(len(line))):
        if line[i] != 'O':
            line[i], line[rock_i] = 'O', '.'
            break
    return line


def rotate_left(rocks):
    transposed = list(map(list, zip(*rocks)))
    reversed = [row[::-1] for row in transposed]
    return list(map(''.join, reversed))


def cycle(times):
    i = 0
    north = roll_all(rocks)
    while i < times:
        west = roll_all(rotate_left(north))
        south = roll_all(rotate_left(west))
        east = roll_all(rotate_left(south))
        north = roll_all(rotate_left(east))
        i += 1
    return east









