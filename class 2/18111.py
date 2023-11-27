import sys
N, M, B = map(int, sys.stdin.readline().split( ))

ground = []
for _ in range(N):
    ground += list(map(int, sys.stdin.readline().split( )))

min_time = 256*2*500*500
height = 0

for i in range(min(ground), max(ground)+1):
    time = 0
    blocks = 0

    for J in range(N*M):
        if ground[J] > i:
            time += 2*(ground[J] - i)
            blocks -= (ground[J] - i)
        else:
            time += (i - ground[J])
            blocks += (i - ground[J])
    
    if blocks <= B and time <= min_time:
        min_time = time
        if i > height:
            height = i

print(min_time, height)