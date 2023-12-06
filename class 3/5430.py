import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    proc = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    arr = sys.stdin.readline().strip()
    if n == 0:
        if 'D' in proc:
            print('error')
        else:
            print('[]')

    else:
        li_str = arr[1:-1]
        q = deque(list(map(int, li_str.split(','))))
        isRev = False
        isError = False
    
        for i in range(len(proc)):
            if proc[i] == 'R':
                if isRev:
                    isRev = False
                else:
                    isRev = True
            elif proc[i] == 'D':
                if not q:
                    isError = True
                    break
                else:
                    if isRev:
                        q.pop()
                    else:
                        q.popleft()

        if isError:
            print('error')
        else:
            if not isRev:
                a = list(q)
                print(str(a).replace(' ', ''))
            else:
                a = list(reversed(list(q)))
                print(str(a).replace(' ', ''))