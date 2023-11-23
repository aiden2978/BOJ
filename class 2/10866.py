import sys
from collections import deque

N = int(sys.stdin.readline())
int_deque = deque([])

for _ in range(N):
    proc = sys.stdin.readline().strip()

    if proc[:10] == 'push_front':
        int_deque.appendleft(int(proc[11:]))
    elif proc[:9] == 'push_back':
        int_deque.append(int(proc[10:]))
    elif proc[:9] == 'pop_front':
        if len(int_deque) == 0:
            print(-1)
        else:
            proc3 = int_deque.popleft()
            print(proc3)
    elif proc[:8] == 'pop_back':
        if len(int_deque) == 0:
            print(-1)
        else:
            proc4 = int_deque.pop()
            print(proc4)
    elif proc == 'size':
        print(len(int_deque))
    elif proc == 'empty':
        if len(int_deque) == 0:
            print(1)
        else:
            print(0)
    elif proc == 'front':
        if len(int_deque) == 0:
            print(-1)
        else:
            print(int_deque[0])
    elif proc == 'back':
        if len(int_deque) == 0:
            print(-1)
        else:
            print(int_deque[-1])