import sys

N = int(sys.stdin.readline().rstrip())
antena = list(map(int, sys.stdin.readline().rstrip().split()))

antena.sort()
mid = (antena[0] + antena[-1]) // 2

last = antena[0]
for i in antena[1:]:
    if i > mid :
        mid = last 
        break
    last = i
print(mid)