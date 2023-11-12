N, M = map(int, input().split( ))
card = list(map(int, input().split( )))

blackjack = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            cardSum = card[i] + card[j] + card[k]
            if cardSum <= M:
                if cardSum > blackjack:
                    blackjack = cardSum

print(blackjack)