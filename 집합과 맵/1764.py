import sys
import collections

N, M = map(int, input().split( ))
people1 = []
people2 = []

for _ in range(N):
    people1.append(sys.stdin.readline().strip('\n'))

for _ in range(M):
    people2.append(sys.stdin.readline().strip('\n'))

common = collections.Counter(people1) & collections.Counter(people2)

print(len(common))
for name in sorted(common):
    print(name)