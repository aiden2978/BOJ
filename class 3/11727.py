import sys
N = int(sys.stdin.readline())

tiles = [0 for _ in range(1001)]
tiles[1] = 1
tiles[2] = 3

for i in range(3, N+1):
    tiles[i] = tiles[i-1] + 2*tiles[i-2]

print(tiles[N]%10007)