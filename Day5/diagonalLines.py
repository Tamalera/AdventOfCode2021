input_file = open('input.txt', 'r')
all_lines = input_file.readlines()

space_field = [0]*1000 # sounds about right
for i in range (1000):
    space_field[i] = [0]*1000
    for j in range (1000):
        space_field[i][j] = 0

# To make it easier to get the points, I manually replaced the arrow ith a comma
for line in all_lines:
    line_list = line.strip('\n').split(',')
    x1 = int(line_list[0])
    y1 = int(line_list[1])
    x2 = int(line_list[2])
    y2 = int(line_list[3])

    # Mark the horizontal lines
    if x1 == x2:
        if y1 < y2:
            for i in range(y1, y2 + 1):
                space_field[x1][i] = space_field[x1][i] + 1 # x1 == x2 as determined above
        else:
            for i in range(y2, y1 + 1):
                space_field[x1][i] = space_field[x1][i] + 1

    # Mark the vertical lines
    if y1 == y2:
        if x1 < x2:
            for i in range(x1, x2 + 1):
                space_field[i][y1] = space_field[i][y1] + 1
        else:
            for i in range(x2, x1 + 1):
                space_field[i][y1] = space_field[i][y1] + 1
    
    # Mark the diagonal lines (45°)
    # x1 < x2 && y1 < y2 up to down or x1 > x2 && y1 > y2 down to up
    # . . . . . .
    # . x . . . .
    # . . x . . .
    # . . . x . .
    # x1 < x2 && y1 > y2 fup to down or x1 > x2 && y1 < y2 down to up
    # . . . . . .
    # . . . x . .
    # . . x . . .
    # . x . . . .
    if abs(x1 - x2) == abs(y1 - y2):
        if x1 < x2 and y1 < y2:
            for i in range(0, abs(x1 - x2) + 1):
                space_field[x1 + i][y1 + i] = space_field[x1 + i][y1 + i] + 1
        elif x1 > x2 and y1 > y2:
            for i in range(0, abs(x1 - x2) + 1):
                space_field[x1 - i][y1 - i] = space_field[x1 - i][y1 - i] + 1
        elif x1 < x2 and y1 > y2:
            for i in range(0, abs(x1 - x2) + 1):
                space_field[x1 + i][y1 - i] = space_field[x1 + i][y1 - i] + 1
        elif x1 > x2 and y1 < y2:
            for i in range(0, abs(x1 - x2) + 1):
                space_field[x1 - i][y1 + i] = space_field[x1 - i][y1 + i] + 1




counter = 0
for i in range (0, 1000):
    for j in range(0, 1000):
        if space_field[i][j] > 1:
            counter += 1

print('Total dangerous fields: ' + str(counter))