import sys

N, B = map(int, sys.stdin.readline().split( ))
mtx = []
for _ in range(N):
    lines = list(map(int, sys.stdin.readline().split( )))
    for i in range(N):
        lines[i] = lines[i] % 1000
    mtx.append(lines)

def mul(mtx1, mtx2):
    res = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            sum = 0
            for k in range(N):
                sum += (mtx1[i][k] * mtx2[k][j])
            res[i][j] = sum % 1000
    return res

def power(mtx, B):
    if B == 1:
        return mtx
    a = power(mtx, B // 2)
    res = mul(a, a)
    if B % 2 == 1:
        res = mul(mtx, res)
    return res
    
resmtx = power(mtx, B)
for i in range(N):
    print(*resmtx[i])