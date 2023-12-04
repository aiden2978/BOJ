import sys
sys.setrecursionlimit(1000000)

N, M = map(int, sys.stdin.readline().split( ))
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
cnt = 0

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split( ))
    graph[a][b], graph[b][a] = 1, 1

# 연결된 모든 node에 대해 방문 처리
def dfs(idx):
    global visited
    visited[idx] = 1
    for i in range(1, N+1):
        if not visited[i] and graph[idx][i]:
            dfs(i)

if M == 0:
    print(N)
else:
    for i in range(1, N+1):
        if not visited[i]:
            dfs(i)
            cnt += 1
    print(cnt)