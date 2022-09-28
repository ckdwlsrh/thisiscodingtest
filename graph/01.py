import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
parent = [0] * (n+1)

for _ in range(1, n+1):
    parent[_] = _


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent,parent[x])
    return parent[x]

def union(parent, a, b):
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

for i in range(m):
    s, a, b = map(int, sys.stdin.readline().rstrip().split())
    
    a = find(parent, a)
    b = find(parent, b)
    
    if s == 0:
        union(parent, a, b)
    elif s == 1:
        if a == b:
            print("YES")
        else:
            print("NO")