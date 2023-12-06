import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().split( ))

tomato = []
for _ in range(H):
    boxes = []
    for _ in range(N):
        lines = list(map(int, sys.stdin.readline().split( )))
        boxes.append(lines)
    tomato.append(boxes)

q = deque([])
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0 ,0]
dz = [0, 0, 0, 0, 1, -1]
max_days = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato[i][j][k] == 1:
                q.append([i, j, k])

while q:
    [curz, cury, curx] = q.popleft()
    for i in range(6):
        if 0 <= curx + dx[i] < M and 0 <= cury + dy[i] < N and 0 <= curz + dz[i] < H:
            if tomato[curz + dz[i]][cury + dy[i]][curx + dx[i]] == 0:
                tomato[curz + dz[i]][cury + dy[i]][curx + dx[i]] = tomato[curz][cury][curx] + 1
                q.append([curz + dz[i], cury + dy[i], curx + dx[i]])
                if tomato[curz][cury][curx] > max_days:
                    max_days = tomato[curz][cury][curx]

isDone = True
for i in range(H):
    for j in range(N):
        if 0 in tomato[i][j]:
            isDone = False

if isDone:
    print(max_days)
else:
    print(-1)