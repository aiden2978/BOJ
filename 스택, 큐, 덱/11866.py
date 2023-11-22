import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split( ))
per = deque([i for i in range(1, N+1)])
rest = []

for _ in range(N):
    per.rotate(-(K-1))
    dead = per.popleft()
    rest.append(dead)

restStr = str(rest[0])
for i in range(1, N):
    restStr = restStr + ', ' + str(rest[i])

print('<' + restStr + '>')