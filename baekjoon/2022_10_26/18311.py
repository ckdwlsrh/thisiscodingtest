import sys

N, K = map(int, sys.stdin.readline().rstrip().split())

cs = list(map(int, sys.stdin.readline().rstrip().split()))

total = 0
for i in range(N):
    total += cs[i]
    if total > K:
        print(i + 1)
        exit(0)

for i in range(N - 1, -1 , -1):
    total += cs[i]
    if total > K:
        print(i + 1)
        break