import sys
T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    gold = list(map(int, sys.stdin.readline().rstrip().split()))
    result = 0
    for j in range(1, m):
        for i in range(n):
            if i == 0:
                gold[i * m + j] += max(gold[i * m + j - 1], gold[(i + 1) * m + j - 1])
            elif i == n - 1:
                gold[i * m + j] += max(gold[(i - 1) * m + j - 1], gold[i * m + j - 1])
            else:
                gold[i * m + j] += max(gold[(i - 1) * m + j - 1], gold[i * m + j - 1], gold[(i + 1) * m + j - 1])
            
            result = max(result, gold[i * m + j])
    print(result)