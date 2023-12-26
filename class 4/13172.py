import sys

def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while True:
        if a % b == 0:
            return b
        else:
            a, b = b, a%b

def power(A, B, C):
    if B == 1:
        return A % C
    elif B % 2 == 0:
        return (power(A, int(B / 2), C) ** 2) % C
    elif B % 2 == 1:
        return (A * power(A, int((B - 1) / 2), C) ** 2) % C

M = int(sys.stdin.readline())
sum = 0

for _ in range(M):
    N, S = map(int, sys.stdin.readline().split( ))
    sum += S * power(N, 1000000005, 1000000007) % 1000000007
    
print(sum % 1000000007)