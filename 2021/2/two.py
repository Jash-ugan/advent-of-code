# Read and sanitize input
f = open("input.txt","r")
raw_input = f.readlines()
input = []
for index, value in enumerate(raw_input):
    input.append(value.replace("\n",""))

# Work through the course

depth       = 0
position    = 0
aim         = 0

for i in input:
    cmds = i.split(" ")
    if cmds[0] == "up":
        aim -= int(cmds[1])
    elif cmds[0] == "down":
        aim += int(cmds[1])
    elif cmds[0] == "forward":
        position += int(cmds[1])
        depth += aim*int(cmds[1])

print(depth*position)