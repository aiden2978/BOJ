N = int(input())
index = 1


while True:
    if N <= 3*index*(index-1)+1:
        break
    index += 1

print(index)