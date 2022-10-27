import sys
import math
N = int(sys.stdin.readline().rstrip())

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent,parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a == b:
        return False
    
    if a > b:
        parent[a] = b
    else:
        parent[b] = a
    
    return True
    
edges = []
stars = []
parent = [_ for _ in range(N)]
for _ in range(N):
    x, y = map(float, sys.stdin.readline().rstrip().split())
    stars.append((x, y))
    for i in range(len(stars) - 1):
        x2, y2 = stars[i]
        d = math.sqrt(abs(x - x2) * abs(x - x2) + abs(y - y2) * abs(y - y2))
        edges.append((_, i, d))
    
edges.sort(key=lambda k:k[2])
result = 0

for edge in edges:
    a, b, d = edge
    if union(parent, a, b):
        result += d

print("{:.2f}".format(result))