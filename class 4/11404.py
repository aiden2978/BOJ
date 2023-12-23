import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[10**8 + 1 for _ in range(N+1)] for _ in range(N+1)]
for i in range(1, N+1):
    graph[i][i] = 0

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split( ))
    graph[a][b] = min(c, graph[a][b])

# i를 거쳐갔을 때 더 값이 작아진다면 최소거리 갱신
for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

for i in range(1, N+1):
    for j in range(1, N+1):
        if graph[i][j] == 10**8 + 1:
            graph[i][j] = 0
    print(*graph[i][1:])