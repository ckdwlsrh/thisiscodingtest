import sys

s = sys.stdin.readline().rstrip()

# 0 -> 1
result = 0
check = False
for i in range(len(s)):
    if s[i] == '1' and not check:
        result += 1
        check = True
    if s[i] == '0' and check :
        check = False

# 1 -> 0
result2 = 0
check = False
for i in range(len(s)):
    if s[i] == '0' and not check:
        result2 += 1
        check = True
    if s[i] == '1' and check :
        check = False
    
print(min(result,result2))