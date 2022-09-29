import sys

n = int(sys.stdin.readline().rstrip())

str = []

for i in range(n):
    str.append(list(sys.stdin.readline().rstrip()))
    
for i in range(n):
    
    cnt = 0
    
    for j in str[i]:
        if j == '(':
            cnt += 1
        else :
            cnt -= 1
            if cnt < 0 :
                break
    
    if cnt == 0:
        print('YES')
    else:
        print('NO')