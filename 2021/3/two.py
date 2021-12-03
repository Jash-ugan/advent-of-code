def read_and_sanitize_input(path):
    # Read and sanitize input
    f = open(path,"r")
    raw_input = f.readlines()
    input = []
    for index, value in enumerate(raw_input):
        input.append(value.replace("\n",""))
    return input

def get_most_common_bit_for_position(input, position):
    addition = 0
    threshold = len(input)/2
    for line in input:
        addition += int(line[position])
    if addition >= threshold:
        return "1"
    elif addition < threshold:
        return "0"

def get_most_uncommon_bit_for_position(input, postition):
    most_common = get_most_common_bit_for_position(input,postition)
    if most_common == "1": return "0"
    elif most_common == "0": return "1"

def oxygen(input, position):
    if len(input) <= 0: raise Exception("No values left.")
    if len(input) == 1: return input[0]

    most_common = get_most_common_bit_for_position(input, position)
    reduced_set = []
    for line in input:
        if line[position] == most_common:
            reduced_set.append(line)
    return oxygen(reduced_set, position+1)

def co2_scrubber_rating(input, position):
    if len(input) <= 0: raise Exception("No values left.")
    if len(input) <= 1: return input[0]

    most_uncommon = get_most_uncommon_bit_for_position(input, position)
    reduced_set = []
    for line in input:
        if line[position] == most_uncommon:
            reduced_set.append(line)
    return co2_scrubber_rating(reduced_set, position+1)

input   = read_and_sanitize_input("3/input.txt")
ox      = oxygen(input, 0)
co2     = co2_scrubber_rating(input, 0)
print("Oxygen: " + ox)
print("Co2 scrubber: " + co2)

life_support = int("0b"+ox,2) * int("0b"+co2,2)
print("Life support rating: " + str(life_support))
