import sys

A, B, C = map(int, sys.stdin.readline().split( ))

def power(A, B, C):
    if B == 1:
        return A % C
    elif B % 2 == 0:
        return (power(A, int(B / 2), C) ** 2) % C
    elif B % 2 == 1:
        return (A * power(A, int((B - 1) / 2), C) ** 2) % C
    
print(power(A, B, C))