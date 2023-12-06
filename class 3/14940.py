import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split( ))

graph = []
goal = [0, 0]

for i in range(n):
    lines = list(map(int, sys.stdin.readline().split( )))
    for j in range(m):
        if lines[j] == 2:
            goal = [j, i]
            lines[j] = 0
        elif lines[j] == 1:
            lines[j] = -1
    graph.append(lines)

def bfs(x, y):
    q = deque([[y, x]])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        [cury, curx] = q.popleft()
        for i in range(4):
            if 0 <= curx + dx[i] < m and 0 <= cury + dy[i] < n:
                if graph[cury+dy[i]][curx+dx[i]] == -1:
                    graph[cury+dy[i]][curx+dx[i]] = graph[cury][curx] + 1
                    q.append([cury+dy[i], curx+dx[i]])

bfs(goal[0], goal[1])

for i in range(n):
    print(*graph[i])