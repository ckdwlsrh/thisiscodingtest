import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

parent = [0] * (n + 1)
for i in range(1,n + 1):
    parent[i] = i

edges = []

for i in range(m):
    a, b, cost = map(int, sys.stdin.readline().rstrip().split())
    edges.append((cost, a, b))

edges.sort()

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent,parent[x])
    return parent[x]


def union(parent, a, b):
    if a > b:
        parent[a] = b
    else:
        parent[b] = a
        
result = 0
max_distance = 0

for i in range(m):
    cost, a, b = edges[i]
    
    a = find(parent, a)
    b = find(parent, b)
    
    if a != b:
        union(parent, a, b)
        max_distance = max(max_distance, cost)
        result += cost

print(result - max_distance)
