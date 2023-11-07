N, B = map(int, input().split( ))
numList = []
BList = [str(i) for i in range(10)]
for i in range(26):
    BList.append(chr(i+65))

div = N
while div >= 1:
    numList.append(BList[div%B])
    div = int(div/B)

print(*reversed(numList), sep = '')