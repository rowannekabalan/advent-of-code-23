from math import gcd

tree = dict()
directions = 'LLR'  # copy over from input


def build_tree():
    global tree
    with open("test.txt") as file:
        for line in file:
            split1 = line.split("=")
            val = split1[0].strip()
            split2 = split1[1].split(",")
            l = ''.join(filter(str.isalnum, split2[0]))
            r = ''.join(filter(str.isalnum, split2[1]))
            tree[val] = {}
            tree[val]['l'] = l
            tree[val]['r'] = r


def build_tree():
    global tree
    with open("test.txt") as file:
        for line in file:
            split1 = line.split("=")
            val = split1[0].strip()
            split2 = split1[1].split(",")
            l = ''.join(filter(str.isalnum, split2[0]))
            r = ''.join(filter(str.isalnum, split2[1]))
            tree[val] = {}
            tree[val]['l'] = l
            tree[val]['r'] = r


def direction(step_no):
    if step_no <= len(directions):
        return directions[step_no - 1]
    return directions[(step_no % len(directions)) - 1]


def next_step(node, d):
    if d == 'L':
        return tree[node]['l']
    return tree[node]['r']


def find_steps_part1(current_node='AAA'):
    step = 0
    while current_node != 'ZZZ':
        step += 1
        current_node = next_step(current_node, direction(step))
    return step


def find_steps_part2(node, d):
    step = 0

    while not node.endswith('Z'):
        step += 1
        node = next_step(node, direction(step))
    return step


def lcm(paths):
    lcm = 1
    for i in paths:
        lcm = lcm * i // gcd(lcm, i)
    return lcm


def find_all_steps():
    current_nodes = [node for node in tree if node.endswith('A')]
    node_path_lengths = []
    for node in current_nodes:
        node_path_lengths.append(find_steps_part2(node, directions[0]))
    return lcm(node_path_lengths)
