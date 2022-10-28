import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
bomb = [[0 for _ in range(N)] for __ in range(N)]
R = M // 2

def check_bomb(sx, sy):
    
    bomb[sx][sy] -= graph[sx - R][sy - R]
    if sx - R - 1 >= 0:
        bomb[sx][sy] += graph[sx - R - 1][sy - R]
    if sy - R - 1 >= 0:
        bomb[sx][sy] += graph[sx - R][sy - R - 1]
    if sx - R - 1 >= 0 and sy - R - 1 >= 0:
        bomb[sx][sy] -= graph[sx - R - 1][sy - R - 1]
    if sx - M >= 0:
        bomb[sx][sy] += bomb[sx - M][sy]
    if sy - M >= 0:
        bomb[sx][sy] += bomb[sx][sy - M]
    if sx - M >= 0 and sy - M >= 0:
        bomb[sx][sy] -= bomb[sx- M][sy - M]
        
    
for i in range(R, N - R):
    for j in range(R, N - R):
        check_bomb(i, j)

for i in range(N):
    print(*bomb[i])
