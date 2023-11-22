import sys
from collections import deque

N = int(sys.stdin.readline())
balloons = list(map(int, sys.stdin.readline().split( )))
order = [i for i in range(1, N+1)]
balloons_data = deque([[b, o] for b, o in zip(balloons, order)])
burst = []

for _ in range(N):
    a = balloons_data.popleft()
    burst.append(a[1])
    if a[0] > 0:
        balloons_data.rotate(-a[0]+1)
    else:
        balloons_data.rotate(-a[0])

print(*burst)