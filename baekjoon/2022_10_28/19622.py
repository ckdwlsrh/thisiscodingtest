import sys

N = int(sys.stdin.readline().rstrip())
meetings = []
dp = [[0, 0] for _ in range(N + 3)]

result = 0
for i in range(2, N + 2):
    start, end, people = map(int, sys.stdin.readline().rstrip().split())
    
    dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
    dp[i][1] = max(dp[i - 1][0], dp[i - 2][1]) + people
    
    result = max(result, dp[i][0], dp[i][1])

print(result)