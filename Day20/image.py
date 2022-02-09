import copy

input_file = open('input.txt', 'r')
all_lines = input_file.readlines()

image_algorythm = all_lines[0].strip('\n')

all_lines = all_lines[2:]  # Image only

infinite_image = []


def append_dark_patch(infinite_image):
    tons_of_dots = []
    for i in range(0, 5100):
        tons_of_dots.append('dot')
    for i in range(0, 2500):
        infinite_image.append(tons_of_dots)


append_dark_patch(infinite_image)

filler = []
for i in range(0, 2500):
    filler.append('dot')

for line in all_lines:
    filler_before = copy.deepcopy(filler)
    res = line.strip('\n')
    for char in res:
        filler_before.append(char)
    for dot in copy.deepcopy(filler):
        filler_before.append(dot)
    output = copy.deepcopy(filler_before)
    infinite_image.append(output)

append_dark_patch(infinite_image)

# From 2500 to 2599 are the original pixels since my algorythm has a light at 0 position,
# all 3x3 dits should light up -> infinite lights
# But that makes no sense, so starting from 2498 2498 to 2602 2602 should be correct
def translate_to_binary(binary_helper):
    for i in range(0, len(binary_helper)):
        if binary_helper[i] == '#':
            binary_helper[i] = 1
        else:
            binary_helper[i] = 0
    binary_number = "".join([str(l) for l in binary_helper])
    binary_res = int(binary_number, 2)
    return binary_res

sum_zero = 0
for i in range(0, len(infinite_image)):
    for j in range(0, len(infinite_image)):
        if infinite_image[i][j] == '#':
            sum_zero = sum_zero + 1

print(str(sum_zero))

infinite_image_first_round = [[i for i in row] for row in infinite_image]

def transform_image_first(row, col):
    binary_helper = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            binary_helper.append(infinite_image[row + i][col + j])

    algo_position = translate_to_binary(binary_helper)
    if image_algorythm[algo_position] == '#':
        infinite_image_first_round[row][col] = '#'
    else:
        infinite_image_first_round[row][col] = '.'


# Check pixel at infinite_image[2499][2499] to [2600][2600] -> rows are filled from 2500 to 2599
for row in range(2499, 2601):
    for col in range(2499, 2601):
        transform_image_first(row, col)

sum_first = 0
for i in range(0, len(infinite_image_first_round)):
    for j in range(0, len(infinite_image_first_round)):
        if infinite_image_first_round[i][j] == '#':
            sum_first = sum_first + 1

print(str(sum_first))

# Second round
infinite_image_second_round = [[i for i in row] for row in infinite_image_first_round]

def transform_image_second(row, col):
    binary_helper = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            binary_helper.append(infinite_image_first_round[row + i][col + j])
    algo_position = translate_to_binary(binary_helper)
    if image_algorythm[algo_position] == '#':
        infinite_image_second_round[row][col] = 1
    else:
        infinite_image_second_round[row][col] = 0

# Check pixel at infinite_image[2498][2498] to [2601][2601] -> rows are filled from 2499 to 2600
for row in range(2498, 2602):
    for col in range(2498, 2602):
        transform_image_second(row, col)

sum = 0
for i in range(0, len(infinite_image_second_round)):
    for j in range(0, len(infinite_image_second_round)):
        if infinite_image_second_round[i][j] == 1:
            sum = sum + 1

print(str(sum))

# This was not correct.
