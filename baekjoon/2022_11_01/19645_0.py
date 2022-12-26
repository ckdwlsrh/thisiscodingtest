import sys
import bisect

N = int(sys.stdin.readline().rstrip())
burger = list(map(int, sys.stdin.readline().rstrip().split()))
s = sum(burger)

dp = [[0] * (N * 50 + 1) for _ in range(N * 50 + 1)]
dp[0][0] = 1

for i in burger:
    dp[i][0]