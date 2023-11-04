N, M = map(int, input().split( ))
ballList = []

for i in range(N):
    ballList.append(i+1)

for i in range(M):
    num1, num2 = map(int, input().split( ))
    ballList[num1-1], ballList[num2-1] = ballList[num2-1], ballList[num1-1]

ballStr = ''
for i in ballList:
    ballStr += str(i) + ' '

print(ballStr)