input_file = open('input.txt', 'r')
all_lines = input_file.readlines()

switched_on_cubes = set()

for line in all_lines:
    res = line.strip('\n').replace(' ', ',').split(',')
    state = res[0]
    x_coords = res[1].strip('x=').split('..')
    y_coords = res[2].strip('y=').split('..')
    z_coords = res[3].strip('z=').split('..')
    if abs(int(x_coords[0])) > 50:
        break
    for i in range(int(x_coords[0]), int(x_coords[1]) + 1):
        for j in range(int(y_coords[0]), int(y_coords[1]) + 1):
            for k in range(int(z_coords[0]), int(z_coords[1]) + 1):
                if state == 'on':
                    switched_on_cubes.add((i, j, k))
                else:
                    if (i, j, k) in switched_on_cubes:
                        switched_on_cubes.remove((i, j, k))

print(switched_on_cubes)
print(str(len(switched_on_cubes)))
