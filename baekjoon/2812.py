import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

num = sys.stdin.readline().rstrip()
result = ""

while True:
    if k == 0:
        break
    max = '0'
    max_index = 0
    for i in range(k + 1):
        if num[i] == '9':
            max_index = i
            break
        if max < num[i]:
            max = num[i]
            max_index = i
    
    a = max_index
    result += num[a]
    k -= a
    num = num[a + 1:n]
    n -= a + 1
    if k == n:
        break
if k == 0:
    result += num
print(int(result))