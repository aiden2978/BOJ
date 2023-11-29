import sys

N, M = map(int, sys.stdin.readline().split( ))
dict = {}

for _ in range(N):
    site, pw = sys.stdin.readline().strip().split( )
    dict[site] = pw

for _ in range(M):
    site = sys.stdin.readline().strip()
    print(dict[site])