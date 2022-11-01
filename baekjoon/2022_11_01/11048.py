import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
p = list(map(int, sys.stdin.readline().rstrip().split()))
for i in range(1, M):
    p[i] += p[i - 1]

for i in range(N - 1):
    last = list(map(int, sys.stdin.readline().rstrip().split()))
    dp = [0] * M
    dp[0] = p[0] + last[0]
    for j in range(1, M):
        dp[j] = max(p[j], dp[j - 1]) + last[j]
    p = dp

print(p[M - 1])