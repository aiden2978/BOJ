import sys
trees = [0]

def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while a%b != 0:
        a, b = b, a%b
    return b

N = int(sys.stdin.readline())
standard = int(sys.stdin.readline())

for _ in range(N-1):
    trees.append(int(sys.stdin.readline()) - standard)

interval = trees[1]

for i in range(N-2):
    interval = gcd(trees[i+2], interval)

print(int(trees[N-1]/interval) - N + 1)