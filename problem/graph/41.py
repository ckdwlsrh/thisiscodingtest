import sys

def find(parent,x):
    if parent[x] != x:
        parent[x] = find(parent,parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


n, m = map(int, sys.stdin.readline().rstrip().split())

graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
parent = [_ for _ in range(n + 1)]

for i in range(n):
    for j in range(i, n):
        if graph[i][j] == 1:
            union(parent, i + 1,j + 1)

result = list(map(int, sys.stdin.readline().rstrip().split()))
root = parent[result[0]]

for i in result[1:]:
    if parent[i] != root:
        print("NO")
        exit(0)

print("YES")