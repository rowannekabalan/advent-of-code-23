def find_between(s, start, end):
    return s.split(start)[1].split(end)[0]


def valid_draw(draw):
    colours = {"red": 12, "green": 13, "blue": 14}
    valid = True

    for item in draw:
        num = item.split(" ")[0]
        colour = item.split(" ")[1]
        if int(num) > colours[colour]:
            valid = False
    return valid

def sum_valid_games():
    sum_games = 0
    with open("input2.txt") as file:
        lines = [line.rstrip() for line in file]
        for line in lines:
            valid_game = True
            game_id = int(find_between(line, " ", ":"))
            game = ((line.split(": ")[1]).split("; "))
            print(game)
            for round in game:
                draw = round.split(", ")
                if not valid_draw(draw):
                    valid_game = False
            if valid_game:
                sum_games = sum_games + game_id
    return sum_games


def power_of_game(game):
    colours = {"red": 0, "green": 0, "blue": 0}
    for draw in game:
        items = draw.split(", ")
        for item in items:
            num = int(item.split(" ")[0])
            colour = item.split(" ")[1]
            if num > colours[colour]:
                colours[colour] = num
    return colours["red"] * colours["green"] * colours["blue"]


def sum_power_of_games():
    sum_power_games = 0
    with open("input2.txt") as file:
        lines = [line.rstrip() for line in file]
        for line in lines:
            game = ((line.split(": ")[1]).split("; "))
            sum_power_games = sum_power_games + power_of_game(game)
    return sum_power_games



