N, M = map(int, input().split( ))
basketList = [0]*N

for i in range(M):
    ballList = list(map(int, input().split( )))
    for j in range(ballList[0], ballList[1]+1):
        basketList[j-1] = ballList[2]

basketStr = ''
for i in basketList:
    basketStr += str(i) + ' '

print(basketStr)