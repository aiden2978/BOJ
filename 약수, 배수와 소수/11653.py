N = int(input())
num = N
primeList = []
i = 2

while num > 1:
    if num%i == 0:
        primeList.append(i)
        num = int(num/i)
    else:
        i += 1

if N == 1:
    print('')
else:
    for prime in primeList:
        print(prime)