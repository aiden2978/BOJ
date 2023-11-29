import sys

L = int(sys.stdin.readline())
tohash = sys.stdin.readline().strip()
hashed = 0

for i in range(L):
    hashed += (ord(tohash[i])-96)*(31**i)

print(hashed%1234567891)