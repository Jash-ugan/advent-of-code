chose = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

outcome = {
    'A X': 3,
    'A Y': 6,
    'A Z': 0,
    'B X': 0,
    'B Y': 3,
    'B Z': 6,
    'C X': 6,
    'C Y': 0,
    'C Z': 3,
}


def read_input():
    with open('input') as f:
        input = f.read()

    return input.split('\n')

def calc_round(round: str) -> int:
    return outcome[round] + chose[round.split(' ')[1]]

def calc_strategy(strategy: list) -> int:
    points = 0
    for round in strategy:
        points += calc_round(round)
    return points




strategy = read_input()
print(calc_strategy(strategy))
