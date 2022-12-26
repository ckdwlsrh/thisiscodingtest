import sys

n = int(sys.stdin.readline().rstrip())
desert = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
directions = [(0, -1), (1, 0), (0, 1), (-1, 0), (0, -1), (1, 0), (0, 1), (-1, 0)]

def tornadomove(x, y, d):
    sand_total = desert[x][y]
    sand_out = 0
    # 옆 1칸
    if x + directions[d - 1][0] < 0 or x + directions[d - 1][0] >= n or y + directions[d - 1][1] < 0 or y + directions[d - 1][1] >= n:
        sand_out += int(sand_total / 100 * 7)
    else:
        desert[x + directions[d - 1][0]][y + directions[d - 1][1]] += int(sand_total / 100 * 7)
    desert[x][y] -= int(sand_total / 100 * 7)
    if x + directions[d + 1][0] < 0 or x + directions[d + 1][0] >= n or y + directions[d + 1][1] < 0 or y + directions[d + 1][1] >= n:
        sand_out += int(sand_total / 100 * 7)
    else:
        desert[x + directions[d + 1][0]][y + directions[d + 1][1]] += int(sand_total / 100 * 7)
    desert[x][y] -= int(sand_total / 100 * 7)
    
    # 옆 2칸
    if x + directions[d - 1][0] * 2 < 0 or x + directions[d - 1][0] * 2 >= n or y + directions[d - 1][1] * 2 < 0 or y + directions[d - 1][1] * 2 >= n:
        sand_out += int(sand_total / 100 * 2)
    else:
        desert[x + directions[d - 1][0] * 2][y + directions[d - 1][1] * 2] += int(sand_total / 100 * 2)
    desert[x][y] -= int(sand_total / 100 * 2)
    
    if x + directions[d + 1][0] * 2 < 0 or x + directions[d + 1][0] * 2 >= n or y + directions[d + 1][1] * 2 < 0 or y + directions[d + 1][1] * 2 >= n:
        sand_out += int(sand_total / 100 * 2)
    else:
        desert[x + directions[d + 1][0] * 2][y + directions[d + 1][1] * 2] += int(sand_total / 100 * 2)
    desert[x][y] -= int(sand_total / 100 * 2)
    
    # 앞 2칸
    if x + directions[d][0] * 2 < 0 or x + directions[d][0] * 2 >= n or y + directions[d][1] * 2 < 0 or y + directions[d][1] * 2 >= n:
        sand_out += int(sand_total / 100 * 5)
    else:
        desert[x + directions[d][0] * 2][y + directions[d][1] * 2] += int(sand_total / 100 * 5)
    desert[x][y] -= int(sand_total / 100 * 5)

    # 대각 앞 1칸
    if x + directions[d][0] + directions[d - 1][0] < 0 or x + directions[d][0] + directions[d - 1][0] >= n or y + directions[d][1] + directions[d - 1][1] < 0 or y + directions[d][1] + directions[d - 1][1] >= n:
        sand_out += int(sand_total / 100 * 10)
    else:
        desert[x + directions[d][0] + directions[d - 1][0]][y + directions[d][1] + directions[d - 1][1]] += int(sand_total / 100 * 10)
    desert[x][y] -= int(sand_total / 100 * 10)
    if x + directions[d][0] + directions[d + 1][0] < 0 or x + directions[d][0] + directions[d + 1][0] >= n or y + directions[d][1] + directions[d + 1][1] < 0 or y + directions[d][1] + directions[d + 1][1] >= n:
        sand_out += int(sand_total / 100 * 10)
    else:
        desert[x + directions[d][0] + directions[d + 1][0]][y + directions[d][1] + directions[d + 1][1]] += int(sand_total / 100 * 10)
    desert[x][y] -= int(sand_total / 100 * 10)
    
    # 대각 뒤 1칸
    if x + directions[d + 2][0] + directions[d - 1][0] < 0 or x + directions[d + 2][0] + directions[d - 1][0] >= n or y + directions[d + 2][1] + directions[d - 1][1] < 0 or y + directions[d + 2][1] + directions[d - 1][1] >= n:
        sand_out += int(sand_total / 100)
    else:
        desert[x + directions[d + 2][0] + directions[d - 1][0]][y + directions[d + 2][1] + directions[d - 1][1]] += int(sand_total / 100)
    desert[x][y] -= int(sand_total / 100)
    if x + directions[d + 2][0] + directions[d + 1][0] < 0 or x + directions[d + 2][0] + directions[d + 1][0] >= n or y + directions[d + 2][1] + directions[d + 1][1] < 0 or y + directions[d + 2][1] + directions[d + 1][1] >= n:
        sand_out += int(sand_total / 100)
    else:
        desert[x + directions[d + 2][0] + directions[d + 1][0]][y + directions[d + 2][1] + directions[d + 1][1]] += int(sand_total / 100)
    desert[x][y] -= int(sand_total / 100)

    # 알파 칸
    if x + directions[d][0] < 0 or x + directions[d][0] >= n or y + directions[d][1] < 0 or y + directions[d][1] >= n:
        sand_out += desert[x][y]
    else:
        desert[x + directions[d][0]][y + directions[d][1]] += desert[x][y]
    desert[x][y] = 0

    return sand_out

def solve(x, y):
    answer = 0
    direction = 0
    d_cnt = 1
    m_cnt = 0
    odd_check = True
    while x != 0 or y != 0:
        x += directions[direction][0]
        y += directions[direction][1]
        answer += tornadomove(x, y, direction)
        m_cnt += 1
        
        if d_cnt == m_cnt:
            m_cnt = 0
            direction += 1
            if direction == 4: direction = 0
            if odd_check: 
                odd_check = False
            else: 
                d_cnt += 1
                odd_check = True
        
        
    print(answer)
        


solve(n // 2, n // 2)


# 1v 2v 3 4v 5 6v 7 8 9v 10 11 12v 