# Part one only

import re;

seeds = []
mappings = []


def parse_input():
    global seeds
    with open("input5.txt") as file:
        input = file.read()
        seeds = input.split(":")[1].split("\n")[0].split()
        transformations = re.findall(r'map:\n([^a-zA-Z]*)(?:\n[a-zA-Z]|$)', input)
        for t in transformations:
            mappings.append(t.strip().split('\n'))


def transform():
    global seeds
    result = []
    for seed in seeds:
        new_seed = seed
        for mapping in mappings:
            new_seed = process_seed(int(new_seed), mapping)
        result.append(new_seed)
    return result


def process_seed(seed, mapping):
    for line in mapping:
        values = line.split()
        dst, src, rng = int(values[0]), int(values[1]), int(values[2])
        offset = rng - 1
        if src <= seed <= src + offset:
            seed = dst + (seed - src)
            break
    return seed


def lowest_location():
    return min(transform())


