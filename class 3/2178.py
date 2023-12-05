import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split( ))
graph = []

for _ in range(N):
    blocks_str = sys.stdin.readline().strip()
    blocks = []
    for i in range(M):
        blocks.append(int(blocks_str[i]))
    graph.append(blocks)

def bfs(x, y):
    q = deque([[y, x]])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        [cury, curx] = q.popleft()
        for i in range(4):
            if 0 <= curx + dx[i] < M and 0 <= cury + dy[i] < N:
                if graph[cury+dy[i]][curx+dx[i]] == 1 and [curx+dx[i], cury+dy[i]] != [x, y]:
                    graph[cury+dy[i]][curx+dx[i]] = graph[cury][curx] + 1
                    q.append([cury+dy[i], curx+dx[i]])
    
    return graph[N-1][M-1]

print(bfs(0, 0))