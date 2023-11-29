import sys
from collections import Counter

num = 1
for _ in range(3):
    num *= int(sys.stdin.readline())

num_c = Counter(str(num))

for i in range(10):
    print(num_c[f'{i}'])