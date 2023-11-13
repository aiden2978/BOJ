N = int(input())
work = set()

for _ in range(N):
    name, boo = map(str, input().split( ))
    if boo == 'enter':
        work.add(name)
    elif boo == 'leave':
        work.discard(name)

worklist = list(work)
worklist.sort(reverse=True)
for man in worklist:
    print(man)