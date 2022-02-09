input_file = open('input.txt', 'r')
all_lines = input_file.readlines()

# Prepare matrix
mat = []
for line in all_lines:
    l = line.strip('\n')
    mat.append(list(l))

# print(mat)

# start from 0, 0
x = y = 0
allPaths = []
paths = []
final_sum = 100000000000  # some ridiculous high number


def getSum(whole_path):
    global final_sum
    sum = 0
    for index, value in enumerate(whole_path):
        sum = sum + int(value)
    sum = sum - int(whole_path[0])
    if sum < final_sum:
        final_sum = sum
    return final_sum


def findPaths(mat, path, i, j):
    # base case for recursion
    if not mat or not len(mat):
        return

    (M, N) = (len(mat), len(mat[0]))

    # Path found
    if i == M - 1 and j == N - 1:
        sum = getSum(path + [mat[i][j]])
        print(str(sum))
        return

    path.append(mat[i][j])

    # Move to the lowest right or down, when in doubt, then move down

    # move down
    if 0 <= i + 1 < M and 0 <= j < N:
        findPaths(mat, path, i + 1, j)

    # move right
    if 0 <= i < M and 0 <= j + 1 < N:
        findPaths(mat, path, i, j + 1)

    # backtracking
    path.pop()


findPaths(mat, paths, x, y)

# This ran easily for 24h... so I stopped it. RIP