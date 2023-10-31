import sys
T = int(input())
data = []
for i in range(T):
    data.append(list(map(int, sys.stdin.readline().strip().split( ))))
    print(data[i][0] + data[i][1])