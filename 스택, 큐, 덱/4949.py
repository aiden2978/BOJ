import sys

def balanced(string):
    stack = []
    for i in range(len(string)):
        if string[i] == '(':
            stack.append(1)
        elif string[i] == '[':
            stack.append(-1)
        elif string[i] == ')':
            if len(stack) == 0 or stack[-1] == -1:
                return("no")
            else:
                stack.pop()
        elif string[i] == ']':
            if len(stack) == 0 or stack[-1] == 1:
                return("no")
            else:
                stack.pop()

    if len(stack) != 0 :
        return("no")
    else:
        return("yes")
    
while True:
    line = sys.stdin.readline()
    index = line.find('.')
    line = line[:index]
    if line == "":
        break
    else:
        print(balanced(line))