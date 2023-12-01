import re;

def calculate() -> int:
    with open("input.txt") as file:
        lines = [line.rstrip() for line in file]
        sum = 0
        for line in lines:
            allDigits = []
            for i, c in enumerate(line):
                if c.isdigit():
                    allDigits.append(c)
            print(allDigits)
            code = allDigits[0] + allDigits[-1]
            sum = sum + int(code)

    return sum

def calculate2() -> int:
    digits = {
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine"
    }
    with open("input.txt") as file:
        lines = [line.rstrip() for line in file]
        sum = 0
        for line in lines:
            allDigits = dict()
            for num, let in digits.items():
                indices = [m.start() for m in re.finditer(let, line)]
                for index in indices:
                    if index != -1:
                            allDigits[index] = num

            for index, char in enumerate(line):
                if char.isdigit():
                    allDigits[index] = char
            code = allDigits[min(allDigits)] + allDigits[max(allDigits)]
            print(code)
            sum = sum + int(code)
            print(sum)
    return sum

