import sys
people = []
rank = []

N = int(sys.stdin.readline())

for _ in range(N):
    people.append(list(map(int, sys.stdin.readline().split( ))))

for i in range(N):
    cnt = 1
    for j in range(N):
        if people[j][0] > people[i][0] and people[j][1] > people[i][1]:
            cnt += 1

    rank.append(cnt)

print(*rank)