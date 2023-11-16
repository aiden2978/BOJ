import sys
import math

def isPrime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num%i == 0:
            return False
    return True

M, N = map(int, sys.stdin.readline().split( ))

for i in range(max(2, M), N+1):
    if isPrime(i):
        print(i)