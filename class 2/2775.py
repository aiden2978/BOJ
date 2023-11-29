import sys
apt = [[0 for _ in range(15)] for _ in range(15)]
apt[0] = [i for i in range(15)]

for i in range(1, 15):
    for j in range(1, 15):
        apt[i][j] = sum(apt[i-1][1:j+1])


T = int(sys.stdin.readline())

for _ in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    
    print(apt[k][n])