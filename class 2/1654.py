import sys

K, N = map(int, sys.stdin.readline().split( ))

lines = []
for _ in range(K):
    lines.append(int(sys.stdin.readline()))

def cnt_lines(list, value):
    cnt = 0
    for item in list:
        cnt += item//value
    return cnt

start = 0
end = max(lines) + 1

while start + 1 < end:
    mid = (start + end) // 2
    if cnt_lines(lines, mid) < N:
        end = mid
    else:
        start = mid

print(start)