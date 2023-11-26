import sys
s = set()

N = int(sys.stdin.readline())
for _ in range(N):
    proc = sys.stdin.readline().strip()
    if proc[:3] == 'add':
        s.add(int(proc[4:]))
    elif proc[:6] == 'remove':
        s.discard(int(proc[7:]))
    elif proc[:5] == 'check':
        num = int(proc[6:])
        if num in s:
            print(1)
        else:
            print(0)
    elif proc[:6] == 'toggle':
        num = int(proc[7:])
        if num in s:
            s.remove(num)
        else:
            s.add(num)
    elif proc == 'all':
        s = {i for i in range(1, 21)}
    elif proc == 'empty':
        s = set()