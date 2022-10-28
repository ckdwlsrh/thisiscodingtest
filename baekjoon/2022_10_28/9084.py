import sys

T = int(sys.stdin.readline().rstrip())
result = []
for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    coins = list(map(int, sys.stdin.readline().rstrip().split()))
    M = int(sys.stdin.readline().rstrip())
    
    dp = [0] * (M + 1)
    dp[0] = 1
    
    for coin in coins:
        for able in range(M+1):
            if able >= coin:
                dp[able] += dp[able - coin]

    result.append(dp[M])

print(*result,sep='\n')