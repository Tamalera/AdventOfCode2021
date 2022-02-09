class Cucumber():
    def __init__(self, char):
        self.direction = char
        self.can_move = False

    def set_direction(self, direction):
        self.direction = direction

    def get_direction(self):
        return self.direction

    def set_can_move(self, yes_or_no):
        self.can_move = yes_or_no

    def it_can_move(self):
        return self.can_move

input_file = open('input.txt', 'r')
all_lines = input_file.readlines()

# with open("test.txt") as f:
#     field = [[Cucumber(x) for x in row.strip('\n')] for row in f]

field = []
for line in all_lines:
    l = []
    res = line.strip('\n')
    for char in res:
        l.append(Cucumber(char))
    field.append(l)

# print(str(len(field)))
# print(str(len(field[0])))
move_counter = 0
for step in range(1, 1000):

    # Check EAST
    for i in range(len(field)):
        for j in range(len(field[i])):
            if (j + 1) == len(field[i]):
                if field[i][j].get_direction() == '>' and field[i][0].get_direction() == '.':
                    field[i][j].set_can_move(True)
            elif field[i][j].get_direction() == '>' and field[i][j + 1].get_direction() == '.':
                field[i][j].set_can_move(True)

    # Move EAST
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j].it_can_move():
                if (j + 1) == len(field[i]):
                    field[i][0].set_direction('>')
                    field[i][j].set_direction('.')
                    field[i][j].set_can_move(False)
                    move_counter = move_counter + 1
                else:
                    field[i][j + 1].set_direction('>')
                    field[i][j].set_direction('.')
                    field[i][j].set_can_move(False)
                    move_counter = move_counter + 1

    # Check SOUTH
    for i in range(len(field)):
        for j in range(len(field[i])):
            if (i + 1) == len(field):
                if field[i][j].get_direction() == 'v' and field[0][j].get_direction() == '.':
                    field[i][j].set_can_move(True)
            elif field[i][j].get_direction() == 'v' and field[i + 1][j].get_direction() == '.':
                field[i][j].set_can_move(True)

    # Move SOUTH
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j].get_direction() == 'v' and field[i][j].it_can_move():
                if (i + 1) == len(field):
                    field[0][j].set_direction('v')
                    field[i][j].set_direction('.')
                    field[i][j].set_can_move(False)
                    move_counter = move_counter + 1
                else:
                    field[i + 1][j].set_direction('v')
                    field[i][j].set_direction('.')
                    field[i][j].set_can_move(False)
                    move_counter = move_counter + 1


    print('Step: ' + str(step))
    print('Counter: ' + str(move_counter))
    if move_counter == 0:
        print(str(step))
        break
    else: # next round
        move_counter = 0
        for i in range(len(field)):
            for j in range(len(field[i])):
                if field[i][j].it_can_move():
                    raise('ERROR: resetting can_move_failed!')