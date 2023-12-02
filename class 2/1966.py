import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split( ))
    imp = list(map(int, sys.stdin.readline().split( )))
    idx = [i for i in range(N)]
    q = deque()
    for i, j in zip(imp, idx):
        q.append([i, j])
    printed = []
    
    while q:
        doc = q.popleft()
        printed.append(doc)
        for items in q:
            if items[0] > doc[0]:
                q.append(doc)
                printed.pop()
                break

    for i in range(N):
        if printed[i][1] == M:
            print(i+1)