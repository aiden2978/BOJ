N = int(input())
cards = set(map(int, input().split( )))
M = int(input())
checks = list(map(int, input().split( )))

checklist = []
for i in range(M):
    if checks[i] in cards:
        checklist.append(1)
    else:
        checklist.append(0)

print(*checklist)