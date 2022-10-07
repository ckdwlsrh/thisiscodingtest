import sys
import copy
from collections import deque
N, L, R = map(int, sys.stdin.readline().rstrip().split())

nations = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
unions = []

def bfs(start,day_visit, day_visit2):
    queue = deque([start])
    
    day_visit2[start[0]][start[1]] = 1
    unions = set()
    unions_cnt = 0
    total = 0
    while queue:
        nx, ny = queue.popleft()
        total += nations[nx][ny]
        unions_cnt += 1
        unions.add((nx,ny))
        day_visit.discard((nx, ny))
        
        if nx - 1 >= 0 and L <= abs(nations[nx-1][ny] - nations[nx][ny]) and abs(nations[nx-1][ny] - nations[nx][ny]) <= R and day_visit2[nx-1][ny] != 1:
            day_visit2[nx-1][ny] = 1
            queue.append([nx - 1,ny])
        
        if nx + 1 < N and L <= abs(nations[nx+1][ny] - nations[nx][ny]) and abs(nations[nx+1][ny] - nations[nx][ny]) <= R and day_visit2[nx+1][ny] != 1:
            day_visit2[nx+1][ny] = 1
            queue.append([nx + 1,ny])
        
        if ny - 1 >= 0 and L <= abs(nations[nx][ny-1] - nations[nx][ny]) and abs(nations[nx][ny-1] - nations[nx][ny]) <= R and day_visit2[nx][ny-1] != 1:
            day_visit2[nx][ny-1] = 1
            queue.append([nx,ny - 1])
        
        if ny + 1 < N and L <= abs(nations[nx][ny+1] - nations[nx][ny]) and abs(nations[nx][ny+1] - nations[nx][ny]) <= R and day_visit2[nx][ny+1] != 1:
            day_visit2[nx][ny+1] = 1
            queue.append([nx,ny + 1])
        
    for x, y in unions:
        nations[x][y] = total // unions_cnt
    
day = 0
while True:
    
    day_visit = set()
    for i in range(N):
        for j in range(N):
            day_visit.add((i,j))
    
    day_visit2 = [[0] * N for _ in range(N)]
    check_cnt = 0
    
    while day_visit:
        check_cnt += 1
        bfs(day_visit.pop(), day_visit, day_visit2)
    
    if check_cnt == N*N:
        break
    day += 1
    
print(day)