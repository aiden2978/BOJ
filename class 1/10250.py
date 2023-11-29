import sys

T = int(sys.stdin.readline())

for _ in range(T):
    H, W, N = map(int, sys.stdin.readline().split( ))
    floor = N%H
    num = int((N-1)/H) + 1
    if floor == 0:
        print(100*H + num)
    else:
        print(100*floor + num)