import sys
import itertools

n = int(sys.stdin.readline().rstrip())
d = [1,2,3,5]

for i in range(0,1001):
    d.append(d[i] * 2)
    d.append(d[i] * 3)
    d.append(d[i] * 5)

d = sorted(list(set(d)))

for i, j in zip(d,range(1, 1001)):
    if j == n:
        print(i)
