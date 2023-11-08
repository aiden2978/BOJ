M = int(input())
N = int(input())
primeList = []

for i in range(M, N+1):
    if i != 1:
        isPrime = True
        for j in range(2, i):
                if i%j == 0:
                    isPrime = False
        if isPrime:
            primeList.append(i)

if primeList == []:
    print(-1)
else:
    print(sum(primeList))
    print(primeList[0])