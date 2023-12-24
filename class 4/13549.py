import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split( ))

graph = [-1 for _ in range(100001)]

def bfs(idx):
    graph[idx] = 0
    q = deque([idx])
    while q:
        cur = q.popleft()
        if cur == K:
            break
        target = cur
        while 0 < target <= 50000:
            if graph[2 * target] == -1:
                graph[2 * target] = graph[target]
                q.append(2 * target)
            target *= 2
            
        if 100000 >= cur - 1 >= 0:
            target = cur - 1
            if graph[target] == -1:
                graph[target] = graph[cur] + 1
                q.append(target)
                
        if cur + 1 <= 100000:
            target = cur + 1
            if graph[target] == -1:
                graph[target] = graph[cur] + 1
                q.append(target)

    return graph[K]

print(bfs(N))