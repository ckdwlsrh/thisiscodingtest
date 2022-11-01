import sys
from collections import deque
import itertools

N, M, G, R = map(int, sys.stdin.readline().rstrip().split())
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
able = []
flower = 999

steps = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def bfs(start_G, start_R):
    q = deque([])
    result = 0
    visited = [[[0, 0] for __ in range(M)]  for _ in range(N)]
    for point in start_G:
        x, y = point
        q.append((x, y, 4, 0))
        visited[x][y][0] = 4
    for point in start_R:
        x, y = point
        q.append((x, y, -4, 0))
        visited[x][y][0] = -4
    
    while q:
        x, y, color, sec = q.popleft()
        if visited[x][y][0] == flower:
            continue
        for step in steps:
            nx, ny = x + step[0], y + step[1]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if graph[nx][ny] == 0:
                continue
            if visited[nx][ny][0] != 0:
                if visited[nx][ny][1] == sec + 1 and visited[nx][ny][0] == (color * -1):
                    result += 1
                    visited[nx][ny][0] = flower
                continue
            visited[nx][ny][0] = color
            visited[nx][ny][1] = sec + 1
            q.append((nx,ny,color,sec + 1))
    
    return result
        

for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            able.append((i, j))

# 전체 경우의 수
answer = 0
for t in itertools.combinations(able, G + R):
    for green in itertools.combinations(t, G):
        red = set(t) - set(green)
        answer = max(answer, bfs(list(green),list(red)))

print(answer)