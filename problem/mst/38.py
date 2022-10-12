import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
graph = [[1e9] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    high, low = map(int, sys.stdin.readline().rstrip().split())
    graph[low][high] = 1

for i in range(1, n + 1):
    graph[i][i] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
            
result = 0
for i in range(1, n + 1):
    check = 0
    for j in range(1, n + 1):
        if graph[i][j] != 1e9 or graph[j][i] != 1e9:
            check += 1
    
    if check == n:
        result += 1

print(result)