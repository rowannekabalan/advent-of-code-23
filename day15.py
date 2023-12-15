from functools import cache
import time

all_records = []

def parse_input():
    with open("input.txt") as file:
        lines = [line.rstrip() for line in file]
        for line in lines:
            all_records.append([
                tuple(line.split()[0]), tuple([int(g) for g in line.split()[1].split(',')])
            ])


@cache
def find_combos(records, groups, current_group=0):
    if not records:
        # Finished groups or matched last remaining group
        if (not groups and current_group == 0) or (len(groups) == 1 and current_group == groups[0]):
            # Valid combination found
            return 1
        return 0

    combos = 0

    # '?' would get expanded twice, once treated as '#' and another as a '.'
    if records[0] in ['#', '?']:
        # Potential group match, expand current group
        combos += find_combos(records[1:], groups, current_group + 1)

    if records[0] in ['.', '?']:
        # Either closing a group or a useless '.' that can be dropped
        if groups and groups[0] == current_group:
            # Group closed, continue with one less group
            combos += find_combos(records[1:], groups[1:])
        elif current_group == 0:
            # Useless '.', continue
            combos += find_combos(records[1:], groups)
    return combos


def sum_combinations(records):
    return sum([find_combos(records[i][0], records[i][1]) for i, rec in enumerate(records)])

# /********* Part 2 *********/

def build_expanded_records():
    global all_records
    expanded_records = []
    for rec in all_records:
        extend_record = list(rec[0]) + ['?'] + list(rec[0]) + ['?'] + list(rec[0]) + ['?'] + list(rec[0]) + ['?'] + list(rec[0])
        extend_group = list(rec[1]) * 5
        expanded_records.append([tuple(extend_record), tuple(extend_group)])
    return expanded_records


parse_input()
print(sum_combinations(all_records))
start = time.time()
expanded = build_expanded_records()
print(sum_combinations(expanded))
print(f'Elapsed: {time.time() - start}')
