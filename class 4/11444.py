import sys

def mtx_mul(mtx1, mtx2):
    return [[(mtx1[0][0] * mtx2[0][0] + mtx1[0][1] * mtx2[1][0]) % 1000000007, (mtx1[0][0] * mtx2[0][1] + mtx1[0][1] * mtx2[1][1]) % 1000000007], [(mtx1[1][0] * mtx2[0][0] + mtx1[1][1] * mtx2[1][0]) % 1000000007, (mtx1[1][0] * mtx2[0][1] + mtx1[1][1] * mtx2[1][1]) % 1000000007]]

def fib_power(n):
    uni = [[1, 1], [1, 0]]
    if n == 1:
        return uni
    else:
        mtx_half = fib_power(n // 2)
        mtx = mtx_mul(mtx_half, mtx_half)
        if n % 2 == 0:
            return mtx
        else:
            return mtx_mul(uni, mtx)

N = int(sys.stdin.readline())

print(fib_power(N)[1][0])