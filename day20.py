from math import gcd


def parse_input():
    modules = {}
    conjunction_memory = {}

    with open("input.txt") as file:
        for line in file:
            src, dst = line.strip().split(' -> ')
            if src.startswith('&'):
                src, dst = src[1:], dst.split(', ')
                modules[src] = {'type': 'c', 'dst': dst}
                conjunction_memory[src] = {}
            elif src.startswith('%'):
                src, dst = src[1:], dst.split(', ')
                modules[src] = {'type': 'f', 'state': 0, 'dst': dst}
            else:
                modules[src] = {
                    'type': 'b',
                    'dst': dst.split(', ')
                }
    for k, v in modules.items():
        for d in v['dst']:
            if d in conjunction_memory.keys():
                conjunction_memory[d].update({k: 0})
    return modules, conjunction_memory


modules, memory = parse_input()
part2_cycles = set()


def send_signal(frm, to, input_signal, cycle):
    if modules[to]['type'] == 'f':
        if not input_signal:
            modules[to]['state'] = int(not modules[to]['state'])
            return modules[to]['state']
        else:
            return -1

    elif modules[to]['type'] == 'c':
        if to == 'df' and any(memory[to].values()):
            part2_cycles.add(cycle + 1)

        if len(memory[to]) == 1:
            return int(not input_signal)
        else:
            memory[to][frm] = input_signal
            return int(0 in memory[to].values())


def process_signal(cycle):
    high, low = 0, 1
    processing_queue = [('broadcaster', 0)]

    while processing_queue:
        nxt = processing_queue.pop(0)
        src, signal = nxt[0], nxt[1]
        for dst in modules[src]['dst']:
            if signal == -1:
                continue
            else:
                if signal == 0:
                    low = low + 1
                else:
                    high = high + 1
                if dst in modules:
                    processing_queue.append((dst, send_signal(src, dst, signal, cycle)))
    return high, low


def press_button(cycles):
    high, low = 0, 0
    for i in range(0, cycles):
        h, l = process_signal(i)
        high += h
        low += l
    return high * low


"""
Part 1: 
print(press_button(1000))
"""


def lcm(paths):
    lcm = 1
    for i in paths:
        lcm = lcm * i // gcd(lcm, i)
    return lcm


def cycles_to_rx():
    press_button(5000)  # figured out manually
    return lcm(part2_cycles)


""" 
Part 2 
modules, memory = parse_input() #reset
print(cycles_to_rx())
"""
