input = []


def parse_input():
    with open("test.txt") as file:
        for line in file:
            input.append(list(map(int, line.split())))

# /****** Part 1 *******/
def find_next(seq):
    hold = [seq[-1]]

    while not all(v == 0 for v in seq.copy()):
        diffs = []
        for n in range(len(seq) - 1):
            diffs.append(seq[n + 1] - seq[n])
        hold.append(diffs[-1])
        seq = diffs
    return sum(hold)


def find_sum():
    sum = 0
    for seq in input:
        sum += find_next(seq)
    return sum


# /****** Part 2 *******/
def find_previous(seq):
    hold = [seq[0]]
    prev = 0

    while not all(v == 0 for v in seq.copy()):
        diffs = []
        for n in range(len(seq) - 1):
            diffs.append(seq[n + 1] - seq[n])
        hold.append(diffs[0])
        seq = diffs
    for i, n in enumerate(hold):
        if i % 2 == 0:
            prev = prev + n
        else:
            prev = prev - n
    return prev


def find_previous_sum():
    sum = 0
    for seq in input:
        sum += find_previous(seq)
    return sum
