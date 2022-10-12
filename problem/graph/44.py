import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())


parent = [_ for _ in range(n + 1)]

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent,parent[x])
    return parent[x]

def union(parent, x, y):
    
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

graph = []
edges = []

for i in range(1, n + 1):
    x, y, z = map(int, sys.stdin.readline().rstrip().split())
    graph.append((x,y,z, i))
    
for i in range(3):
    graph = sorted(graph,key = lambda k:k[i])
    
    for j in range(1, n):
        edges.append((abs(graph[j-1][i] - graph[j][i]), graph[j-1][3], graph[j][3]))

edges.sort(key = lambda k: k[0])
edges = deque(edges)

result = 0
while edges:
    dist, x, y = edges.popleft()
    x = find(parent, x)
    y = find(parent, y)
    if x == y:
        continue
    union(parent,x,y)
    result += dist

print(result)