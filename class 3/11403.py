import sys
from collections import deque

N = int(sys.stdin.readline())
graph = []
q = deque([])

for i in range(N):
    lines = list(map(int, sys.stdin.readline().split( )))
    graph.append(lines)
    for j in range(N):
        if lines[j] == 1:
            q.append([i, j])

while q:
    [curi, curj] = q.popleft()
    for k in range(N):
        if graph[curj][k] == 1 and graph[curi][k] == 0:
            graph[curi][k] = 1
            q.append([curi, k])

for i in range(N):
    print(*graph[i])