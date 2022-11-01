import sys
from collections import deque


N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    
    visited = [0] * 10000
    visited[a] = 1
    q = deque([(a, "")])
    while q:
        a, s = q.popleft()
        if a == b:
            print(s)
            break
        # D
        if visited[a * 2 % 10000] == 0: 
            q.append(((a * 2 % 10000), s + "D"))
            visited[a * 2 % 10000] = 1
        
        # S
        if visited[a - 1] == 0:
            if a - 1 < 0: q.append((9999, s + "S"))
            else : q.append((a - 1,s + "S"))
            visited[a - 1] = 1
        # L
        if visited[a // 1000 + (a % 1000) * 10] == 0:
            q.append((a // 1000 + (a % 1000) * 10, s + "L"))
            visited[a // 1000 + (a % 1000) * 10] = 1
        # R
        if visited[a % 10 * 1000 + a // 10] == 0: 
            q.append((a % 10 * 1000 + a // 10, s + "R"))
            visited[a % 10 * 1000 + a // 10] = 1