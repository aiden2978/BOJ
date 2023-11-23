import sys

N, r, c = map(int, sys.stdin.readline().split( ))
order = 0

for i in range(N-1, -1, -1):
    if c > 2**i - 1:
        if r > 2**i - 1:
            order += 3*2**(2*i)
            r -= 2**i
            c -= 2**i
        else:
            order += 2**(2*i)
            c -= 2**i
    else:
        if r > 2**i - 1:
            order += 2*2**(2*i)
            r -= 2**i

print(order)