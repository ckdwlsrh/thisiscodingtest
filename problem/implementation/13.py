from functools import total_ordering
import sys
import itertools

n, m = map(int, sys.stdin.readline().rstrip().split())
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
house = []
chickens = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append([i,j])
        elif graph[i][j] == 2:
            chickens.append([i,j])

result = 1000000
for chicken in itertools.combinations(chickens,m):
    total = 0
    for i, j in house:
        close_chick = 100000
        for x, y in chicken:
            close_chick = min(close_chick, abs(i - x) + abs(j - y))
        total += close_chick
    
    result = min(result, total)

print(result)