import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split( ))

tomato = []
for _ in range(N):
    lines = list(map(int, sys.stdin.readline().split( )))
    tomato.append(lines)

q = deque([])
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
max_days = 0
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            q.append([i, j])

while q:
    [cury, curx] = q.popleft()
    for i in range(4):
        if 0 <= curx + dx[i] < M and 0 <= cury + dy[i] < N:
            if tomato[cury + dy[i]][curx + dx[i]] == 0:
                tomato[cury + dy[i]][curx + dx[i]] = tomato[cury][curx] + 1
                q.append([cury + dy[i], curx + dx[i]])
                if tomato[cury][curx ] > max_days:
                    max_days = tomato[cury][curx]

isDone = True
for i in range(N):
    if 0 in tomato[i]:
        isDone = False

if isDone:
    print(max_days)
else:
    print(-1)