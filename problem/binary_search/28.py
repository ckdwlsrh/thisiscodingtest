import sys
import bisect

n = int(sys.stdin.readline().rstrip())
array = list(map(int,sys.stdin.readline().rstrip().split()))

first = 0
end = n - 1

while first <= end:
    mid = (first + end) // 2
    if array[mid] == mid:
        print(mid)
        exit(0)
    elif array[mid] > mid:
        end = mid - 1
    elif array[mid] < mid:
        first = mid + 1

print(-1)