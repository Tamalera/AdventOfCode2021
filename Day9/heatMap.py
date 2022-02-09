with open("input.txt") as f:
    heat_map = [[x for x in row.strip('\n')] for row in f]
lowest_point_found = []
for i in range(len(heat_map)):
    for j, value in enumerate(heat_map[i]):
        neighbours = []
        # TOP
        if i != 0:
            neighbours.append(heat_map[i - 1][j])
        # BOTTOM
        if i < len(heat_map) - 1 and j < len(heat_map):
            neighbours.append(heat_map[i + 1][j])
        # LEFT
        if j != 0:
            neighbours.append(heat_map[i][j - 1])
        # RIGHT
        if j < len(heat_map[i]) - 1 and i < len(heat_map):
            neighbours.append(heat_map[i][j + 1])

        max_nighbours = len(neighbours)
        counter = 0
        for neighbour in neighbours:
            if neighbour > heat_map[i][j]:
                counter = counter + 1

        if max_nighbours == counter:
            lowest_point_found.append(heat_map[i][j])

sum_low = 0
for low in lowest_point_found:
    sum_low = sum_low + int(low) + 1

print(sum_low)

