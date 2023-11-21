import sys
from collections import deque

N = int(sys.stdin.readline())
int_deque = deque([])

for _ in range(N):
    proc = sys.stdin.readline()

    if proc[0] == '1':
        int_deque.appendleft(int(proc[2:]))
    elif proc[0] == '2':
        int_deque.append(int(proc[2:]))
    elif int(proc) == 3:
        if len(int_deque) == 0:
            print(-1)
        else:
            proc3 = int_deque.popleft()
            print(proc3)
    elif int(proc) == 4:
        if len(int_deque) == 0:
            print(-1)
        else:
            proc4 = int_deque.pop()
            print(proc4)
    elif int(proc) == 5:
        print(len(int_deque))
    elif int(proc) == 6:
        if len(int_deque) == 0:
            print(1)
        else:
            print(0)
    elif int(proc) == 7:
        if len(int_deque) == 0:
            print(-1)
        else:
            print(int_deque[0])
    elif int(proc) == 8:
        if len(int_deque) == 0:
            print(-1)
        else:
            print(int_deque[-1])