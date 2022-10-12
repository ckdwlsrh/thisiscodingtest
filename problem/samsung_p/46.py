import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

steps = [(-1,0),(0,-1),(0,1),(1,0)]
q = deque([])
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            q.append((2, i, j))
            graph[i][j] = 0
            break
    
result = 0
times = 0
while q:
    shark_size, start_x, start_y = q.popleft()
    
    # bfs
    bfs_q = deque([])
    bfs_q.append((start_x,start_y, 0))
    visit = [[0] * n for _ in range(n)]
    edible = []
    
    while bfs_q:
        x, y, dist = bfs_q.popleft()
        for step in steps:
            nx = x + step[0]
            ny = y + step[1]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] > shark_size or visit[nx][ny] != 0:
                continue
            
            visit[nx][ny] = dist + 1
            bfs_q.append((nx,ny, dist + 1))
            
            if graph[nx][ny] < shark_size and graph[nx][ny] > 0:
                edible.append([nx,ny,visit[nx][ny]])

    if not edible:
        break
    
    edible.sort(key = lambda k:(k[2],k[0],k[1]))
    x, y, dist = edible[0]
    graph[x][y] = 0
    times += 1
    if times == shark_size:
        shark_size += 1
        times = 0
    result += visit[x][y]
    q.append((shark_size, x, y))

print(result)