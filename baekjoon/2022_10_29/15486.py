import sys

N = int(sys.stdin.readline().rstrip())
dp = [0] * (N + 1)
tmp = 0
for i in range(N):
    T, P = map(int, sys.stdin.readline().rstrip().split())
    
    tmp = max(tmp, dp[i])
    if i + T > N:
        continue
    dp[i + T] = max(dp[i + T], tmp + P)

print(max(dp))