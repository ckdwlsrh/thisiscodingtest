from collections import deque

n, m = map(int, input().split())

graph = [list(map(int, input())) for _ in range(n)]

cnt = 1
x = 0
y = 0
queue = deque([(x, y, cnt)])


while queue:
    x, y, cnt = queue.popleft()
    
    if x < 0 or x >= n or y < 0 or y >= m:
        continue
    
    if graph[x][y] == 1:
        graph[x][y] = cnt
        cnt += 1
        
        queue.append((x - 1, y, cnt))
        queue.append((x + 1, y, cnt))
        queue.append((x, y - 1, cnt))
        queue.append((x, y + 1, cnt))
        
    

print(graph[n-1][m-1])