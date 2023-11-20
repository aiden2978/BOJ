import sys
from collections import deque

N = int(sys.stdin.readline())
cards = deque([(i+1) for i in range(N)])

while len(cards) > 1:
    cards.popleft()
    cardDown = cards.popleft()
    cards.append(cardDown)

print(*cards)