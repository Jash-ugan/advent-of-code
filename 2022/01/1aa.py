with open("input") as f:
    input = f.read()

max_cal = 0
for elf in input.split('\n\n'):
    max_cal = max(sum([ int(x) for x in elf.split('\n') ]), max_cal)

print(max_cal)