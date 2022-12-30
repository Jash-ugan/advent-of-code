with open("input") as f:
    input = f.read()

cals = []
for elf in input.split('\n\n'):
    cals.append(sum([ int(x) for x in elf.split('\n') ]))


print(sum(sorted(cals, reverse=True)[:3]))