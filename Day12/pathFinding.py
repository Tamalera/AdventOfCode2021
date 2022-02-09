input_file = open('input.txt', 'r')
all_lines = input_file.readlines()

def make_graph():
    graph = {}
    for line in all_lines:
        res = line.strip('\n').split('-')
        if res[0] in graph:
            graph[res[0]] += [res[1]]
        else: 
            graph[res[0]] = [res[1]]
        # Both directions are allowed
        if res[1] in graph:
            graph[res[1]] += [res[0]]
        else: 
            graph[res[1]] = [res[0]]
    # print(graph)
    return graph

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path or node.isupper():
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

# Setup graph
graph = make_graph()

# Find all paths
all_paths = find_all_paths(graph, 'start', 'end')
# print(all_paths)
print(str(len(all_paths)))

