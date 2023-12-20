import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    stickers = []
    for _ in range(2):
        stickers.append(list(map(int, sys.stdin.readline().split( ))))

    # x o o | x x o | ...
    # o o o | x o o | ...
        
    # o o o | x o o | ...
    # x o o | x x o | ...
    dp = [[0 for _ in range(N)] for _ in range(2)]

    if N == 1:
        print(max(stickers[0][0], stickers[1][0]))
    else:
        dp[0][1] = stickers[0][0]
        dp[1][1] = stickers[1][0]

        for i in range(2, N):
            dp[0][i] = max(dp[1][i-1] + stickers[0][i-1], dp[1][i-2] + stickers[0][i-1])
            dp[1][i] = max(dp[0][i-1] + stickers[1][i-1], dp[0][i-2] + stickers[1][i-1])

        print(max(dp[0][N-2] + stickers[1][N-1], dp[0][N-1] + stickers[1][N-1], dp[1][N-2] + stickers[0][N-1], dp[1][N-1] + stickers[0][N-1]))