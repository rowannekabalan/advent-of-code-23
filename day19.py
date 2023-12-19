import re


def parse_input():
    all_rules = {}
    all_parts = {}

    with open("input.txt", "r") as file:
        rules, parts = map(str.split, file.read().split("\n\n"))

        for rule in rules:
            key, conditions = rule.split('{')
            conditions = conditions[:-1].split(',')
            all_rules[key] = [(c.split(':')[0], c.split(':')[1]) if ':' in c else ('True', c) for c in conditions]

        for i, part in enumerate(parts):
            matches = dict(re.findall(r'([a-z])=(\d+)', part))
            all_parts[i] = {key: int(value) for key, value in matches.items()}

    return all_rules, all_parts


def parse_rule(string):
    match = re.match(r'([a-z]+)([<>]+)(\d+)', string)

    variable, operator, value = match.groups()
    return variable, operator, int(value)


all_rules, all_parts = parse_input()


# /******* Part 1 ******/

def process_part(part, rule):
    for step in rule:
        if not step[0] == "True":
            char, op, val = parse_rule(step[0])
            if eval(f' {part[char]} {op} {val}'):
                if step[1] in ['R', 'A']:
                    return step[1]
                return process_part(part, all_rules[step[1]])
        else:
            if step[1] in ['R', 'A']:
                return step[1]
            return process_part(part, all_rules[step[1]])


def calculate_accepted(parts):
    total = 0
    for part in parts:
        res = process_part(parts[part], all_rules['in'])
        if res == "A":
            total += parts[part]['x'] + parts[part]['m'] + parts[part]['a'] + parts[part]['s']
    return total


# /******* Part 2 *******/


accepted_combos = []


def split_part_ranges(parts, condition):
    char, op, val = parse_rule(condition)
    matched, unmatched = parts.copy(), parts.copy()
    start, end = parts[char]

    if op == '>' and val < end:
        matched[char] = (val + 1, end)
        unmatched[char] = (start, val)
    elif op == '<' and val > start:
        matched[char] = (start, val - 1)
        unmatched[char] = (val, end)

    return matched, unmatched


def process_rule(rule, parts):
    for step in all_rules[rule]:
        if step[0] == "True":
            if step[1] == 'A':
                accepted_combos.append(parts)
            elif step[1] != 'R':
                accepted_combos.append(process_rule(step[1], parts))
        else:
            matched, unmatched = split_part_ranges(parts, step[0])
            if step[1] not in ['R', 'A']:
                accepted_combos.append(process_rule(step[1], matched))
            elif step[1] == 'A':
                accepted_combos.append(matched)
            parts = unmatched
    return


def sum_accepted_combinations():
    total = 0
    process_rule('in', {'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)})
    for combo in accepted_combos:
        if combo:
            x_range = combo['x'][1] - combo['x'][0] + 1
            m_range = combo['m'][1] - combo['m'][0] + 1
            a_range = combo['a'][1] - combo['a'][0] + 1
            s_range = combo['s'][1] - combo['s'][0] + 1
            total += x_range * m_range * a_range * s_range
    return total
