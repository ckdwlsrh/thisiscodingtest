from collections import deque
def solution(board):
    N = len(board)
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                board[i][j] = -1
            elif board[i][j] == 0:
                board[i][j] = 1e9
    # bfs
    queue = deque([[(0,0),(0,1)],0])
    while queue:
        r1, r2, dist = queue.popleft()
        x1, y1 = r1
        x2, y2 = r2
        board[x1][y1] = dist
        board[x2][y2] = dist
        
        #가로 상태
        if x1 == x2:
            # x1축 회전
            if x1 - 1 >= 0 and board[x1 - 1][y1 - 1] != -1 and board[x1 - 1][y1] > dist + 1:
                queue.append([[(x1,y1),(x1 - 1, y1)], dist + 1])
            if x1 + 1 < N and board[x1 - 1][y1 - 1] != -1 and board[x1 - 1][y1] > dist + 1:
                queue.append([[(x1,y1),(x1 - 1, y1)], dist + 1])
            
            # x2축 회전
            
            #상하좌우
            if x1 - 1 >= 0 and board[x1-1][y1] > dist + 1 and board[x2-1][y2] > dist + 1 :
                queue.append([[(x1-1,y1),(x2-1,y2)], dist + 1])
            if x1 + 1 < N and board[x1+1][y1] > dist + 1 and board[x2+1][y2] > dist + 1 :
                queue.append([[(x1-1,y1),(x2-1,y2)], dist + 1])
            if min(y1, y2) - 1 >= 0 and board[x1][min(y1,y2) - 1] > dist + 1:
                queue.append([[(x1,y1-1),(x2,y2-1)], dist + 1])
            if max(y1, y2) + 1 < N and board[x2][max(y1, y2) + 1] > dist + 1 :
                queue.append([[(x1,y1+1),(x2,y2+1)], dist + 1])
        #세로 상태
        if y1 == y2:
            
    
    return board[N - 1][N - 1]