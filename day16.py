import sys

contraption = []
energised = set()
neighbours = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}
max_energised = 0


def parse_input():
    with open("input.txt") as file:
        lines = [line.rstrip() for line in file]
        for line in lines:
            contraption.append(list(line))
        return contraption


parse_input()
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

    if beam_x not in range(rows) or beam_y not in range(cols):
        return 0

    if visited is None:
        visited = {}

    energised.add((beam_x, beam_y))

    if (beam_x, beam_y, direction) in visited:
        return 0

    visited[(beam_x, beam_y, direction)] = True

    new_d = next_move(contraption[beam_x][beam_y], direction)

    if dead_end(beam_x, beam_y, new_d):
        return 0

    if len(new_d) == 1:
        beam_x += neighbours[new_d[0]][0]
        beam_y += neighbours[new_d[0]][1]
        return 1 + navigate(beam_x, beam_y, new_d[0], visited)
    else:
        return 1 + navigate(beam_x + neighbours[new_d[0]][0], beam_y + neighbours[new_d[0]][1], new_d[0], visited) + \
            navigate(beam_x + neighbours[new_d[1]][0], beam_y + neighbours[new_d[1]][1], new_d[1], visited)


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
