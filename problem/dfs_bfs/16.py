import sys
import itertools
import copy

N, M = map(int, sys.stdin.readline().rstrip().split())
lab = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
lab_test = []
virus = []
space = []

def spread(x, y):
    
    if x < 0 or x >= N or y < 0 or y >= M:
        return
    if lab_test[x][y] == 2 or lab_test[x][y] == 1:
        return
    lab_test[x][y] = 2
    spread(x - 1, y)
    spread(x + 1, y)
    spread(x, y - 1)
    spread(x, y + 1)
    return


for i in range(N):
    for j in range(M):
        if lab[i][j] == 2:
            virus.append([i,j])
        elif lab[i][j] == 0:
            space.append([i,j])
            
result = 0

for walls in itertools.combinations(space,3):
    
    lab_test = copy.deepcopy(lab)
    
    for x, y in walls:
        lab_test[x][y] = 1
    
    for x, y in virus:
        spread(x - 1, y)
        spread(x + 1, y)
        spread(x, y - 1)
        spread(x, y + 1)
    
    cnt = 0
    for i in range(N):
        for j in range(M):
            if lab_test[i][j] == 0:
                cnt += 1 
    
    result = max(result, cnt)
    lab_test.clear()
    
print(result)