N, M = map(int, input().split( ))
chess = []

for i in range(N):
    chessLine = []
    chessStr = str(input())
    for j in range(M):
        chessLine.append(chessStr[j])
    chess.append(chessLine)

cntRes = 64

for x in range(N-7):
    for y in range(M-7):
        cnt = 0
        for i in range(x, x+8):
            for j in range(y, y+8):
                if (i%2 == j%2) and chess[i][j] == 'B':
                    cnt += 1
                elif (i%2 != j%2) and chess[i][j] == 'W':
                    cnt += 1
        if min(cnt, 64-cnt) < cntRes:
            cntRes = min(cnt, 64-cnt)

print(cntRes)