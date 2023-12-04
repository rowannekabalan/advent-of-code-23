cards = dict()


def populate_dict():
    with open("input4.txt") as file:
        lines = [line.rstrip() for line in file]
        for line in lines:
            game_id = int(line.split()[1].split(":")[0])
            numbers = ((line.split(": ")[1]).split("| "))
            winning = numbers[0].split()
            my_nums = numbers[1].split()
            cards[game_id] = {
                "winning": winning,
                "nums": my_nums
            }


# ****** Part 1 ******

def game_score(game_id, card_pile):
    score = 0
    for num in card_pile[game_id]['nums']:
        if num in card_pile[game_id]['winning']:
            if score == 0:
                score = 1
            else:
                score = score * 2
    return score


def total_score(card_pile):
    total_points = 0
    for game_id in card_pile:
        total_points = total_points + game_score(game_id, card_pile)
    return total_points


# ****** Part 2 ******

def count_matches(winning, nums):
    count = 0
    for num in nums:
        if num in winning:
            count += 1
    return count


def final_stockpile():
    new_cards = dict()
    for game_id in cards.keys():
        new_cards[game_id] = 1
    process_cards(1, new_cards)
    return new_cards


def process_cards(game_id, new_cards):
    if game_id not in new_cards:
        return
    matches = count_matches(cards[game_id]["winning"], cards[game_id]["nums"])
    next_game = game_id + 1
    for j in range(new_cards[game_id]):
        for i in range(next_game, next_game + matches):
            if i in new_cards:
                new_cards[i] += 1
    return process_cards(next_game, new_cards)


def count_final_stockpile():
    count = 0
    stockpile = final_stockpile()
    for id in stockpile:
        count += stockpile[id]
    return count

