N = int(input())
score = list(map(int, input().split( )))

M = max(score)
highscore = []
for i in score:
    highscore.append(i/M*100)

sum = 0
for i in highscore:
    sum += i

print(sum/N)