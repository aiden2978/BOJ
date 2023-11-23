import sys

N, K = map(int, sys.stdin.readline().split( ))
bin = 1

for i in range(K):
    bin *= (N-i)
    bin /=(i+1)

print(int(bin))