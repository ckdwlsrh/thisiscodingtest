def solution(n, build_frame):
    building = [[0] * (n+1) for _ in range(n+1)]
    answer = []
    for x, y, a, b in build_frame:
        if a == 0 and b == 1 and (building[x][y] >= 1 or y == 0):
            building[x][y] = 1
            building[x][y + 1] = 1
            answer.append([x,y,a])
        elif a == 1 and b == 1 and (building[x][y] == 1 or building[x + 1][y] == 1 or (building[x + 1][y] == 2 and building[x - 1][y] == 2)):
            building[x][y] = 2
            building[x + 1][y] = 2
            answer.append([x,y,a])
    
    answer.sort(key=lambda k:(k[0],k[1])
    return answer