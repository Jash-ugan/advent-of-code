# Read and sanitize input
f = open("3/input.txt","r")
raw_input = f.readlines()
input = []
for index, value in enumerate(raw_input):
    input.append(value.replace("\n",""))

# Prepare result list
result = []
for i in range(0,12):result.append(0)

# Add all bits per row
for line in input:
    for index, bit in enumerate(line):
        result[index] += int(bit)

gamma_rate = ""
epsilon_rate = ""

for i in result:
    if i > 500:
        gamma_rate += "1"
        epsilon_rate += "0"
    elif i < 500:
        gamma_rate += "0"
        epsilon_rate += "1"
    else:
        print("ERROR")

print("Gamma rate bin: " + gamma_rate)
print("Epsilon rate bin: " + epsilon_rate)

gamma_rate      = int("0b"+gamma_rate,2)
epsilon_rate    = int("0b"+epsilon_rate,2)

print("")
print("Gamma rate dec: " + str(gamma_rate))
print("Epsilon rate dec: " + str(epsilon_rate))

result = gamma_rate*epsilon_rate
print("")
print("Result " + str(result))