input_file = open('input_points.txt', 'r')
all_lines = input_file.readlines()

# fold along x=655
folding_along_x = 655

rows = 0
cols = 0

def print_grid(grid):
    for row in grid:
        for col in row:
            print(col, end=" ")
        print()

def find_maximum():
    global cols, rows
    for line in all_lines:
        l = line.strip('\n').split(',')
        if cols < int(l[0]):
            cols = int(l[0])
        if rows < int(l[1]):
            rows = int(l[1])

def fill_grid():
    global line, l
    for line in all_lines:
        l = line.strip('\n').split(',')
        folding_grid[int(l[1])][int(l[0])] = '#'

def fold_once(folding_grid, folding_along_x):
    folded_grid = []
    cut = len(folding_grid[0]) // folding_along_x
    for row in folding_grid:
        first_half = row[:len(row)//cut]
        second_half = row[len(row)//cut:]
        half_row_reverse = first_half[::-1]
        for i in range(0, len(half_row_reverse)):
            if half_row_reverse[i] == '#':
                second_half[i + 1] = '#'
        folded_grid.append(second_half)
    return folded_grid



find_maximum()
folding_grid = [['.' for i in range(0, cols + 1)] for j in range(0, rows + 1)]
fill_grid()

once_folded = fold_once(folding_grid, folding_along_x)

counter = 0
for row in once_folded:
    for sign in row:
        if sign == '#':
            counter = counter + 1
print(str(counter))
