import sys

def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while a%b != 0:
        a, b = b, a%b
    return b

a, b = map(int, input().split( ))
print(int(a*b/gcd(a, b)))