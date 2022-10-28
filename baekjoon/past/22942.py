import sys

n = int(sys.stdin.readline().rstrip())

circles = {}
for _ in range(n):
    x, r = map(int,sys.stdin.readline().rstrip().split())
    circles[x - r] = x + r


last_left = -1e9
last_right = -1e9
for x in sorted(circles.keys()):
    if last_left == -1e9:
        last_left = x
        last_right = circles[x]
        continue
    left = x
    right = circles[x]
    
    
    if right < last_right :
        pass
    elif last_right < left:
        pass
    else:
        print('NO')
        exit(0)
    last_left = x
    last_right = circles[x]

print('YES')
    
    