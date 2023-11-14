import sys

def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while a%b != 0:
        a, b = b, a%b
    return b

N = int(sys.stdin.readline())

for _ in range(N):
    A, B = map(int, sys.stdin.readline().split( ))
    print(int(A*B/gcd(A, B)))