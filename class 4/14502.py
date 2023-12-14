import sys
import copy
from collections import deque
from itertools import combinations

def dfs(y, x):
    global walled
    q = deque([[y, x]])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while q:
        [cury, curx] = q.popleft()
        for i in range(4):
            if 0 <= cury + dy[i] < N and 0 <= curx + dx[i] < M:
                if walled[cury + dy[i]][curx + dx[i]] == 0:
                    walled[cury + dy[i]][curx + dx[i]] = 2
                    q.append([cury + dy[i], curx + dx[i]])


N, M = map(int, sys.stdin.readline().split( ))

graph = []
empty = []
viruses = []

for i in range(N):
    lines = list(map(int, sys.stdin.readline().split( )))
    graph.append(lines)
    for j in range(M):
        if lines[j] == 0:
            empty.append([i, j])
        if lines[j] == 2:
            viruses.append([i, j])

combs = list(combinations(empty, 3))
safe = 0

for comb in combs:
    cnt = 0
    walled = copy.deepcopy(graph)
    for idx in range(3):
        walled[comb[idx][0]][comb[idx][1]] = 1
    for virus in viruses:
        dfs(virus[0], virus[1])
    
    for i in range(N):
        for j in range(M):
            if walled[i][j] == 0:
                cnt += 1
    if cnt > safe:
        safe = cnt

print(safe)