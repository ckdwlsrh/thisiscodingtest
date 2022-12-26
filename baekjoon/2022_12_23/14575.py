import sys

N, T = map(int, sys.stdin.readline().rstrip().split())

d = []
maxL = -1
maxR = -1
checkL = 0
checkR = 0

for i in range(N):
    L, R = map(int, sys.stdin.readline().rstrip().split())
    d.append((L, R, R - L))
    
    checkL += L
    checkR += R
    
    maxL = max(maxL, L)
    maxR = max(maxR, R)

if checkR < T or T < checkL:
    print(-1)
    exit(0)

answer = 1e9
while maxL <= maxR :
    S = (maxL + maxR) // 2
    total = 0
    remain = T
    for L, R, volume in d:
        remain -= L
        total += min(S - L, volume)
    
    if total >= remain:
        answer = min(answer, S)
        maxR = S - 1
    else:
        maxL = S + 1

print(answer)