import sys

n, m, x, y, k = map(int, sys.stdin.readline().split())
MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dices = [0] * 6
forwardpoint = 0
endpoint = 5

def change_pos(d):
    global n, m, x, y
    F, E, S, W, N, B = dices 
    if d == 1 and y + 1 < m:
        dices[0] = W
        dices[5] = E
        dices[1] = F
        dices[3] = B
        y += 1
    elif d == 2 and y - 1 >= 0:
        dices[0] = E
        dices[5] = W
        dices[1] = B
        dices[3] = F
        y -= 1
    elif d == 3 and x - 1 >= 0:
        dices[0] = S
        dices[5] = N
        dices[2] = B
        dices[4] = F
        x -= 1
    elif d == 4 and x + 1 < n:
        dices[0] = N
        dices[5] = S
        dices[2] = F
        dices[4] = B
        x += 1
    else:
        return False
    return True


direction = list(map(int, sys.stdin.readline().split()))
for dir in direction:
    if change_pos(dir): 
        if MAP[x][y] == 0:
            MAP[x][y] = dices[5]
        else:
            dices[5] = MAP[x][y]
            MAP[x][y] = 0
        print(dices[0])




