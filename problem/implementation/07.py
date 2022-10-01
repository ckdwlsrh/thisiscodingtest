import sys

N = sys.stdin.readline().rstrip()
l = len(N)
left = 0
right = 0
for i in range(l//2):
    left += int(N[i])
    right += int(N[l//2 + i])
if left == right:
    print("LUCKY")
else:
    print("READY")