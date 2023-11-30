import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    k = int(sys.stdin.readline())
    q = deque()

    proc, num = sys.stdin.readline().strip().split( )
    num = int(num)

    if proc == 'I':
        q.append(num)