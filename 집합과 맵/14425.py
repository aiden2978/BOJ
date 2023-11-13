N, M = map(int, input().split( ))
strings = set([])
checks = []

for _ in range(N):
    strings.add(input())
for _ in range(M):
    checks.append(input())

count = 0
for i in range(M):
    if checks[i] in strings:
        count += 1

print(count)