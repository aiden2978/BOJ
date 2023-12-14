import sys

dx = [1, -1, 0, 0]
dy = [0, 0 ,1, -1]

def dfs(x, y):
    global visited_chr, max_cnt, cnt
    visited_chr[ord(board[y][x]) - 65] = 1
    cnt += 1
    if cnt > max_cnt:
        max_cnt = cnt
    for i in range(4):
        newx = x + dx[i]
        newy = y + dy[i]
        if 0 <= newx < C and 0 <= newy < R:
            if not visited_chr[ord(board[newy][newx]) - 65]:
                dfs(newx, newy)
                visited_chr[ord(board[newy][newx]) - 65] = 0
                cnt -= 1
    return max_cnt

R, C = map(int, sys.stdin.readline().split( ))

board = [sys.stdin.readline().strip() for _ in range(R)]
visited_chr = [0 for _ in range(26)]
max_cnt = 0
cnt = 0

print(dfs(0, 0))