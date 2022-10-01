import sys

n = int(sys.stdin.readline().rstrip())
fear = list(map(int, sys.stdin.readline().rstrip().split()))

fear.sort()
cnt = [0] * (n + 1)


for i in range(n):
    cnt[fear[i]] += 1

result = 0
max = n
for i in range(1, n):
    cnt[i + 1] += cnt[i] % i
    cnt[i] //= i
    max -= cnt[i] * i
    if max < 0:
        break
    result += cnt[i]

print(result)

