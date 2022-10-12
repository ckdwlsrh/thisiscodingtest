import sys
n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
graph = [[1e9] * (n + 1) for _ in range(n + 1)]

for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(m):
    x, y, d = map(int, sys.stdin.readline().rstrip().split())
    if d < graph[x][y]: graph[x][y] = d


for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n + 1):
    s = ""
    for j in range(1, n + 1):
        if graph[i][j] == 1e9:
            s += str(0) + " "
        else:
            s += str(graph[i][j]) + " "
    
    print(s)