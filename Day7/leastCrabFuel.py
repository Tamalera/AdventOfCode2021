input_file = open('input.txt', 'r')
crabs = input_file.readlines()

all_crabs = crabs[0].split(',')

sums = {}
for i in range(0, len(all_crabs) + 1):
    sums[i] = 0

for crab in all_crabs:
    for index in range(0, len(all_crabs) + 1):
        fuel = sums.get(index) + abs(int(crab) - index)
        sums.update({index:fuel})


# 0 is not valid
sums = {key:val for key, val in sums.items() if val != 0}

lowest_fuel_sum = min(sums, key=sums.get)

print(sums)
print('Fuel Saving Distance: ' + str(lowest_fuel_sum))
print('Fuel Saving Distance: ' + str(sums[lowest_fuel_sum]))