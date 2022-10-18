import sys

N = int(sys.stdin.readline().rstrip())
milk_city = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

dp = [[[0 for _ in range(3)] for __ in range(N)] for ___ in range(N)]

if milk_city[0][0] == 0: dp[0][0][0] = 1

for i in range(1, N):
    milk = milk_city[i][0]
    if milk == 0:
        dp[i][0][0] = dp[i - 1][0][2] + 1
    else:
        dp[i][0][0] = dp[i - 1][0][0]
    if milk == 1 and dp[i][0][2] < dp[i][0][0]:
        dp[i][0][1] = dp[i - 1][0][0] + 1
    else:
        dp[i][0][1] = dp[i - 1][0][1]
    if milk == 2 and dp[i][0][0] < dp[i][0][1]:
        dp[i][0][2] = dp[i - 1][0][1] + 1
    else:
        dp[i][0][2] = dp[i - 1][0][2]

for i in range(1, N):
    milk = milk_city[0][i]
    if milk == 0:
        dp[0][i][0] = dp[0][i - 1][2] + 1
    else:
        dp[0][i][0] = dp[0][i - 1][0]
    if milk == 1 and dp[0][i][2] < dp[0][i][0]:
        dp[0][i][1] = dp[0][i - 1][0] + 1
    else:
        dp[0][i][1] = dp[0][i - 1][1]
    if milk == 2 and dp[0][i][0] < dp[0][i][1]:
        dp[0][i][2] = dp[0][i - 1][1] + 1
    else:
        dp[0][i][2] = dp[0][i - 1][2]


for i in range(1, N):
    for j in range(1, N):
        milk = milk_city[i][j] # 현재 우유 색
        if milk == 0:
            dp[i][j][0] = max(dp[i - 1][j][2] + 1, dp[i][j - 1][2] + 1)
        else:
            dp[i][j][0] = max(dp[i][j - 1][0], dp[i - 1][j][0])
        if milk == 1 and dp[i][j][2] < dp[i][j][0]:
            dp[i][j][1] = max(dp[i - 1][j][0] + 1, dp[i][j - 1][0] + 1)
        else:
            dp[i][j][1] = max(dp[i - 1][j][1], dp[i][j - 1][1])
        if milk == 2 and dp[i][j][0] < dp[i][j][1]:
            dp[i][j][2] = max(dp[i - 1][j][1] + 1, dp[i][j - 1][1] + 1)
        else:
            dp[i][j][2] = max(dp[i - 1][j][2], dp[i][j - 1][2])
                    

print(max(dp[N-1][N-1]))