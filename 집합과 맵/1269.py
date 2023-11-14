import sys
import collections

N, M = map(int, sys.stdin.readline().split( ))
A = list(map(int, sys.stdin.readline().split( )))
B = list(map(int, sys.stdin.readline().split( )))

print(N+M-2*(len(collections.Counter(A) & collections.Counter(B))))