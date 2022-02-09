input_file = open('input.txt', 'r')
all_lines = input_file.readlines()

class FlashyOctopus():
    def __init__(self, number):
        self.number = number
        self.flashed = False
    
    def set_number(self, num):
        self.number = num

    def increase(self):
        self.number = self.number + 1
    
    def flash(self):
        self.flashed = True

    def reset_flash(self):
        self.flashed = False

    def did_flash(self):
        return self.flashed

def increase_by_one(swarm):
    for i in range(0, 10):
        for j in range(0, 10):
            swarm[i][j].increase()

def do_flash(swarm):
    for i in range(0, 10):
        for j in range(0, 10):
            if swarm[i][j].number > 9 and swarm[i][j].did_flash() == False:
                swarm[i][j].flash()
                set_adjacent(swarm, i, j)

def set_adjacent(swarm, i, j):
    # TOP
    if i - 1 >= 0:
        swarm[i - 1][j].increase()
    # TOP LEFT
    if i - 1 >= 0 and j - 1 >= 0:
        swarm[i - 1][j - 1].increase()
    # TOP RIGHT
    if i - 1 >= 0 and j + 1 < 10:
        swarm[i - 1][j + 1].increase()
    # LEFT
    if j - 1 >= 0:
        swarm[i][j - 1].increase()
    # RIGHT
    if j + 1 < 10:
        swarm[i][j + 1].increase()
    # BOTTOM
    if i + 1 < 10:
        swarm[i + 1][j].increase()
    # BOTTOM LEFT
    if i + 1 < 10 and j - 1 >= 0:
        swarm[i + 1][j - 1].increase()
    # BOTTOM RIGHT
    if i + 1 < 10 and j + 1 < 10:
        swarm[i + 1][j + 1].increase()
    do_flash(swarm)

    
def count_flashed(swarm, step):
    flashing = 0
    for i in range(0, 10):
        for j in range(0, 10):
            if swarm[i][j].did_flash():
                flashing = flashing + 1
                swarm[i][j].reset_flash()
                swarm[i][j].set_number(0)
    if max_flashing == flashing:
        print(str(step - 1)) # Because it is AFTER the step

swarm = []
for line in all_lines:
    res = line.strip('\n')
    row = []
    for l in res:
        row.append(FlashyOctopus(int(l)))
    swarm.append(row)

max_flashing = 100
for step in range(0, 500): # Try first 500, if needed, put up to 1000 or even more
    increase_by_one(swarm)
    do_flash(swarm)
    count_flashed(swarm, step)