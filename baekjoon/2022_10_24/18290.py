import sys
import itertools

N, M, k = map(int, sys.stdin.readline().rstrip().split())

board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

xy = []

for i in range(N):
    for j in range(M):
        xy.append((i,j))

result = -100000

for i in itertools.combinations(xy, k):
    checked = False
    check = set(i)
    for x, y in i:
        if (x + 1, y) in check or (x - 1, y) in check or (x, y + 1) in check or (x, y - 1) in check:
            checked = True
            break
    
    if checked: continue
    
    s = 0
    for x, y in i:
        s += board[x][y]
    
    result = max(result, s)

print(result)