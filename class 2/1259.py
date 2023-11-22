import sys

while True:
    input = sys.stdin.readline().strip()
    if input == '0':
        break
    else:
        result = 'yes'
        for i in range(int(len(input)/2)+1):
            if input[i] != input[len(input)-i-1]:
                result = 'no'
        print(result)