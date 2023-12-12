import sys

N = int(sys.stdin.readline())
house = []

for _ in range(N):
    lines = list(map(int, sys.stdin.readline().split( )))
    house.append(lines)

pipe_right = [[0 for _ in range(N)] for _ in range(N)]
pipe_down = [[0 for _ in range(N)] for _ in range(N)]
pipe_rightdown = [[0 for _ in range(N)] for _ in range(N)]

pipe_right[0][1] = 1

for i in range(N):
    for j in range(N):
        if i == 0 and j == 1:
            continue
        if house[i][j] == 0:
            if j > 0:
                pipe_right[i][j] += (pipe_right[i][j-1] + pipe_rightdown[i][j-1])
            if i > 0:
                pipe_down[i][j] += (pipe_down[i-1][j] + pipe_rightdown[i-1][j])
            if house[i-1][j] == 0 and house[i][j-1] == 0 and i > 0 and j > 0:
                pipe_rightdown[i][j] += (pipe_right[i-1][j-1] + pipe_down[i-1][j-1] + pipe_rightdown[i-1][j-1])

print((pipe_right[N-1][N-1] + pipe_down[N-1][N-1] + pipe_rightdown[N-1][N-1]))