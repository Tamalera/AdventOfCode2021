input_file = open('input.txt', 'r')
all_lines = input_file.readlines()

lines_after_pipe = []
for line in all_lines:
    lines_after_pipe.append(line.partition(' | ')[2])

counter = 0
for line in lines_after_pipe:
    signals = line.strip('\n').split(' ')
    for sig in signals:
        # 1 -> 2 ; 4 -> 4 ; 7 -> 3 ; 8 -> 7
        if len(sig) == 2 or len(sig) == 4 or len(sig) == 3 or len(sig) == 7:
            counter = counter + 1
print(str(counter))
