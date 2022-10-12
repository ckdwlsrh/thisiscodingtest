import sys
import heapq
t = int(sys.stdin.readline().rstrip())

steps = [(-1,0),(0,1),(1,0),(0,-1)]
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    graph = []
    for i in range(n):
        graph.append(list(map(int,sys.stdin.readline().rstrip().split())))
    
    mst = [[1e9] * n for __ in range(n)]
    queue = []
    heapq.heappush(queue, (graph[0][0],0,0))
    
    while queue:
        cost, x, y = heapq.heappop(queue)
        if mst[x][y] < cost:
            continue
        mst[x][y] = cost
        for step in steps:
            nx = x + step[0]
            ny = y + step[1]
            if nx < 0 or nx >= n or ny < 0 or ny >= n :
                continue
            heapq.heappush(queue, (cost + graph[nx][ny], nx, ny))
    
    print(mst[n-1][n-1])