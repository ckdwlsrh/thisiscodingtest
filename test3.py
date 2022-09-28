import sys

def find_parents(parent, x):
    if parent[x] != x:
        parent[x] = find_parents(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    if a > b:
        parent[a] = b
    else :
        parent[b] = a

n, m = map(int, sys.stdin.readline().rstrip().split())

parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i

edges = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(m)]


edges.sort(key=lambda k:k[2])

result = 0

for i in range(m):
    a, b, d = edges[i]
    a = find_parents(parent, a)
    b = find_parents(parent, b)
    if a != b:
        union(parent,a,b)
        result += d

print(result)