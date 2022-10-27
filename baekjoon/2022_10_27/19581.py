import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    u, v, w = map(int, sys.stdin.readline().rstrip().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

def max_index(dist):
    m = 0
    for i in range(1, N + 1):
        if dist[i] > m:
            m = dist[i]
            m_index = i
    return m_index
    
def bfs(start):
    q = deque([(start, 0)])
    dist = [-1 for _ in range(N + 1)]
    #left max
    while q:
        now, cost = q.popleft()
        dist[now] = cost
        for i in graph[now]:
            v, w = i
            if dist[v] != -1:
                continue
            q.append((v, cost + w))
    
    return dist

dist = bfs(1)
# 젤먼 a 구하기
a = max_index(dist)
# b 구하기
dist = bfs(a)
b = max_index(dist)

# a에서 거리중 2번째
dist.sort(reverse=True)
result1 = dist[1]

# b에서 거리중 2번째
dist = bfs(b)
dist.sort(reverse=True)
result2 = dist[1]

print(max(result1, result2))