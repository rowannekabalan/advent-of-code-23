import sys

energised = set()
neighbours = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}
max_energised = 0


def parse_input():
    with open("input.txt") as file:
        return [list(line.rstrip()) for line in file]


contraption = parse_input()
rows = len(contraption)
cols = len(contraption[0])


# /******* Part 1 *******

def next_move(current, direction):
    if current == "." or (current == "|" and direction in ['N', 'S']) or (current == "-" and direction in ['W', 'E']):
        return direction

    if current == '|':
        return ['N', 'S']
    if current == '-':
        return ['W', 'E']
    if current == '/':
        if direction == 'E':
            return 'N'
        if direction == 'W':
            return 'S'
        if direction == 'S':
            return 'W'
        if direction == 'N':
            return 'E'
    else:
        if direction == 'E':
            return 'S'
        if direction == 'W':
            return 'N'
        if direction == 'S':
            return 'E'
        if direction == 'N':
            return 'W'


def dead_end(x, y, direction):
    return (x == 0 and direction == 'N') or (x == rows - 1 and direction == 'S') or (
            y == 0 and direction == 'W') or (y == cols - 1 and direction == 'E')


def navigate(beam_x=0, beam_y=0, direction='E', visited=None):
    global energised, neighbours

    if visited is None:
        visited = {}

    if not (0 <= beam_x < rows) or not (0 <= beam_y < cols) or (beam_x, beam_y, direction) in visited:
        return 0

    energised.add((beam_x, beam_y))

    visited[(beam_x, beam_y, direction)] = True

    d = next_move(contraption[beam_x][beam_y], direction)

    if dead_end(beam_x, beam_y, d):
        return 0

    new_x = beam_x + neighbours[d[0]][0]
    new_y = beam_y + neighbours[d[0]][1]

    if len(d) == 1:
        return 1 + navigate(new_x, new_y, d[0], visited)
    else:
        new_x2 = beam_x + neighbours[d[1]][0]
        new_y2 = beam_y + neighbours[d[1]][1]
        return 1 + navigate(new_x, new_y, d[0], visited) + navigate(new_x2, new_y2, d[1], visited)


def tiles_energised(x=0, y=0, d='E'):
    global energised
    navigate(x, y, d)
    result = len(energised)
    energised = set()
    return result


# /******* Part 2 *******

def find_max_energised():
    global max_energised, energised

    for i in range(rows):
        for j in range(cols):
            if i == 0:
                max_energised = max(max_energised, tiles_energised(i, j, 'S'))
            elif i == rows - 1:
                max_energised = max(max_energised, tiles_energised(i, j, 'N'))
            if j == 0:
                max_energised = max(max_energised, tiles_energised(i, j, 'E'))
            elif j == cols - 1:
                max_energised = max(max_energised, tiles_energised(i, j, 'W'))

    return max_energised


sys.setrecursionlimit(10 ** 6)
