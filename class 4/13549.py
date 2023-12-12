import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split( ))

graph = [0 for _ in range(100001)]

def bfs(idx):
    q = deque([idx])
    while q:
        cur = q.popleft()
        if cur == K:
            break 
        if 2*cur <= 100000:
            if not graph[2*cur]:
                graph[2*cur] = graph[cur]
                q.append(2*cur)
        if cur + 1 <= 100000:
            if not graph[cur + 1]:
                graph[cur + 1] = graph[cur] + 1
                q.append(cur + 1)
        if cur - 1 >= 0:
            if not graph[cur - 1]:
                graph[cur - 1] = graph[cur] + 1
                q.append(cur - 1)
    return graph[K]

print(bfs(N))