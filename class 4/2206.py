import sys
from collections import deque

def bfs(x, y, graph):
    visited = [[[0 for _ in range(2)] for _ in range(M)] for _ in range(N)]
    visited[y][x][0] = 1
    q = deque([[x, y, 0]])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while q:
        [curx, cury, curz] = q.popleft()
        for i in range(4):
            newx = curx + dx[i]
            newy = cury + dy[i]
            if 0 <= newx < M and 0 <= newy < N:
                if curz == 0:
                    if not visited[newy][newx][0]:
                        if graph[newy][newx]:
                            q.append([newx, newy, 1])
                            visited[newy][newx][1] = visited[cury][curx][0] + 1
                        else:
                            q.append([newx, newy, 0])
                            visited[newy][newx][0] = visited[cury][curx][0] + 1
                else:
                    if not visited[newy][newx][1] and not graph[newy][newx]:
                        q.append([newx, newy, 1])
                        visited[newy][newx][1] = visited[cury][curx][1] + 1
    if visited[N-1][M-1][0] > 0:
        if visited[N-1][M-1][1] > 0:
            return min(visited[N-1][M-1])
        else:
            return visited[N-1][M-1][0]

    else:
        if visited[N-1][M-1][1] > 0:
            return visited[N-1][M-1][1]
        else:
            return -1

N, M = map(int, sys.stdin.readline().split( ))

board = []
walls = []

for i in range(N):
    line = sys.stdin.readline().strip()
    lines = []
    for j in range(M):
        lines.append(int(line[j]))
        if line[j] == '1':
            walls.append([i, j])
    board.append(lines)

print(bfs(0, 0, board))