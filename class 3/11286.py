import sys
import heapq

N = int(sys.stdin.readline())

h = []

for _ in range(N):
    x = int(sys.stdin.readline())
    if x > 0:
        heapq.heappush(h, [x, 1])
    elif x < 0:
        heapq.heappush(h, [-x, -1])
    else:
        if not h:
            print(0)
        else:
            p = heapq.heappop(h)
            print(p[0] * p[1])