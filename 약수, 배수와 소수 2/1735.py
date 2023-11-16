import sys

def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while a%b != 0:
        a, b = b, a%b
    return b

n1, m1 = map(int, sys.stdin.readline().split( ))
n2, m2 = map(int, sys.stdin.readline().split( ))

nRes, mRes = n1*m2 + n2*m1, m1*m2

print(int(nRes / gcd(nRes, mRes)), int(mRes / gcd(nRes, mRes)))