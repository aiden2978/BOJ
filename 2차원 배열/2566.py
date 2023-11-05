maxRow = 0
maxCol = 0
maxList = []
maxIndex = []

for i in range(9):
    gridList = list(map(int, input().split( )))
    maxList.append(max(gridList))
    maxIndex.append(gridList.index(max(gridList)))

resNum = max(maxList)
maxRow = maxList.index(max(maxList)) + 1
maxCol = maxIndex[maxRow-1] + 1

print(resNum)
print(maxRow, maxCol)