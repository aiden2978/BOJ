import sys
import math

def isPrime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num%i == 0:
            return False
    return True

N = int(sys.stdin.readline())
for _ in range(N):
    num = int(sys.stdin.readline())
    if num == 0 or num == 1:
        print(2)
    else:
        while isPrime(num) == False:
            num += 1
        print(num)