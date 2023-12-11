import sys

N = int(sys.stdin.readline())

maxlines = list(map(int, sys.stdin.readline().split( )))
minlines = maxlines.copy()

for _ in range(N-1):
    lines = list(map(int, sys.stdin.readline().split( )))
    max_0 = max(maxlines[0], maxlines[1]) + lines[0]
    min_0 = min(minlines[0], minlines[1]) + lines[0]
    max_1 = max(maxlines[0], maxlines[1], maxlines[2]) + lines[1]
    min_1 = min(minlines[0], minlines[1], minlines[2]) + lines[1]
    max_2 = max(maxlines[1], maxlines[2]) + lines[2]
    min_2 = min(minlines[1], minlines[2]) + lines[2]
    maxlines = [max_0, max_1, max_2]
    minlines = [min_0, min_1, min_2]

print(max(maxlines), min(minlines))
            