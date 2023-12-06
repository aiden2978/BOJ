import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
err_buttons = list(map(int, sys.stdin.readline().split( )))
able_num = [i for i in range(1000001)]

min_move = abs(N - 100)

def isAble(num):
    for btn in err_buttons:
        if str(btn) in str(num):
            return False
    return True

for i in range(1000001):
    if isAble(i):
        move = abs(i - N) + len(str(i))
        if move < min_move:
            min_move = move

print(min_move)