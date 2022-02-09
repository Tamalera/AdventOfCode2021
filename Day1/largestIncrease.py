input_file = open('input.txt', 'r')
all_lines = input_file.readlines()
increase_counter = 0
previous_line = 0
for line in all_lines:
    if int(line) > previous_line:
        increase_counter = increase_counter + 1
    previous_line = int(line)
    
print(increase_counter-1) # Minus one because the first line will always be counted with initial one