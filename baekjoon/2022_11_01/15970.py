import sys

N = int(sys.stdin.readline().rstrip())
dot = []
colors = set()
result = 0
for _ in range(N):
    pos, color = map(int, sys.stdin.readline().rstrip().split())
    dot.append((pos,color))
    colors.add(color)

dot.sort(key=lambda k:(k[1],k[0]))


for i in range(N):
    left, right = 1e9, 1e9
    
    if i - 1 >= 0 and dot[i - 1][1] == dot[i][1]:
        left = abs(dot[i][0] - dot[i - 1][0])
    if i + 1 < N and dot[i + 1][1] == dot[i][1]:
        right = abs(dot[i][0] - dot[i + 1][0])
    
    if left == 1e9 and right == 1e9:
        result += 0
    else:
        result += min(left, right)

print(result)