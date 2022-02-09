input_file = open('input.txt', 'r')
all_lines = input_file.readlines()
gamma = ''
epsilon = ''

dict = {
    '1': 0, 
    '2': 0, 
    '3': 0,
    '4': 0, 
    '5': 0, 
    '6': 0,
    '7': 0, 
    '8': 0, 
    '9': 0,
    '10': 0, 
    '11': 0, 
    '12': 0
}
for line in all_lines:
    for l, index in zip(line, range(0,12)):
        if l == '1':
            dict[str(index + 1)] = dict[str(index + 1)] + 1
    for item in dict.values():
        if item > 500:
            gamma = gamma + '1'
        else:
            gamma = gamma + '0'
            print(gamma)
        for num in gamma:
            if num == '0':
                epsilon = epsilon + '1'
            else:
                epsilon = epsilon + '0'
                print(epsilon)
    result = int(gamma, 2) * int(epsilon, 2)
    print(result)