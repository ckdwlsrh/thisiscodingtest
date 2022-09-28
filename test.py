import time
from collections import deque
import heapq
import sys
#무한대
INF = int(1e9)
start_time = time.time()

n, m = map(int, input().split())

start = int(input())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else :
        print(distance[i])


end_time = time.time()
print("time : ", end_time - start_time)


#입력 빠른 속도 strip -> 앞뒤 공백 제거 rstrip -> 뒤 공백 제거
data = sys.stdin.readline().rstrip()