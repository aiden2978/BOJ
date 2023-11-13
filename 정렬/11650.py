N = int(input())

x, y = map(int, input().split( ))
X = [x]
Y = [y]

for i in range(1, N):
    x, y = map(int, input().split( ))
    X.append(x)
    Y.append(y)
    j = i
    while j >= 1:
        if X[j] < X[j-1]:
            X[j-1], X[j] = X[j], X[j-1]
            Y[j-1], Y[j] = Y[j], Y[j-1]
            j -= 1
        elif X[j] == X[j-1]:
            k = j
            while k >= 1 and Y[k] < Y[k-1]:
                X[k-1], X[k] = X[k], X[k-1]
                Y[k-1], Y[k] = Y[k], Y[k-1]
                k -= 1
            j -= 1
        else:
            break

for i in range(N):
    print(X[i], Y[i])