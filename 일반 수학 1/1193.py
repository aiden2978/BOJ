# (1 + ... + i-1) < X <= (1 + ... + i)
# 분모 + 분자 = i+1
# i가 짝수일 떄
# 분자 = X - (1 + ... + i-1)
# 분모 = i+1 - 분자

X = int(input())
i = 1

while True:
    if X <= int(i*(i+1)/2):
        if i%2 == 0:
            print(X-int(i*(i-1)/2), '/', i+1+int(i*(i-1)/2)-X, sep = '')
        else:
            print(i+1+int(i*(i-1)/2)-X, '/', X-int(i*(i-1)/2), sep = '')
        break
    i += 1