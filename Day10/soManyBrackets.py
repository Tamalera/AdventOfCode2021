import queue

input_file = open('input.txt', 'r')
all_lines = input_file.readlines()

opening_brackets = ['[', '(', '<', '{']

illegal_chars = []

def is_not_corresponding(opening, closing):
    if opening == '[' and closing != ']':
        return True
    if opening == '(' and closing != ')':
        return True
    if opening == '<' and closing != '>':
        return True
    if opening == '{' and closing != '}':
        return True
    return False


for line in all_lines:
    bracket_queue = queue.LifoQueue(len(line))
    for bracket in line:
        if bracket in opening_brackets:
            bracket_queue.put(bracket)
        else:
            if bracket != '\n' and is_not_corresponding(bracket_queue.get(), bracket):
                illegal_chars.append(bracket)
                break


# print(illegal_chars)
sum_of_brackets = 0
for b in illegal_chars:
    if b == ')':
        sum_of_brackets = sum_of_brackets + 3
    if b == ']':
        sum_of_brackets = sum_of_brackets + 57
    if b == '}':
        sum_of_brackets = sum_of_brackets + 1197
    if b == '>':
        sum_of_brackets = sum_of_brackets + 25137

print(sum_of_brackets)