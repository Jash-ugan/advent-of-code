import json


with open("input") as f:
    input = f.read()

elfs = {}
input = input.split('\n\n')
num_elfs = len(input)
ctr = 0

while ctr < num_elfs:
    cals        = [ int(x) for x in input[ctr].split('\n') ]
    elfs[ctr]   = {'sumcals': sum(cals), 'inventory': cals}
    ctr += 1

max_elf = elfs[0]
for elf in elfs:
    if max_elf['sumcals'] < elfs[elf]['sumcals']:
        max_elf = elfs[elf]

print(max_elf)
