import sys

s = sys.stdin.readline().rstrip()

result = int(s[0])

for i in s[1:]:
    if i != '0':
        if result == 0:
            result += 1
        result *= int(i)
    elif i == '1':
        result += int(i)
        
print(result)