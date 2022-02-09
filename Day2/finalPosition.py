input_file = open('input.txt', 'r')
all_lines = input_file.readlines()
positions = []
numbers = []
for line in all_lines:
    l = line.split()
    positions.append(l[0])
    numbers.append(int(l[1]))

total_depth = 0
total_dist = 0
for x, y in zip(positions, numbers):
    if x == 'forward':
        total_dist = total_dist + int(y)
    elif x == 'down':
        total_depth = total_depth + int(y)
    elif x == 'up':
        total_depth = total_depth - int(y)
    else:
        print('Unknown position')
        distance = total_dist * total_depth
print(str(distance))