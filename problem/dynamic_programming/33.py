import sys

n = int(sys.stdin.readline().rstrip())
days = []
result = [0 for _ in range(n + 1)]

for i in range(n):
    day, money = map(int,sys.stdin.readline().rstrip().split())
    days.append([day,money])
for i in range(n):
    if i != 0:
        result[i] = max(result[i], result[i - 1])
    
    if i + days[i][0] > n:
        continue
    
    result[i + days[i][0]] = max(result[i + days[i][0]], days[i][1] + result[i])

print(max(result))