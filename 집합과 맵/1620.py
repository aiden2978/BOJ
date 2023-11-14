import sys

N, M = map(int, sys.stdin.readline().split( ))

picto = {}

for i in range(N):
    pokemon = sys.stdin.readline().strip()
    picto.update({pokemon:str(i+1)})
    picto.update({str(i+1):pokemon})

for _ in range(M):
    print(picto[str(sys.stdin.readline().strip())])