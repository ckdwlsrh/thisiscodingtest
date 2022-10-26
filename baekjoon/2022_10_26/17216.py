import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

d = arr[:]

for i in range(n):
    for j in range(i):
        if arr[j] > arr[i]:
            d[i] = max(d[i],d[j] + arr[i])

print(max(d))