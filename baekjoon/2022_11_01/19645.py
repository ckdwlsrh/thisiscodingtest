import sys

N = int(sys.stdin.readline().rstrip())
burger = list(map(int, sys.stdin.readline().rstrip().split()))
ev = sum(burger) / 3
max_burger = 0

burger.sort(reverse=True)
moziri = [[] for _ in range(3)]
moziri_s = [0] * 3

i = 0
cnt = 0
while i < N:
    if ev < moziri_s[cnt % 3]:
        cnt += 1
        continue
    else:
        moziri[cnt % 3].append(burger[i])
        moziri_s[cnt % 3] += burger[i]
        i += 1
        cnt += 1

print(*moziri_s)