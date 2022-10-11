import sys

n = int(sys.stdin.readline().rstrip())
triangle = []
for i in range(n):
    arr = list(map(int,sys.stdin.readline().rstrip().split()))
    m = len(arr)
    triangle.append(arr)
    if i == 0:
        continue
    triangle[i][0] += triangle[i - 1][0]
    for j in range(1, m - 1):
        triangle[i][j] += max(triangle[i - 1][j], triangle[i - 1][j - 1])
    triangle[i][m - 1] += triangle[i - 1][m - 2]

print(max(triangle[n - 1]))