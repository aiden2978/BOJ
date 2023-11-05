N, M = map(int, input().split( ))
a = []
b = []

for i in range(N):
    sublist = list(map(int, input().split( )))
    a.append(sublist)

for i in range(N):
    sublist = list(map(int, input().split( )))
    b.append(sublist)

for i in range(N):
    sublist = []
    for j in range(M):
        sublist.append(a[i][j] + b[i][j])
    print(*sublist)