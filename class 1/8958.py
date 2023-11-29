import sys

def score(string):
    total_score = 0
    score = 0
    for i in range(len(string)):
        if string[i] == 'O':
            score += 1
            total_score += score
        else:
            score = 0
    return total_score

N = int(sys.stdin.readline())

for _ in range(N):
    answer = sys.stdin.readline().strip()
    print(score(answer))