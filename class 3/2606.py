import sys
from collections import deque

def bfs(idx):
    global visited
    visited[idx] = 1
    for i in range(1, N+1):
        if not visited[i] and graph[idx][i]:
            bfs(i)

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split( ))
    graph[a][b], graph[b][a] = 1, 1

bfs(1)
print(sum(visited) - 1)