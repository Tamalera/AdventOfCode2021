from collections import Counter

input_file = open('input.txt', 'r')
all_lines = input_file.readlines()


class Node:
    def __init__(self, name, tries):
        self.name = name
        self.tries = tries

    def decrease_tries(self):
        self.tries = self.tries - 1

    def can_visit(self):
        return self.tries >= 0


def set_tries(name):
    if name.isupper():
        return 100000000  # any large number you think the node will not be visited
    if name == 'start' or name == 'end':
        return 1
    if name.islower():
        return 2


def make_graph():
    res_graph = {}
    for line in all_lines:
        res = line.strip('\n').split('-')
        if res[0] in res_graph:
            res_graph[res[0]] += [Node(res[1], set_tries(res[1]))]
        else:
            res_graph[res[0]] = [Node(res[1], set_tries(res[1]))]
        # Both directions are allowed
        if res[1] in res_graph:
            res_graph[res[1]] += [Node(res[0], set_tries(res[0]))]
        else:
            res_graph[res[1]] = [Node(res[0], set_tries(res[0]))]
    # print(graph)
    return res_graph


def find_all_paths(a_graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in a_graph:
        return []
    paths = []
    for node in a_graph[start]:
        node.decrease_tries()
        if node not in path or node.name.isupper():
            new_paths = find_all_paths(a_graph, node.name, end, path)
            for new_path in new_paths:
                paths.append(new_path)
        elif node in path and node.name.islower() and node.can_visit():
            new_paths = find_all_paths(a_graph, node.name, end, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths


# Setup graph
graph = make_graph()

# Find all paths
all_paths = find_all_paths(graph, 'start', 'end')
# print(all_paths)
print(str(len(all_paths)))

# It does not work. no clue why. RIP
