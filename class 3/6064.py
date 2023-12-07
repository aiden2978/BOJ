import sys

def calc(M, N, x, y):
    if x != M:
        for i in range(x % M, M * N + 1, M):
            if i % N == y % N:
                return(i)
    else:
        for i in range(M, M * N + 1, M):
            if i % N == y % N:
                return(i)
    return(-1)

T = int(sys.stdin.readline())

for _ in range(T):
    M, N, x, y = map(int, sys.stdin.readline().split( ))
    print(calc(M, N, x, y))