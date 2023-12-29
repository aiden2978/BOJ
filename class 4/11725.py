import sys
sys.setrecursionlimit(10**8)

def dfs(start):
    visited[start] = 1
    for i in tree[start]:
        if visited[i] == 0:
            dist[i] = dist[start] + 1
            dfs(i)

N = int(sys.stdin.readline())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    i, j = map(int, sys.stdin.readline().split( ))
    tree[i].append(j)
    tree[j].append(i)
dist = [0 for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

dfs(1)

for i in range(2, N+1):
    for j in tree[i]:
        if dist[j] == dist[i] - 1:
            print(j)
            break