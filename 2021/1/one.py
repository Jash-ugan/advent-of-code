
f = open("input.txt","r")
raw_input = f.readlines()
sonar = {}

for index, value in enumerate(raw_input):
    sonar[index+1] = {"depth": int(value.replace("\n","")), "trend": None}

for index in sonar:
    if index == 1:
        continue
    if sonar[index-1]["depth"] < sonar[index]["depth"]:
        sonar[index]["trend"] = 'increased'
    elif sonar[index-1]["depth"] > sonar[index]["depth"]:
        sonar[index]["trend"] = 'decreased'
    elif sonar[index-1]["depth"] == sonar[index]["depth"]:
        sonar[index]["trend"] = 'equal'

number_of_inc = 0
for i in sonar:
    if sonar[i]['trend'] == "increased":
        number_of_inc += 1

print(number_of_inc)
