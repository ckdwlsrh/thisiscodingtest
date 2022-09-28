import sys

INF = int(1e9)

n, m = map(int, sys.stdin.readline().rstrip().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(1, n + 1):
    graph[_][_] = 0

for _ in range(m):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    graph[x][y] = 1
    graph[y][x] = 1
    
x, k = map(int, sys.stdin.readline().rstrip().split())

for s in range(1, n+1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][s] + graph[s][j])

if graph[1][k] == INF or graph[k][x] == INF:
    print("-1")
else :
    print(graph[1][k] + graph[k][x])