import sys

str = sys.stdin.readline().rstrip()

result = 0
check = 0
for i in str:
    if i == '1' and check == 0:
        result += 1
        check = 1
    elif check == 1 and i == '0':
        check = 0

print(result)