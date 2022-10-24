import sys
from collections import deque

N, k = map(int, sys.stdin.readline().rstrip().split())
path = []

path.append(list(sys.stdin.readline().rstrip()))
path.append(list(sys.stdin.readline().rstrip()))

q = deque([(0,0,0)]) # 현재 위치, 좌우 방향 , 없어진 길

while q:
    x, d, r = q.popleft()
    
    if x + k >= N:
        print(1)
        exit(0)
    
    if path[d][x + 1] != "0":
        path[d][x + 1] = "0"
        q.append((x + 1, d, r + 1))
    
    if x - 1 > r and path[d][x - 1] != "0" :
        path[d][x - 1] = "0"
        q.append((x - 1, d, r + 1))
    
    if d == 1:
        if path[0][x + k] != "0":
            path[0][x + k] = "0"
            q.append((x + k, 0, r + 1))
    else:
        if path[1][x + k] != "0":
            path[1][x + k] = "0"
            q.append((x + k, 1, r + 1))

print(0)