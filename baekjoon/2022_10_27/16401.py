import sys
import bisect

M, N = map(int, sys.stdin.readline().rstrip().split())
snacks = list(map(int, sys.stdin.readline().rstrip().split()))

snacks.sort()

first = 0
end = snacks[-1]

result = 0
while first <= end:
    
    mid = (first + end) // 2
    if mid == 0:
        break
    
    cnt = 0
    for i in range(N - 1, -1, -1):
        cnt += snacks[i] // mid
        if snacks[i] // mid == 0:
            break
    
    if cnt >= M:
        result = mid
        first = mid + 1
    elif cnt < M:
        end = mid - 1
print(result)