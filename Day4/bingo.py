input_file = open('input.txt', 'r')
all_lines = input_file.readlines()

# prepare input file such, that drawn numbers are copied here and 
# that double space is replaces with single space and
# remove leading spaces and
# add new line at the end
bingo_numbers = [83,69,34,46,30,23,19,75,22,37,89,78,32,39,11,44,95,43,26,48,84,53,94,88,18,40,62,35,27,42,15,2,91,20,4,64,99,71,54,97,52,36,28,7,74,45,70,86,98,1,61,50,68,6,77,8,57,47,51,72,65,3,49,24,79,13,17,92,41,80,63,67,82,90,55,0,10,93,38,21,59,73,33,31,9,76,5,66,16,58,85,87,12,29,25,14,96,56,60,81]


class BingoField():
    def __init__(self):
        self.number = 0
        self.marked = False
    
    def set_number(self, num):
        self.number = num
    
    def mark(self):
        self.marked = True

    def is_marked(self):
        return self.marked

class BingoBoard():
    def __init__(self):
        self.board = [[BingoField() for j in range(0, 5)] for i in range(0, 5)]

    def draw_board(self):
        for row in self.board:
            for i in range(0, 5):
                print(row[i].number, row[i].marked)

def bingo_found(all_boards):
    for boards in all_boards:
        # check rows
        for row in boards.board:
            counter = 0
            for field in row:
                if field.is_marked():
                    counter = counter + 1
            if counter == 5:
                boards.draw_board()
                calculate_board_score(boards)
                return True
        #check cols
        col_counter = 0
        for i in range(0, 5):
            for num in boards.board[i]:
                if num.is_marked():
                    col_counter = col_counter + 1
                else:
                    col_counter = 0
                    break
            if col_counter == 5:
                boards.draw_board()
                calculate_board_score(boards)
                return True
    return False

def calculate_board_score(winning_board):
    sum = 0
    for row in winning_board.board:
        for field in row:
            if field.is_marked() == False:
                sum = sum + field.number
    print('SUM: ' + str(sum))


all_boards = []
new_board = BingoBoard()
counter = 0
for line in all_lines:
    res = line.strip('\n').split(' ')
    
    if res != ['']:
        for row, i in zip(new_board.board[counter], range(0, 5)):
            row.set_number(int(res[i]))
        counter = counter + 1

    else:
        # print('------START-------')
        # new_board.draw_board()
        # print('-------END---------')
        all_boards.append(new_board)
        new_board = BingoBoard()
        counter = 0
    
for bingo in bingo_numbers:
    for boards in all_boards:
        for row in boards.board:
            for field in row:
                if field.number == int(bingo):
                    field.mark()
    if bingo_found(all_boards):
        print('BINGO: ' + str(bingo))
        break

# The last multiplication step I did manually because I was too lazy...