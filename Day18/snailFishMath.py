import json

input_file = open('input.txt', 'r')
all_lines = input_file.readlines()

def nest_level(snail_fish_math_input):
    # Sanity check
    if type(snail_fish_math_input) != list:
        return 0

    nesting_level = 0
    for list_part in snail_fish_math_input:
        nesting_level = max(nesting_level, nest_level(list_part))

    # Need to add one as the "base list" is a list
    return nesting_level + 1

def get_list_in_certain_depth(lst, depth):
    result = []
    if depth > 0:
        for elem in get_list_in_certain_depth(lst, depth - 1):
            if isinstance(elem, list):
                result.extend(elem[1:])
    else:
        result = lst
    return result


results = []
for line in all_lines[0:5]:
    res = line.strip('\n')
    l = json.loads(res)

    if results != []:
        results.append(l)
        # Explode and split if necessary
        nesting_level = nest_level(results)
        print(nesting_level)
        if nesting_level > 4:
            innermost_list = get_list_in_certain_depth(results, nesting_level - 2)
            print(innermost_list)
            # Nah thats not it. Giving up. No clue how to do this
            # explode(results)
            # snail_fish_split(results)

    # This is only relevant the first time of the loop
    if results == []:
        results = l
# ?????