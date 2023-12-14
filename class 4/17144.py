import sys
import copy

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def diff(x, y):
    global board, newboard
    diffused = board[y][x] // 5
    for i in range(4):
        if 0 <= x + dx[i] < C and 0 <= y + dy[i] < R and board[y + dy[i]][x + dx[i]] != -1:
            newboard[y + dy[i]][x + dx[i]] += diffused
            newboard[y][x] -= diffused

R, C, T = map(int, sys.stdin.readline().split( ))

board = []
newboard = []
for i in range(R):
    lines = list(map(int, sys.stdin.readline().split( )))
    board.append(lines)
    newboard.append(lines[:])
    if lines[0] == -1:
        ac = i

sum = 2
for _ in range(T):
    for i in range(R):
        for j in range(C):
            if board[i][j] != -1:
                for k in range(4):
                    if 0 <= j + dx[k] < C and 0 <= i + dy[k] < R and board[i + dy[k]][j + dx[k]] != -1:
                        newboard[i][j] += board[i + dy[k]][j + dx[k]] // 5
                        newboard[i][j] -= board[i][j] // 5
    
    for i in range(ac - 2, 0, -1):
        newboard[i][0] = newboard[i - 1][0]
    for i in range(C - 1):
        newboard[0][i] = newboard[0][i + 1]
    for i in range(ac - 1):
        newboard[i][C - 1] = newboard[i + 1][C - 1]
    for i in range(C - 2, 0, -1):
        newboard[ac - 1][i + 1] = newboard[ac - 1][i]
    newboard[ac - 1][1] = 0

    for i in range(ac + 1, R - 1):
        newboard[i][0] = newboard[i + 1][0]
    for i in range(C - 1):
        newboard[R - 1][i] = newboard[R - 1][i + 1]
    for i in range(R - 2, ac - 1, -1):
        newboard[i + 1][C - 1] = newboard[i][C - 1]
    for i in range(C - 2, 0, -1):
        newboard[ac][i + 1] = newboard[ac][i]
    newboard[ac][1] = 0

    board = copy.deepcopy(newboard)

for i in range(R):
    for j in range(C):
        sum += board[i][j]

print(sum)