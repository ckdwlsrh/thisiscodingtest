import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
balls = list(map(int, sys.stdin.readline().rstrip().split()))
weight = [0] * (m + 1)

for i in balls:
    weight[i] += 1

result = 0

for i in range(1,m + 1):
    for j in range(i + 1,m + 1):
        result += (weight[i] * weight[j])
        
print(result)