import sys
import bisect

n, x = map(int, sys.stdin.readline().rstrip().split())
array = list(map(int, sys.stdin.readline().rstrip().split()))

left = bisect.bisect_left(array,x)
right = bisect.bisect_right(array,x)

if right - left == 0 :
    print(-1)
else :
    print(right - left)