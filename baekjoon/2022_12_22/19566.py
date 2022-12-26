import sys
import collections
n, k = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
result = 0
psum = [0] + arr[:]
need = collections.defaultdict(int)


for i in range(1, n + 1):
    psum[i] += psum[i - 1]
    cnt = psum[i] - k * i
    
    result += need[cnt]
    need[cnt] += 1 
print(result + need[0])