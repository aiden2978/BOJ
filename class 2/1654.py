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

start = 1
end = max(lines)//N

while True:
    mid = (start + end)//2
    if cnt_lines(lines, mid) > N:
        start = mid + 1
    elif cnt_lines(lines, mid) < N:
        end = mid - 1
    else:
        if cnt_lines(lines, mid) == N:
            start = mid + 1
        else:
            break

print(mid)

