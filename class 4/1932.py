import sys

N = int(sys.stdin.readline())
tri = []
for _ in range(N):
    lines = list(map(int, sys.stdin.readline().split( )))
    tri.append(lines)

if N == 1:
    print(tri[0][0])
else:
    for i in range(1, N):
        for j in range(i+1):
            if j == 0:
                tri[i][j] += tri[i-1][j] 
            elif j == i:
                tri[i][j] += tri[i-1][j-1]
            else:
                tri[i][j] += max(tri[i-1][j-1], tri[i-1][j])

    print(max(tri[N-1]))