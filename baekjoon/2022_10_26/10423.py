import sys

N, M, K = map(int, sys.stdin.readline().rstrip().split())

tmp = list(map(int, sys.stdin.readline().rstrip().split()))
plants = [0 for _ in range(N + 1)]
for _ in tmp:
    plants[_] = 1

parent = [_ for _ in range(N + 1)]
edges = []
values = []

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent,parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a == b or (plants[a] == 1 and plants[b] == 1):
        return False
    
    if plants[b] == 1:
        parent[a] = b
    else:
        parent[b] = a
    return True

for _ in range(M):
    u, v, w = map(int, sys.stdin.readline().rstrip().split())
    edges.append((w, u, v))

result = 0
edges.sort(key = lambda k:k[0])
for edge in edges:
    w, x, y = edge
    if union(parent, x, y):
        result += w
        values.append((x, y, w))

print(result)