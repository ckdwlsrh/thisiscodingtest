import bisect
import sys

N = int(sys.stdin.readline().rstrip())

a = []
a_index = []
b = []
b_index = []

for i in range(N):
    n , o = map(int, sys.stdin.readline().rstrip().split())
    a.append(n - o)
    a_index.append(n - o)
    b.append(n + o)
    b_index.append(n + o)

a.sort()
b.sort()

for i in range(N):
    print(bisect.bisect_left(b, a_index[i]) + 1, bisect.bisect_right(a, b_index[i]))
