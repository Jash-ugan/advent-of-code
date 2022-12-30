desired_outcome = {
    'X': 0,
    'Y': 3,
    'Z': 6,
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

def chose_to_get(round):
    return str([x for x in outcome if "A" in x and outcome[x]==desired_outcome[round.split(' ')[1]]])


strategy = read_input()
print(chose_to_get(strategy[0]))
