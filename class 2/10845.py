import sys
from collections import deque

N = int(sys.stdin.readline())

queue = deque([])
cnt = 0
for _ in range(N):
    proc = sys.stdin.readline().strip()
    if proc[:4] == 'push':
        queue.append(int(list(proc.split( ))[1]))
    elif proc == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            qpop = queue.popleft()
            print(qpop)
    elif proc == 'size':
        print(len(queue))
    elif proc == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif proc == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    else:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])