import sys
import heapq

INF = int(1e9)

n, m, c = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    x, y, z = map(int, sys.stdin.readline().rstrip().split())
    graph[x].append((y, z))
    
q = []
heapq.heappush(q,(0, c))
distance[c] = 0

while q:
    dist, now = heapq.heappop(q)
    
    if distance[now] < dist:
        continue
    
    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q,(cost, i[0]))

cnt = 0
s = 0
for i in range(1, n + 1):
    if distance[i] == INF or distance[i] == 0:
        continue
    else :
        cnt += 1
        s = max(distance[i],s)

print(cnt , s)