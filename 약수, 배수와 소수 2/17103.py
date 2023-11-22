import sys
import math

def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(num))+1):
            if num%i == 0:
                return False
        return True
    
sieve = [1]*(1000000)
sieve[0] = 0
for i in range(1, 1001):
    if isPrime(i) == True:
        for j in range(2*i-1, 1000000, i):
            sieve[j] = 0

N = int(sys.stdin.readline())

for _ in range(N):
    m = int(sys.stdin.readline())
    if m == 4:
        print(1)
    else:
        cnt = 0
        for i in range(3, int(m/2)+1, 2):
            if sieve[i-1] and sieve[m-i-1]:
                cnt += 1
        print(cnt)