import sys

n, m = map(int, sys.stdin.readline().split())
MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

tetro = [
    [[0,0],[0,1],[1,0],[1,1]], # 1
    [[0,0],[0,1],[0,2],[0,3]], # 2
    [[0,0],[0,1],[1,1],[1,2]],
    [[0,0],[0,1],[0,2],[1,1]],
    [[0,0],[1,0],[2,0],[2,1]]
]

def roll(t, x, y):
    answer = 0
    for i in range(4):
        sum = 0
        for dx, dy in t:
            if x + dx >= n or x + dx < 0 or y + dy >= m or y + dy < 0:
                break
            sum += MAP[x+ dx][y + dy]
        answer = max(answer, sum)
        answer = max(answer, reverse(t, x, y))
        for j in range(4):
            t[j][0], t[j][1] = t[j][1], t[j][0]
            t[j][0] *= -1
        
    
    return answer

def reverse(t, x, y):
    answer = 0
    # x -
    sum = 0
    for j in range(4):
        t[j][0] *= -1
    for dx, dy in t:
        if x + dx >= n or x + dx < 0 or y + dy >= m or y + dy < 0:
            break
        sum += MAP[x+ dx][y + dy]
    answer = max(answer, sum)

    # xy -
    sum = 0
    for j in range(4):
        t[j][1] *= -1
    for dx, dy in t:
        if x + dx >= n or x + dx < 0 or y + dy >= m or y + dy < 0:
            break
        sum += MAP[x+ dx][y + dy]
    answer = max(answer, sum)

    # y -
    sum = 0
    for j in range(4):
        t[j][0] *= -1
    for dx, dy in t:
        if x + dx >= n or x + dx < 0 or y + dy >= m or y + dy < 0:
            break
        sum += MAP[x+ dx][y + dy]
    answer = max(answer, sum)
    
    return answer



answer = 0

for i in range(n):
    for j in range(m):
        for t in tetro:
            answer = max(answer, roll(t, i, j))

print(answer)