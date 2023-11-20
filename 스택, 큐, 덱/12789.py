import sys

N = int(sys.stdin.readline())
line = list(map(int, sys.stdin.readline().split( )))
space = []

min = 1
for _ in range(N):
    if line[0] != min or len(line) == 0:
        if len(space) != 0 and space[-1] == min:
            space.pop()
            min += 1
        else:
            back = line.pop(0)
            space.append(back)
    else:
        line.pop(0)
        min += 1

if min == N+1 or space == sorted(space, reverse=True):
    print('Nice')
else:
    print('Sad')