import sys, time

def parse_input():
    trails = []
    with open("input.txt") as file:
        for line in file:
            trails.append(list(line.strip()))
    return trails


trails = parse_input()
rows, cols = len(trails), len(trails[0])
visited = set()
longest_path = 0


def valid_moves(x, y, visited):
    moves = []
    neighbours = {'<': (0, -1), '>': (0, 1), 'v': (1, 0), '^': (-1, 0)}

    for dx, dy in neighbours.values():
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < rows and 0 <= new_y < cols and not (new_x, new_y) in visited and trails[new_x][
            new_y] != "#":
            moves.append((new_x, new_y))
    return moves


def dfs(x, y, visited, current_length):
    global longest_path

    visited.add((x, y))

    if (x, y) == end_point:
        longest_path = max(longest_path, current_length)

    moves = valid_moves(x, y, visited)

    for new_x, new_y in moves:
        dfs(new_x, new_y, visited, current_length + 1)

    visited.remove((x, y))


start_point = (0, 1)
end_point = (140, 139)

sys.setrecursionlimit(10 ** 6)

dfs(start_point[0], start_point[1], visited, 0)

start = time.time()
print(longest_path)
print(time.time() - start)
