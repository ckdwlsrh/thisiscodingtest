import sys
from collections import deque

N, M = map(int,sys.stdin.readline().rstrip().split())
recipe = [[] for _ in range(N + 1)]
p = [0] * (N + 1)
answer = []

for _ in range(M):
    arr = list(map(int,sys.stdin.readline().rstrip().split()))
    recipe[arr[-1]].append(set(arr[1:-1]))
    p[arr[-1]] += arr[0]

L = int(sys.stdin.readline().rstrip())
potions = list(map(int,sys.stdin.readline().rstrip().split()))
q = deque([])

for i in potions:
    p[i]

print(recipe)

#위상정렬하면 끝남 ㅇㅇ