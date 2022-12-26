import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
area = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

for i in range(1, n):
    area[i][0] += area[i - 1][0]
for j in range(1, m):
    area[0][j] += area[0][j - 1]

for i in range(1, n):
    for j in range(1, m):
        area[i][j] += area[i - 1][j] + area[i][j - 1] - area[i - 1][j - 1]

k = int(sys.stdin.readline().rstrip())

def prefix_sum(sx, sy, ex, ey):
    result = 0
    result += area[ex][ey]
    if sx - 1 >= 0 :
        result -= area[sx - 1][ey]
    if sy - 1 >= 0 :
        result -= area[ex][sy - 1]
    if sx - 1 >= 0 and sy - 1 >= 0:
        result += area[sx - 1][sy - 1]
    
    print(result)

for l in range(k):
    sx, sy, ex, ey = map(int, sys.stdin.readline().rstrip().split())
    prefix_sum(sx - 1, sy - 1, ex - 1, ey - 1)