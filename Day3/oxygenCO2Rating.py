input_file = open('input.txt', 'r')
all_lines = input_file.readlines()
found_oxygen = ''
found_co2 = ''### Oxygen Part
dict = {
    'first': 0
}
new_lines = all_lines
helper = []
for index in range(0, 12):
    for line in new_lines:
        if line[index] == '1':
            dict['first'] = dict['first'] + 1
   
    if dict['first'] >= (len(new_lines) / 2):
        for line in new_lines:
            if line[index] == '1':
                helper.append(line)
    else:
        for line in new_lines:
            if line[index] == '0':
                helper.append(line)
    if len(helper) == 1:
        found_oxygen = helper[0]
    dict['first'] = 0   
    new_lines = helper
    helper = []        ### CO2 Part
dict = {
    'first': 0
}
new_lines = all_lines
helper = []
for index in range(0, 12):
    for line in new_lines:
        if line[index] == '1':
            dict['first'] = dict['first'] + 1    
        if dict['first'] >= (len(new_lines) / 2):
            for line in new_lines:
                if line[index] == '0':
                    helper.append(line)
        else:
            for line in new_lines:
                if line[index] == '1':
                    helper.append(line)
        if len(helper) == 1:
            found_co2 = helper[0]
        dict['first'] = 0   
        new_lines = helper
        helper = [] 
        print('Oxygen: ' + found_oxygen)
print('CO2: ' + found_co2)
result = int(found_oxygen, 2) * int(found_co2, 2)
print('Result: ' + str(result))
