import sys
import math

N = int(sys.stdin.readline())
k = int(math.log2(int(N / 3)))

res = [['  *  ', ' * * ', '*****']]

for i in range(1, k+1):
    newtri = []
    emptystr = ' ' * (3*(2**(i-1)))
    for j in range(3*(2**(i-1))):
        newtri.append(''.join([emptystr, res[i-1][j], emptystr]))
    for j in range(3*(2**(i-1))):
        newtri.append(''.join([res[i-1][j], ' ', res[i-1][j]]))
    res.append(newtri)

for i in range(N):
    sys.stdout.write(res[k][i])
    sys.stdout.write('\n')