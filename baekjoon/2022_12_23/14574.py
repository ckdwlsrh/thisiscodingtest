import sys
from collections import deque

def floor(Pa, Pb, Ca, Cb):
    return int((Ca + Cb) / abs(Pa - Pb))

N = int(sys.stdin.readline().rstrip())
chef = [(0, 0)]
nodes = []

for i in range(1, N + 1):
    P, C = map(int, sys.stdin.readline().rstrip().split())
    chef.append((P, C))
    for j in range(1, i):
        nodes.append((floor(P, chef[j][0], C, chef[j][1]), i, j))

parent = [_ for _ in range(N + 1)]
degree = [0 for _ in range(N + 1)]
nodes_connected = [[] for _ in range(N + 1)]

def find(x, parent):
    if x != parent[x]:
        parent[x] = find(parent[x],parent)
    return parent[x]

def union(a, b, parent):
    a = find(a, parent)
    b = find(b, parent)
    if a == b:
        return False
    if a > b:
        parent[a] = b
    else:
        parent[b] = a
    return True

result = 0

nodes.sort(key = lambda k:k[0], reverse=True)
for dist, x, y in nodes:
    if union(x, y, parent):
        result += dist
        degree[x] += 1
        degree[y] += 1
        nodes_connected[x].append(y)
        nodes_connected[y].append(x)
        
print(result)

q = deque([])
for i in range(1, N + 1):
    if degree[i] == 1:
        degree[i] -= 1
        q.append(i)

check = [False for _ in range(N + 1)]
while q:
    next_cook = q.popleft()
    check[next_cook] = True
    for v in nodes_connected[next_cook]:
        if check[v]: continue
        print(v, next_cook)
        degree[v] -= 1
        if degree[v] == 1:
            q.append(v)
        