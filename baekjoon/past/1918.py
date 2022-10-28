import sys

exp = sys.stdin.readline().rstrip()

gwalho = []
stack = []
result = ""

for char in exp:
    if char == '(':
        gwalho.append(stack)
        stack = []
        pass
    elif char == '*' or char == '/':
        if stack:
            if stack[-1] == '/' or stack[-1] == '*':
                result += stack.pop()
        stack.append(char)
    elif char == '+' or char == '-':
        while stack:
            if stack[-1] == '+' or stack[-1] == '-':
                result += stack.pop()
                break
            result += stack.pop()
        stack.append(char)
    elif char ==')':
        while stack:
            result += stack.pop()
        stack = gwalho.pop()
    else:
        result += char

while stack:
    result += stack.pop()
    
print(result)