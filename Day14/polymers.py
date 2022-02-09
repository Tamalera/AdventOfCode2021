from collections import Counter

input_file = open('input.txt', 'r')
all_lines = input_file.readlines()

starting = 'SCVHKHVSHPVCNBKBPVHV'

insertion_rules = {}
for line in all_lines:
    res = line.strip('\n').split(' -> ')
    insertion_rules[res[0]] = res[1]

# print(insertion_rules)
def insertion(double_value):
    return insertion_rules[double_value]

def polymerize(primer):
    new_polymer = ''
    for index, value in enumerate(primer):
        double_value = ''
        if index + 1 < len(primer):
            double_value = value + primer[index + 1]
        else:
            new_polymer = new_polymer + primer[index]
        if double_value != '':
            new_polymer = new_polymer + primer[index] + insertion(double_value)
    return new_polymer

# FIRST PART
my_polymer = polymerize(starting) # first round
for i in range(0, 9):
    my_polymer = polymerize(my_polymer)

# print(my_polymer)
counter = Counter(my_polymer)
sorted_by_frequency = counter.most_common()
# print(sorted_by_frequency)
most_common = sorted_by_frequency[0][1]
least_common = sorted_by_frequency[-1][1]
print(str(most_common - least_common))

# SECOND PART: this takes forever, because I don't know how to speed it up XD RIP PART 2
# my_polymer = polymerize(starting) # first round
# for i in range(0, 39):
#     print('ROUND: ' + str(i))
#     my_polymer = polymerize(my_polymer)