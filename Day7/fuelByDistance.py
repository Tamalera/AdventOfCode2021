input_file = open('input.txt', 'r')
crabs = input_file.readlines()

all_crabs = crabs[0].split(',')
def sum_of_number(abs_dist):
    sum = 0
    for i in range(0, abs_dist + 1):
        sum = sum + i
        i = i + 1
    return sum

sums = {}
for i in range(0, len(all_crabs) + 1):
    sums[i] = 0

for crab in all_crabs:
    for index in range(0, len(all_crabs) + 1):
        fuel = sums.get(index) + sum_of_number(abs(int(crab) - index))
        sums.update({index:fuel})


# 0 is not valid
sums = {key:val for key, val in sums.items() if val != 0}

lowest_fuel_sum = min(sums, key=sums.get)

# This will take a bit for calculating, as it is not efficient ;)
# print(sums)
print('Fuel Saving Distance: ' + str(lowest_fuel_sum))
print('Fuel Saving Distance: ' + str(sums[lowest_fuel_sum]))