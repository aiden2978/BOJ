need = [1, 1, 2, 2, 2, 8]
chess = list(map(int, input().split( )))
res = [0]*6

for i in range(6):
    res[i] = need[i] - chess[i]

chessStr = ''
for i in res:
    chessStr += str(i) + ' '

print(chessStr)