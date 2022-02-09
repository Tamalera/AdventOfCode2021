input_file = open('input.txt', 'r')
all_lines = input_file.readlines()

temporary_output = open("temp_output.txt", "a")
previous_previous_line = 0
previous_line = 0
for line in all_lines:
    sum_of_three = previous_previous_line + previous_line + int(line)
    temporary_output.writelines(str(sum_of_three) + '\n')
    previous_previous_line = previous_line
    previous_line = int(line)

temporary_output.close()# Now do actual counting

temp = open('temp_output.txt', 'r')
lines = temp.readlines()
lines = lines[2:]
# need to start from third line as first one
increase_counter = 0
prev_line = 0
for line in lines:
    if int(line) > prev_line:
        increase_counter = increase_counter + 1
    prev_line = int(line)
    
print(increase_counter - 1)