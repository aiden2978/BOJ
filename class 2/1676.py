import sys

num = int(sys.stdin.readline())
cnt = 0
times = 1

while num >= 5**times:
    cnt += (num//(5**times))
    times += 1

print(cnt)