import queue

input_file = open('input.txt', 'r')
all_lines = input_file.readlines()

opening_brackets = ['[', '(', '<', '{']

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

def inverse(bracket):
    if bracket == '[':
        return ']'
    if bracket == '(':
        return ')'
    if bracket == '<':
        return '>'
    if bracket == '{':
        return '}'
    if bracket == ']':
        return '['
    if bracket == ')':
        return '('
    if bracket == '>':
        return '<'
    if bracket == '}':
        return '{'

def get_value(bracket):
    if bracket == ']':
        return 2
    if bracket == ')':
        return 1
    if bracket == '>':
        return 4
    if bracket == '}':
        return 3

def remove_last_found(my_list, x):
    my_list.pop(len(my_list) - my_list[::-1].index(x) - 1)

fixed_brackets = []
for line in all_lines:
    is_incomplete = True
    bracket_queue = queue.LifoQueue(len(line))
    for bracket in line:
        if bracket in opening_brackets:
            bracket_queue.put(bracket)
        else:
            if bracket != '\n' and is_not_corresponding(bracket_queue.get(), bracket):
                is_incomplete = False # because it is corrupted
                break

    # Only use the incomplete lines
    brackets = []
    if is_incomplete:
        brackets = []
        for bracket in line:
            if bracket in opening_brackets:
                brackets.append(bracket)
            else:
                if bracket != '\n':
                    remove_last_found(brackets, inverse(bracket))
    if(len(brackets) != 0):
        fixed_brackets.append(brackets)

# print(fixed_brackets)

score_list = []
for bracket_list in fixed_brackets:
    total_score = 0
    reversed_list = list(reversed(bracket_list))
    for b in reversed_list:
        bracket = inverse(b)
        value = get_value(bracket)
        total_score = total_score * 5 + value
    score_list.append(total_score)

sorted_scores = list(sorted(score_list))
# print(sorted_scores)
the_middle = int((len(sorted_scores))/2)
print(str(sorted_scores[the_middle]))