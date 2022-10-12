import sys
import heapq

n, m = map(int, sys.stdin.readline().rstrip().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    graph[x].append(y)
    graph[y].append(x)

md = [1e9 for _ in range(n + 1)]

queue = []
heapq.heappush(queue, (0, 1))

while queue:
    dist, x = heapq.heappop(queue)
    if md[x] < dist:
        continue
    md[x] = dist
    for i in graph[x]:
        heapq.heappush(queue, (md[x] + 1, i))

md[0] = -1

sorted_md = sorted(range(len(md)), key=lambda k:-md[k])

result = md[sorted_md[0]]
result_index = sorted_md[0]
count = 0
for i in sorted_md:
    if md[i] != result:
        break
    count += 1

print(str(result_index) + " " + str(result)+ " " + str(count))