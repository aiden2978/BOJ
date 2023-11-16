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

# / 구간마다 소수의 개수를 구하면 시간이 오래걸림
# while True:
#     num = int(sys.stdin.readline())
#     if num == 0:
#         break
#     else:
#         cnt = 0
#         for i in range(num+1, 2*num+1):
#             if isPrime(i):
#                 cnt += 1
#         print(cnt)

# 에라토스테네스의 체 사용
sieve = [1]*(123456*2)
for i in range(123456*2):
    if isPrime(i+1) == False:
        sieve[i] = 0

while True:
    num = int(sys.stdin.readline())
    if num == 0:
        break
    else:
        print(sum(sieve[num:(2*num)]))