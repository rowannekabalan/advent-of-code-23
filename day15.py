steps = []
lenses = dict()


def parse_input():
    with open('input.txt') as file:
        steps = file.readline().split(',')
        return steps

# /******** Part 1 ******/

def hash(string):
    current_value = 0
    for char in string:
        current_value += ord(char)
        current_value = current_value * 17
        current_value = current_value % 256
    return current_value

def sum_all():
    return sum([hash(step) for step in steps])

# /******** Part 2 ******/

def process_step(step):
    if '=' in step:
        seq = step.split('=')[0]
        num = step.split('=')[1]
        h = hash(seq)
        if h not in lenses:
            lenses[h] = [(seq, num)]
        else:
            found = 0
            for i, val in enumerate(lenses[h]):
                if val[0] == seq:
                    lenses[h].remove(val)
                    lenses[h].insert(i, (seq, num))
                    found = 1
                    break
            if not found:
                lenses[h].append((seq, num))

    else:
        seq = step.split('-')[0]
        h = hash(seq)
        if h in lenses:
            for i, val in enumerate(lenses[h]):
                if val[0] == seq:
                    lenses[h].remove(val)
                    break

def calculate_focus_power():
    sum = 0
    for box in lenses:
        if len(lenses[box]) > 0:
            for i, lens in enumerate(lenses[box]):
                print(lens)
                sum += (1+ box) * (i+1) * int(lens[1])
    return sum
