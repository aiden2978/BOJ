import math

N, M = map(int, input().split( ))

basketList = []
for i in range(N):
    basketList.append(i+1)

for i in range(M):
    num1, num2 = map(int, input().split( ))
    k = math.floor((num2-num1)/2)
    for j in range(k+1):
        basketList[num1-1+j], basketList[num2-1-j] = basketList[num2-1-j], basketList[num1-1+j]

basketStr = ''
for i in basketList:
    basketStr += str(i) + ' '

print(basketStr)
