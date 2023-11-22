import sys

a, b = map(int, sys.stdin.readline().split( ))

def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while a%b != 0:
        a, b = b, a%b
    return b

print(gcd(a, b))
print(int(a*b/gcd(a,b)))