import sys

# □
# □
# □
# □
def tet1_1(list, i, j):
    return list[i][j] + list[i][j+1] + list[i][j+2] + list[i][j+3]

# □ □ □ □
def tet1_2(list, i, j):
    return list[i][j] + list[i+1][j] + list[i+2][j] + list[i+3][j]

# □ □
# □ □
def tet2(list, i, j):
    return list[i][j] + list[i][j+1] + list[i+1][j] + list[i+1][j+1]

# □
# □
# □ □
def tet3_1(list, i, j):
    return list[i][j] + list[i][j+1] + list[i][j+2] + list[i+1][j+2]

#     □
# □ □ □
def tet3_2(list, i, j):
    return list[i+2][j] + list[i][j+1] + list[i+1][j+1] + list[i+2][j+1]

# □ □
#   □
#   □
def tet3_3(list, i, j):
    return list[i][j] + list[i+1][j] + list[i+1][j+1] + list[i+1][j+2]

# □ □ □
# □
def tet3_4(list, i, j):
    return list[i][j] + list[i+1][j] + list[i+2][j] + list[i][j+1]

#   □
#   □
# □ □
def tet3_5(list, i, j):
    return list[i+1][j] + list[i+1][j+1] + list[i][j+2] + list[i+1][j+2]

# □ □ □
#     □
def tet3_6(list, i, j):
    return list[i][j] + list[i+1][j] + list[i+2][j] + list[i+2][j+1]

# □ □
# □
# □
def tet3_7(list, i, j):
    return list[i][j] + list[i+1][j] + list[i][j+1] + list[i][j+2]

# □
# □ □ □
def tet3_8(list, i, j):
    return list[i][j] + list[i][j+1] + list[i+1][j+1] + list[i+2][j+1]

# □
# □ □
#   □
def tet4_1(list, i, j):
    return list[i][j] + list[i][j+1] + list[i+1][j+1] + list[i+1][j+2]

#   □ □
# □ □
def tet4_2(list, i, j):
    return list[i+1][j] + list[i+2][j] + list[i][j+1] + list[i+1][j+1]

#   □
# □ □
# □
def tet4_3(list, i, j):
    return list[i+1][j] + list[i][j+1] + list[i+1][j+1] + list[i][j+2]

# □ □
#   □ □
def tet4_4(list, i, j):
    return list[i][j] + list[i+1][j] + list[i+1][j+1] + list[i+2][j+1]

# □ □ □
#   □
def tet5_1(list, i, j):
    return list[i][j] + list[i+1][j] + list[i+2][j] + list[i+1][j+1]

# □
# □ □
# □
def tet5_2(list, i, j):
    return list[i][j] + list[i][j+1] + list[i+1][j+1] + list[i][j+2]

#   □
# □ □ □
def tet5_3(list, i, j):
    return list[i+1][j] + list[i][j+1] + list[i+1][j+1] + list[i+2][j+1]

#   □
# □ □
#   □
def tet5_4(list, i, j):
    return list[i+1][j] + list[i][j+1] + list[i+1][j+1] + list[i+1][j+2]

N, M = map(int, sys.stdin.readline().split( ))
board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split( ))))

max_value = 0

# □
# □
# □
# □
for i in range(N):
    for j in range(M-3):
        if tet1_1(board, i, j) > max_value:
            max_value = tet1_1(board, i, j)

# □ □ □ □
for i in range(N-3):
    for j in range(M):
        if tet1_2(board, i, j) > max_value:
            max_value = tet1_2(board, i, j)

# □ □
# □ □
for i in range(N-1):
    for j in range(M-1):
        if tet2(board, i, j) > max_value:
            max_value = tet2(board, i, j)

# □ □
# □ □
# □ □
for i in range(N-1):
    for j in range(M-2):
        local_max = max(tet3_1(board, i, j), tet3_3(board, i, j), tet3_5(board, i, j), tet3_7(board, i, j), tet4_1(board, i, j), tet4_3(board, i, j), tet5_2(board, i, j), tet5_4(board, i, j))
        if local_max > max_value:
            max_value = local_max

# □ □ □
# □ □ □
for i in range(N-2):
    for j in range(M-1):
        local_max = max(tet3_2(board, i, j), tet3_4(board, i, j), tet3_6(board, i, j), tet3_8(board, i, j), tet4_2(board, i, j), tet4_4(board, i, j), tet5_1(board, i, j), tet5_3(board, i, j))
        if local_max > max_value:
            max_value = local_max

print(max_value)