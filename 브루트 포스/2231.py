N = int(input())

def divSum(x):
    nList = []
    for i in range(len(str(x))):
        nList.append(int(str(x)[i]))
    return x + sum(nList)

minCtor = N+1
for i in range(N+1):
    if divSum(i) == N and i < minCtor:
        minCtor = i

if minCtor == N+1:
    print(0)
else:
    print(minCtor)