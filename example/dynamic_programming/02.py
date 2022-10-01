import sys
n = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().rstrip().split()))

v = [0] * 101
v[1] = data[0]
v[2] = data[1]


for i in range(3, n + 1):
    v[i] = max(v[i - 1], v[i - 2] + data[i - 1])
    
print(v[n])