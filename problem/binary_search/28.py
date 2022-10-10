import sys
import bisect

n, c = map(int, sys.stdin.readline().rstrip().split())
house = []
for _ in range(n):
    house.append(int(sys.stdin.readline().rstrip()))
    
house.sort()
first = house[0]
end = house[-1]

step = (first + end) // (c - 1)

result = 0
for i in range(step, end, step):
    router = bisect.bisect_left(house,i)
    
    result = min(result,house[router] - first)
    house
    