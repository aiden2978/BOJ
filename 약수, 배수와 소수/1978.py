N = int(input())
numList = list(map(int, input().split( )))
count = 0

for i in range(N):
    isPrime = True
    if numList[i] >= 2:
        for j in range(2, numList[i]):
            if numList[i]%j == 0:
                isPrime = False
        if isPrime:
            count += 1

print(count)