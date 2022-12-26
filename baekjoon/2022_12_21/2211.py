import sys
import heapq

n, m = map(int,sys.stdin.readline().rstrip().split())

graph = [[] for _ in range(n + 1)]
result = {}

for i in range(m):
    x, y, c = map(int, sys.stdin.readline().rstrip().split())
    graph[x].append([y, c])
    graph[y].append([x, c])

def dijkstra(graph, start):
    dist = [1e9 for _ in range(n + 1)]
    dist[start] = 0
    queue = []
    heapq.heappush(queue,[dist[start],start])
    
    while queue:
        current_dist, node = heapq.heappop(queue)
        if dist[node] < current_dist: continue
        
        for new_node, new_dist in graph[node]:
            d = current_dist + new_dist
            if d < dist[new_node]:
                dist[new_node] = d
                result[new_node] = node
                heapq.heappush(queue, [d, new_node]) 
    

dijkstra(graph, 1)
print(n - 1)
for i in range(2, n + 1):
    print(i, result[i])