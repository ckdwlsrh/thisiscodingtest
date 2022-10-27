import sys

N, M, H = map(int, sys.stdin.readline().rstrip().split())

blocks = []
dp = [0 for _ in range(50001)]
able = set()

for i in range(N):
    blocks.append(list(map(int, sys.stdin.readline().rstrip().split())))
    if i == 0:
        blocks[i].append(0)
        able = set(blocks[i])
        for j in blocks[i]:
            dp[j] += 1
        continue
    
    tmp = []
    for j in sorted(list(able),reverse=True):
        for k in blocks[i]:
            if dp[k + j] == 0:
                dp[k + j] = dp[j]
                tmp.append(k + j)
            else:
                dp[k + j] += dp[j]
        
    able = able.union(set(tmp))

print(dp[H] % 10007)