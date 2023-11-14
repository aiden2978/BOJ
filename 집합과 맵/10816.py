import sys

N = int(sys.stdin.readline())
card1 = list(map(int, sys.stdin.readline().split( )))
M = int(sys.stdin.readline())
card2 = list(map(int, sys.stdin.readline().split( )))

card1_cnt = {}
for num in card1:
    card1_cnt[num] = card1_cnt.get(num, 0) + 1

for num in card2:
    print(card1_cnt.get(num, 0), end = ' ')