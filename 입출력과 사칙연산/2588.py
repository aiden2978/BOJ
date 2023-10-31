a = int(input())
b = int(input())

b0 = b%10
b1 = int((b/10))%10
b2 = int(b/100)

print(a*b0)
print(a*b1)
print(a*b2)
print(a*b)