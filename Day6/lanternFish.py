import copy

input_file = open('input.txt', 'r')
all_fish = input_file.readlines()

fish_list = all_fish[0].split(',')
print(len(fish_list))
fish_num = []
for fish in fish_list:
    fish_num.append(int(fish))

max_days = 80
counter = 0
while counter != max_days:
    helper = copy.deepcopy(fish_num)
    for fishy, index in zip(fish_num, range (0, len(fish_num) + 1)):
        if fishy != 0:
            helper[index] = fishy - 1
        else:
            helper[index] = 6
            helper.append(8)
    fish_num = copy.deepcopy(helper)
    counter = counter + 1    

print(len(fish_num))
