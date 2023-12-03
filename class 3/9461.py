import sys

p = [0 for _ in range(101)]
p[1] = 1
p[2] = 1
p[3] = 1
p[4] = 2
p[5] = 2

for i in range(6, 101):
    p[i] = p[i-1] + p[i-5]

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    print(p[N])