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
    
sieve = [1]*(1000000+1)
for i in range(1, 1000000+1):
    if isPrime(i) == False:
        sieve[i] = 0
    
N = int(sys.stdin.readline())

for _ in range(N):
    n = int(sys.stdin.readline())
    if n == 4:
        print(1)
    else:
        cnt = 0
        for i in range(3, int(n/2)+1, 2):
            if sieve[i] and sieve[n-i]:
                cnt += 1
    print(cnt)