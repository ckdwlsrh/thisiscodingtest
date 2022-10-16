import sys
import itertools
import copy

n = 4 # 격자
m = 16 # 물고기 수
answer = 0
direction = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]

g = [[0] * n for _ in range(n)]

f = [[] for _ in range(m + 1)] # now_X, now_Y, Direction

for i in range(n):
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(0, n * 2, 2):
        g[i][j // 2] = arr[j]
        f[arr[j]] = [i, j // 2, arr[j + 1] - 1]


def rotate(graph, fishes, shark_locate):
    for i in range(1, m + 1):
        x, y, d = fishes[i]
        if d == -1:
            continue
        for s in itertools.chain(range(d,8), range(0,d)):
            nx = x + direction[s][0]
            ny = y + direction[s][1]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            
            if graph[nx][ny] != shark_locate:
                fishes[i] = [nx, ny, s]
                fishes[graph[nx][ny]] = [x , y, fishes[graph[nx][ny]][2]]
                
                graph[x][y], graph[nx][ny] = graph[nx][ny], graph[x][y]
                
                break
    
def dfs(graph, fishes, sx, sy, result):
    global answer
    #지금 그래프 복제해놓기
    graph_tmp = copy.deepcopy(graph)
    fish_tmp = copy.deepcopy(fishes)
    """
    graph_tmp = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            graph_tmp[i].append(graph[i][j])
    
    fish_tmp = []
    for i in range(m+1):
        fish_tmp.append(fishes[i])
    """
    #상어 먼저 움직이기
    now_fish = graph_tmp[sx][sy]
    result += now_fish
    
    direct = fish_tmp[now_fish][2]
    
    fish_tmp[now_fish][2] = -1
    
    #물고기 진행
    rotate(graph_tmp, fish_tmp, now_fish)
    
    # 갈곳 넣기
    for i in range(1,4):
        sx += direction[direct][0]
        sy += direction[direct][1]

        if sx < 0 or sx >= n or sy < 0 or sy >= n:
            continue
        if fish_tmp[graph_tmp[sx][sy]][2] == -1:
            continue
        
        dfs(graph_tmp, fish_tmp, sx, sy, result)
    # 원래대로 돌리기 rotate
    
    answer = max(answer, result)

dfs(g, f, 0, 0, 0)
print(answer)