import re;
import time;

seeds = []
mappings = []
seed_ranges = []


def parse_input():
    global seeds
    with open("input5.txt") as file:
        input = file.read()
        seeds = input.split(":")[1].split("\n")[0].split()
        transformations = re.findall(r'map:\n([^a-zA-Z]*)(?:\n[a-zA-Z]|$)', input)
        for t in transformations:
            mappings.append(t.strip().split('\n'))
        for i in range(0, len(seeds), 2):
            seed, rng = int(seeds[i]), int(seeds[i + 1])
            seed_ranges.append((seed, seed + rng - 1))


def process_seed_range(seed_range):
    for mapping in mappings:
        seed_range = map_seed_range(seed_range, mapping)
    return seed_range


def process_seed(seed, rule):
    dst, src, rng = map(int, rule.split())
    seed = dst + (seed - src)
    return seed


def map_seed_range(range, mapping):
    unmapped = range
    mapped = set()
    for rule in mapping:
        for partial_range in unmapped.copy():
            result = range_map_and_partition(partial_range[0], partial_range[1], rule)
            if result[0]:
                mapped = mapped.union(result[0])
                unmapped.remove(partial_range)

            unmapped = unmapped.union(result[1])

    return mapped.union(unmapped)


def range_map_and_partition(start, end, rule):  
    rule_start = int(rule.split()[1])
    rule_end = rule_start + int(rule.split()[2]) - 1
    mapped = set()
    unmapped = set()

    if start >= rule_start and end <= rule_end:
        # in rule range
        mapped.add((process_seed(start, rule), process_seed(end, rule)))
    elif (start < rule_start and end < rule_start) or (start > rule_end and end > rule_end):
        # out of rule range
        unmapped.add((start, end))
    elif start < rule_start and end <= rule_end:
        # starts outside rule range and ends within
        mapped.add((process_seed(rule_start, rule), process_seed(end, rule)))
        unmapped.add((start, rule_start - 1))
    elif rule_start <= start <= rule_end:
        # starts inside rule range and ends outside
        mapped.add((process_seed(start, rule), process_seed(rule_end, rule)))
        unmapped.add((rule_end + 1, end))
    else:
        # starts before rule range and ends after
        mapped.add((process_seed(rule_start, rule), process_seed(rule_end, rule)))
        unmapped.add((start, rule_start - 1))
        unmapped.add((rule_end + 1, end))

    return {0: mapped, 1: unmapped}


def find_lowest_location():
    all_locations = []
    s = set()
    for seed_range in seed_ranges:
        s.add(seed_range)
        locations = process_seed_range(s)
        all_locations.extend(locations)
    return min(all_locations)[0]

