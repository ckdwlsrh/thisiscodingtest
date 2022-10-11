import sys

n = int(sys.stdin.readline().rstrip())
soldiers = list(map(int, sys.stdin.readline().rstrip().split()))
result = [1 for _ in range(n)]
answer = 1

for i in range(1, n):
    for j in range(0, i):
        if soldiers[j] > soldiers[i]:
            result[i] = max(result[i], result[j] + 1)
            answer = max(answer, result[i])

print(n - answer)