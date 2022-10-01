import sys

str = sys.stdin.readline().rstrip()

result1 = 0
result2 = 0
check = 0
for i in str:
    if i == '1' and check == 0:
        result1 += 1
        check = 1
    elif check == 1 and i == '0':
        check = 0


for i in str:
    if i == '0' and check == 0:
        result2 += 1
        check = 1
    elif check == 1 and i == '1':
        check = 0

print(min(result1,result2))