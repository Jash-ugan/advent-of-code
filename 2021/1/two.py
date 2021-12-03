f           = open("input.txt","r")
raw_input   = f.readlines()
sonar       = {}
windows     = {}

def get_window_sum(starting_index):
    return sonar[index]['depth']+sonar[index+1]['depth']+sonar[index+2]['depth']

for index, value in enumerate(raw_input):
    sonar[index] = {"depth": int(value.replace("\n","")), "trend": None}

for index in sonar:
    if index == len(sonar)-2:
        break
    windows[index] = {'sum': get_window_sum(index)}

count_increased = 0
for index in windows:
    if index == 0:
        continue
    if windows[index-1]['sum'] < windows[index]['sum']:
        windows[index]['trend'] = 'increased'
        count_increased += 1
    elif windows[index-1]['sum'] > windows[index]['sum']:
        windows[index]['trend'] = 'decreased'
    elif windows[index-1]['sum'] == windows[index]['sum']:
        windows[index]['trend'] = 'no change'

print(count_increased)