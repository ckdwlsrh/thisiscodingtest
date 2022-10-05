import sys
from collections import deque

N, M, K, X = map(int, sys.stdin.readline().rstrip().split())
path = [[] for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    path[x].append(y)

cities = [-1] * (N + 1)
queue = deque([X])
cities[X] = 0

result = []
while queue:
    now = queue.popleft()
    for city in path[now]:
        if cities[city] != -1:
            continue
        cities[city] = cities[now] + 1
        if cities[city] == K:
            result.append(city)
        queue.append(city)


if result:
    result.sort()
    for i in result:
        print(i)
else:
    print(-1)