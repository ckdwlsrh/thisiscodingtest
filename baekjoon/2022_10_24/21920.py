import sys
import math

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
X = int(sys.stdin.readline().rstrip())

S = 0
cnt = 0

for i in range(N):
    if math.gcd(A[i], X) == 1:
        S += A[i]
        cnt += 1

if cnt == 0:
    print(0)
else:
    print("{:.6f}".format(S/cnt))