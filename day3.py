import re;

# ******* Part 1 ********/


num_indices = dict()
matrix = []
size = 0


def sum_parts():
    global size
    row, sum = 0, 0

    with (open("input3.txt") as file):
        lines = [line.rstrip() for line in file]
        size = len(lines)
        for line in lines:
            matrix.append(list(line))
            indices = [(m.start(), m.end()) for m in re.finditer(r'\d+', line)]
            if len(indices) != 0:
                num_indices[row] = indices
            row += 1

    for row in num_indices:
        for start, end in num_indices[row]:
            if check_neighbours(row, start, end, matrix):
                part = ''.join(matrix[row][start:end])
                sum += int(part)
    return sum


def check_neighbours(row, col, end_col, matrix):
    valid_neighbours = False
    single_digit = (
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    )
    double_digit = single_digit + ((-1, 2), (0, 2), (1, 2))

    triple_digit = double_digit + ((-1, 3), (0, 3), (1, 3))

    if (end_col - col) == 3:
        neighbours = triple_digit
    elif (end_col - col) == 2:
        neighbours = double_digit
    else:
        neighbours = triple_digit

    for x, y in neighbours:
        if row + x in range(size) and col + y in range(size):
            if re.match(r'[^a-zA-Z0-9.]', matrix[row + x][col + y]):
                valid_neighbours = True

    return valid_neighbours


# ******* Part 2 ********/
def find_gear_ratios():
    potential_gears = []
    count, sum = 0, 0
    
    for row in matrix:
        indices = ([i for i, x in enumerate(row) if x == "*"])
        if len(indices) != 0:
            for index in indices:
                potential_gears.append((count, index))
        count += 1
    for x, y in potential_gears:
        gear_neighbours = find_gear_neighbours(x, y, matrix)
        if gear_neighbours:
            sum = sum + gear_parts_ratio(gear_neighbours)
    return sum


def find_gear_neighbours(row, col, matrix):
    neighbour_nums = []
    neighbours = (
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    )

    for x, y in neighbours:
        if row + x in range(size) and col + y in range(size):
            num = re.match(r'\d', matrix[row + x][col + y])
            if num:
                neighbour_nums.append((row + x, col + y))

    if len(neighbour_nums) >= 2:
        return neighbour_nums
    else:
        return False


def gear_parts_ratio(gear_neighbours):
    parts = set()
    ratio = 0

    for row, col in gear_neighbours:
        for start, end in num_indices[row]:
            if start <= col <= end:
                part = ''.join(matrix[row][start:end])
                parts.add(part)
    p = list(parts)
    if len(parts) > 1:
        ratio = int(p[0]) * int(p[1])
    return ratio
