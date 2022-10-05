import sys
from collections import deque

N, K = map(int, sys.stdin.readline().rstrip().split())

cyl = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

virus = []

S, X, Y = map(int, sys.stdin.readline().rstrip().split())
for i in range(N):
    for j in range(N):
        if cyl[i][j] != 0:
            virus.append([cyl[i][j],i,j])
            cyl[i][j] = 0

virus.sort(key=lambda k:k[0])

second = -1
last = K
queue = deque(virus)

while queue and second != S:
    now, x, y = queue.popleft()
    if now == 1 and last == K:
        second += 1
        last = now
    if x < 0 or x >= N or y < 0 or y >= N:
        continue
    if cyl[x][y] != 0:
        continue
    cyl[x][y] = now
    queue.append([now,x - 1,y])
    queue.append([now,x + 1,y])
    queue.append([now,x,y - 1])
    queue.append([now,x,y + 1])
    
    last = now
    
print(cyl[X-1][Y-1])