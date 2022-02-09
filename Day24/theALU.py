input_file = open('input.txt', 'r')
all_lines = input_file.readlines()

w = 0
x = 0
y = 0
z = 0

def take_input(monad_digit):
    return monad_digit

def mul(a, b):
    return a * b

def add(a, b):
    return a + b

def mod(a, b):
    return a % b

def dif(a, b):
    if b != 0:
        return a/b
    else:
        raise Exception("Cannot divide by zero")

def eql(a, b):
    return 1 if a == b else 0


def get_action(x, param):
    pass


def perform_action(res):
    global w, x, y, z
    if res[1] == 'x':
        x = get_action(x, res[2])

methods = []
counter = 0
result = []
for line in all_lines:
    res = line.strip('\n').split(' ')
    result.append(res)
    counter = counter + 1
    if counter == 18:
        methods.append(result)
        result = []
        counter = 0

# print(methods)
# inp w
# mul x 0
# add x z
# mod x 26
# div z 26
# add x -9
# eql x w
# eql x 0
# mul y 0
# add y 25
# mul y x
# add y 1
# mul z y
# mul y 0
# add y w
# add y 10
# mul y x
# add z y
# z = z + y for z to be 0 y needs to be 0 of z = -y
# y = (w + some_num) * x
# z = -((w + some_num) * x)
# z = -((input_num + some_num) * 0|1) -> of y == 0, then z == 0, else z = -(input_num + some_num)
# So x needs to be 0 --> x = ((z mod 26) - 9) == input_num

for i in range(0, 100):
    for j in range(1, 10):
        if(((i%26) - 9) == j):
            print('i: ' + str(i))
            print('j: ' + str(j))

# Got lost....