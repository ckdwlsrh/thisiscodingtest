import sys
import itertools
import copy

N = int(sys.stdin.readline().rstrip())

school = [list(sys.stdin.readline().rstrip().split()) for _ in range(N)]
teachers = []
space = []

steps = [[0,1],[0,-1],[1,0],[-1,0]]


for i in range(N):
    for j in range(N):
        if school[i][j] == 'T':
            teachers.append([i,j])
        elif school[i][j] == 'X':
            space.append([i,j])

monitored = False

for obstacle in itertools.combinations(space,3):
    tmp_school = copy.deepcopy(school)
    for i, j in obstacle:
        tmp_school[i][j] = 'O'
    
    monitored = False # f -> 안걸림 True -> 걸림
    
    for i, j in teachers:
        for step in steps:
            x, y = i + step[0], j + step[1]
            while True:
                if x < 0 or x >= N or y < 0 or y >= N:
                    break
                if tmp_school[x][y] == 'O':
                    break
                if tmp_school[x][y] == 'T':
                    break
                if tmp_school[x][y] == 'S':
                    monitored = True
                    break
                x += step[0]
                y += step[1]
            if monitored:
                break
        if monitored:
            break
    
    if not monitored:
        break

if not monitored:
    print("YES")
elif monitored:
    print("NO")