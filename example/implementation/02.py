from re import A


n, m = map(int, input().split())
x, y, arrow = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(n)]
Map[x][y] = 2

steps = [(-1, 0),(0, -1),(1, 0),(0, 1)]
movin = 1
tried = 0
while True :
    
    if tried == 4:
        dx = x - steps[arrow][0]
        dy = y - steps[arrow][1]
        if dx < n or dx >= 0 or dy >= 0 or dy < m or Map[dx][dy] != 0 :
            break
        
    if arrow == 0:
        arrow = 3
    else :
        arrow -= 1
        
    dx = x + steps[arrow][0]
    dy = y + steps[arrow][1]
    tried += 1
    
    if dx < n and dx >= 0 and dy >= 0 and dy < m and Map[dx][dy] == 0:
        movin += 1
        Map[dx][dy] = 2
        x = dx
        y = dy
        tried = 0
        
print(movin)    
    

