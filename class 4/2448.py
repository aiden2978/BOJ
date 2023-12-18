import sys
import math

N = int(sys.stdin.readline())

def tri(n):
    if n == 0:
        return ([['  *  '], [' * * '], ['*****']])
    else:
        newtri = []
        nostar = empty(n-1)
        star = tri(n-1)
        for i in range(3 * (2 ** (n-1))):
            newtri.append(nostar[i] + star[i] + nostar[i])
        for i in range(3 * (2 ** (n-1))):
            newtri.append(star[i] + [' '] + star[i])
        return newtri

    
def empty(n):
    return [[' ' for _ in range(3 * (2 ** (n)))] for _ in range(3 * (2 ** (n)))]

k = int(math.log2(int(N / 3)))

for i in range(N):
    print(*tri(k)[i], sep = '')