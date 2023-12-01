import sys
from collections import deque

# dfs
def dfs(idx):
    global visited, result_dfs
    # 방문한 node에 추가하고 탐색한 순서대로 결과 list에 추가
    visited[idx] = 1
    result_dfs.append(idx)
    # 현재 node와 인접해 있고, 방문하지 않은 node에 대해 재귀 호출
    for i in range(1, N+1):
        if not visited[i] and graph[idx][i]:
            dfs(i)

# bfs
def bfs(idx):
    global visited, result_bfs
    visited = [0 for _ in range(N+1)]
    visited[idx] = 1
    q = deque([idx])
    #  queue가 빌 때까지 시행
    while q:
        # queue의 맨 앞, 즉 최단 거리의 node를 pop
        cur = q.popleft()
        result_bfs.append(cur)
        # 앞에서 pop한 node와 인접해 있고, 방문하지 않은 node를 차례로 queue에 추가
        for i in range(1, N+1):
            if not visited[i] and graph[cur][i]:
                visited[i] = 1
                q.append(i)

N, M ,V = map(int, sys.stdin.readline().split( ))
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
result_dfs = []
result_bfs = []

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split( ))
    graph[a][b], graph[b][a] = 1, 1

dfs(V)
print(*result_dfs)

bfs(V)
print(*result_bfs)