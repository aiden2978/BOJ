import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split( ))

graph = [[0 for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split( ))
    graph[a][b], graph[b][a] = 1, 1

def bfs(idx):
    dist = [0 for _ in range(N+1)]
    q = deque([])
    for i in range(1, N+1):
        if graph[idx][i]:
            dist[i] = 1
            q.append(i)
    while q:
        cur = q.popleft()
        for i in range(1, N+1):
            if i != idx and graph[i][cur] and not dist[i]:
                dist[i] = dist[cur] + 1
                q.append(i)
    return sum(dist)

min_value = N**2
min_person = 0
for i in range(1, N+1):
    if bfs(i) < min_value:
        min_value = bfs(i)
        min_person = i
    
print(min_person)