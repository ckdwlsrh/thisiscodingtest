import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())

board = [[0] * (n+1) for _ in range(n+1)]
board[1][1] = 1
now_x, now_y = 1, 1

step = [[0,1],[1,0],[0,-1],[-1,0]]
now_d = 0
tail = deque([(1,1)])

k = int(sys.stdin.readline().rstrip())
for _ in range(k):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    board[x][y] = 9
    
l = int(sys.stdin.readline().rstrip())
move = [0] * 10001

for _ in range(l):
    s, d = sys.stdin.readline().rstrip().split()
    if d == 'D':
        move[int(s)] += 1
    else :
        move[int(s)] -= 1


for i in range(1, 10001):
    x = now_x + step[now_d][0]
    y = now_y + step[now_d][1]
    if x > n or x < 1 or y > n or y < 1:
        break
    elif board[x][y] == 1:
        break
    elif board[x][y] == 9:
        board[x][y] = 1
        now_x = x
        now_y = y
        tail.append((x,y))
    else:
        board[x][y] = 1
        tail.append((x,y))
        now_x = x
        now_y = y
        # tail pop
        tail_x, tail_y = tail.popleft()
        board[tail_x][tail_y] = 0
    now_d += move[i]
    if now_d > 3:
        now_d = 0
    elif now_d < 0:
        now_d = 3

print(i)