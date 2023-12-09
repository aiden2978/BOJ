import sys
from collections import deque

A, B = map(int, sys.stdin.readline().split( ))

num = B
cnt = 1
while True:
    if num < A:
        print(-1)
        break
    elif num == A:
        print(cnt)
        break
    elif num % 2 == 0:
        num = int(num / 2)
        cnt += 1
    elif num % 10 == 1:
        num = int((num - 1) / 10)
        cnt += 1
    else:
        if num != A:
            print(-1)
            break