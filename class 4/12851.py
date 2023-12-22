import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split( ))

graph = [0 for _ in range(100001)]
cnt = [0 for _ in range(100001)]

def bfs(idx):
    q = deque([idx])
    while q:
        cur = q.popleft()
        # 한바퀴 더 돌기 위해 100001을 append한 후 100001이 나오면 break
        if cur == K:
            q.append(100001)
        if cur == 100001:
            break
        if cur + 1 <= 100000:
            target = cur + 1
            if not graph[target]:
                graph[target] = graph[cur] + 1
                cnt[target] = 1  
                q.append(target)   
            elif graph[target] == graph[cur] + 1:
                cnt[target] += 1
                q.append(target) 
                
        if cur - 1 >= 0:
            target = cur - 1
            if not graph[target]:
                graph[target] = graph[cur] + 1
                cnt[target] = 1  
                q.append(target)   
            elif graph[target] == graph[cur] + 1:
                cnt[target] += 1
                q.append(target) 

        if 2*cur <= 100000:
            target = 2 * cur
            if not graph[target]:
                graph[target] = graph[cur] + 1
                cnt[target] = 1     
                q.append(target)
            elif graph[target] == graph[cur] + 1:
                cnt[target] += 1
                q.append(target) 

if N == K:
    print(0, 1)
else:
    bfs(N)
    print(graph[K], cnt[K])