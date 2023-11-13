N = int(input())
list666 = []

i = 0
while len(list666) <= N:
    if '666' in str(i):
        list666.append(i)
    i += 1

print(list666[N-1])