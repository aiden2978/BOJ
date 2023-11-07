N = int(input())
for i in range(N):
    cost = int(input())
    coinList = [int(cost/25), int((cost%25)/10), int(((cost%25)%10)/5), int(cost%5)]
    print(*coinList)