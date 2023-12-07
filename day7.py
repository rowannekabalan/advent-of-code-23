from collections import Counter

input_dict = {}
hands_by_type = {i: [] for i in range(7)}
wildcards = False


def parse_input():
    with open("input.txt") as file:
        for line in file:
            hand, value = line.split()
            input_dict[hand] = int(value)


def card_strength(card):
    high_cards = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
    if wildcards:
        high_cards['J'] = 1
    if card in high_cards:
        return high_cards[card]
    else:
        return int(card)


def custom_sort_key(hand):
    return tuple(card_strength(card) for card in hand)


def hand_type(hand):
    counts = Counter(hand).values()
    jokers = Counter(hand)['J']
    h_type = 0

    if wildcards and jokers != 0:
        jokers = Counter(hand)['J']
        non_jokers = Counter(c for c in hand if c != 'J').values()

        if jokers == 5 or (5 - jokers) in non_jokers:
            h_type = 6
        elif 4 - jokers in non_jokers:
            h_type = 5
        elif jokers == 2:
            h_type = 3
        elif jokers == 1:
            if 1 not in non_jokers:
                h_type = 4
            elif 2 in non_jokers:
                h_type = 3
            else:
                h_type = 1
    else:
        if 5 in counts:
            h_type = 6
        elif 4 in counts:
            h_type = 5
        elif 3 in counts:
            if 2 in counts:
                h_type = 4
            else:
                h_type = 3
        elif 2 in counts:
            if len(counts) == 3:
                h_type = 2
            else:
                h_type = 1

    hands_by_type[h_type].append(hand)
    return h_type


def total_winnings(with_wildcards):
    global wildcards
    winnings = 0
    total_ranked = []
    wildcards = with_wildcards

    sorted(input_dict.keys(), key=hand_type)

    for k, v in hands_by_type.items():
        hands_by_type[k] = sorted(v, key=custom_sort_key)

    for item in hands_by_type.values():
        total_ranked.extend(item)

    for i, val in enumerate(total_ranked):
        winnings += ((i + 1) * input_dict[val])

    return winnings
