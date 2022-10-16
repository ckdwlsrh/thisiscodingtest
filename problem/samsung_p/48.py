from re import S
import sys
from collections import deque

N, M, k = map(int, sys.stdin.readline().rstrip().split())

graph = []
sharks = [[] for _ in range(M + 1)]
directions = [[-1,0],[1,0],[0,-1],[0,1]]
sharks_direction = [[[] for __ in range(5)] for _ in range(M + 1)]


for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    for j in range(N):
        if graph[i][j] != 0:
            sharks[graph[i][j]] = [i, j]

first_direction = list(map(int, sys.stdin.readline().rstrip().split()))
for i, d in zip(range(1, M + 1), first_direction):
    sharks[i].append(d)
    
for i in range(M * 4):
    order = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in order:
        sharks_direction[i//4 + 1][i%4 + 1].append(directions[j - 1])

time = 0
cnt = 0
while time <= 1000 and cnt < M - 1:
    # 냄새 뿌리기
    for i in range(N):
        for j in range(N):
            if graph[i][j] > 10000:
                graph[i][j] -= 1
                if graph[i][j] % 10000 == 0:
                    graph[i][j] = 0
    
    for i in range(1, M + 1):
        x, y, d = sharks[i]
        if x == -1 and y == -1:
            continue
        graph[x][y] = i * 10000 + k
    
    # 움직인다
    for i in range(1, M + 1):
        x, y, d = sharks[i]
        if x == -1 and y == -1:
            continue
        # 빈공간 중 우선순위
        into_smell = []
        for steps in sharks_direction[i][d]:
            nx = x + steps[0]
            ny = y + steps[1]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if graph[nx][ny] > 10000:
                if graph[nx][ny] // 10000 == i and not into_smell:
                    into_smell = [nx, ny, directions.index(steps) + 1]
                continue
            
            sharks[i] = [nx, ny, directions.index(steps) + 1]
            break
        #  냄새 중 우선순위
        if sharks[i] == [x, y, d]:
            sharks[i] = [into_smell[0], into_smell[1], into_smell[2]]
        
    # 같은 자리의 상어들 다 삭제
    for i in range(1, M + 1):
        x, y, d = sharks[i]
        if x == -1 and y == -1:
            continue
        if graph[x][y] == 0:
            graph[x][y] = i
        elif graph[x][y] // 10000 == i:
            graph[x][y] = i
        elif graph[x][y] < i:
            sharks[i] = [-1, -1, -1]
            cnt += 1
    
    time += 1

if time > 1000:
    print(-1)
else:
    print(time)