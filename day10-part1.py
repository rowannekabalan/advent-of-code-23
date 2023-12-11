from collections import defaultdict

maze = []
size = 0
start = ()


def parse_input():
    global size, start
    with open("input.txt") as file:
        lines = [line.rstrip() for line in file]
        size = len(lines) if len(lines) > len(lines[0]) else len(lines[0])
        row = 0
        for line in lines:
            if 'S' in line:
                start = (row, line.index('S'))
            else:
                row += 1
            maze.append(list(line))


valid_directions = {
    '|': ('N', 'S'),
    '-': ('W', 'E'),
    'L': ('N', 'E'),
    'J': ('N', 'W'),
    '7': ('S', 'W'),
    'F': ('S', 'E'),
    'S': ('S', 'W', 'N', 'E'),
    '.': ()
}


def valid_move(destination, direction):
    if destination == '.':
        return False
    else:
        if direction == 'S':
            return 'N' in valid_directions[destination]
        elif direction == 'N':
            return 'S' in valid_directions[destination]
        elif direction == 'E':
            return 'W' in valid_directions[destination]
        else:
            return 'E' in valid_directions[destination]


def find_valid_moves(node):
    valid = []
    row = node[0]
    col = node[1]
    neighbours = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}

    for d in valid_directions[maze[row][col]]:
        for x, y in [neighbours[d]]:
            if row + x in range(size):
                if col + y in range(size):
                    if valid_move(maze[row + x][col + y], d):
                        valid.append((row + x, col + y))

    return valid

# not used as it exceed max recursion depth allowed by python
def find_loop():
    def dfs(node, parent, path):
        nonlocal longest_loop, loop_found, visited
        visited.add(node)
        path.append(node)
        for neighbour in find_valid_moves(node):
            if neighbour not in visited:
                dfs(neighbour, node, path)
            elif neighbour != parent and not loop_found:
                loop_start = path.index(neighbour)
                current_loop = path[loop_start:]
                if len(current_loop) > len(longest_loop):
                    longest_loop = current_loop
                    loop_found = True

        path.pop()

    longest_loop = []
    loop_found = False
    visited = set()
    dfs(start, None, [])

    return longest_loop


def find_loop_iterative():
    stack = [(start, None, [])]
    longest_loop = []
    loop_found = False
    visited = set()

    while stack:
        node, parent, path = stack.pop()
        visited.add(node)
        path.append(node)

        for neighbour in find_valid_moves(node):
            if neighbour not in visited:
                stack.append((neighbour, node, path.copy()))
            elif neighbour != parent and not loop_found:
                loop_start = path.index(neighbour)
                current_loop = path[loop_start:]
                if len(current_loop) > len(longest_loop):
                    longest_loop = current_loop
                    loop_found = True

        path.pop()

    return longest_loop


def get_steps():
    return len(find_loop_iterative()) / 2
