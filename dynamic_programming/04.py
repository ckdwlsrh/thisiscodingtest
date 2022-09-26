import sys
n, m = map(int,sys.stdin.readline().rstrip().split())
w = []
d = [100000] * 10001

for _ in range(n):
    w.append(int(sys.stdin.readline().rstrip()))
    d[w[_]] = 1

w.sort()

for i in range(1, m+1):
    for j in range(n):
        
        if i - w[j] < 1:
            break
        
        d[i] = min(d[i] , d[i - w[j]] + 1)

if d[m] == 100000:
    print(-1)
else :
    print(d[m])