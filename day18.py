def parse_input():
    with open("input.txt") as file:
        return [(line.split()[0], int(line.split()[1])) for line in file]


# /******** Part1 *******

def dig(plan):
    start_x, start_y = 0, 0
    trenches = []
    directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

    for direction, steps in plan:
        for i in range(steps + 1):
            new_x = start_x + directions[direction][0] * i
            new_y = start_y + directions[direction][1] * i

            trenches.append((new_x, new_y))
        start_x, start_y = new_x, new_y

    return trenches


def polygon_area(vertices):  # shoelace formula
    n = len(vertices)
    area = 0.5 * abs(
        sum(vertices[i][0] * vertices[(i + 1) % n][1] - vertices[(i + 1) % n][0] * vertices[i][1] for i in range(n)))
    return area


def interior_points(area, boundary_count):  # pick's theorem
    return area - boundary_count / 2 + 1


def count_trenches(boundaries, plan):  # combines above formulas to count interior points in the polygon
    boundary_count = sum([line[1] for line in plan])
    area = polygon_area(boundaries)
    return int(interior_points(area, boundary_count) + boundary_count)


def calculate_part_1():
    plan = parse_input()
    trenches = dig(plan)
    return count_trenches(trenches, plan)


# /******** Part2 *******

def parse_part_2():
    directions = {0: 'R', 1: 'D', 2: 'L', 3: 'U'}

    with open("input.txt") as file:
        plan = [(directions[int(line.split()[2][-2])], int(line.split()[2][2:-2], 16)) for line in file]

    return plan

def calculate_part_2():
    plan = parse_part_2()
    trenches = dig(plan)
    return count_trenches(trenches, plan)


