import sys


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    parent = [_ for _ in range(N + 1)]
    num = list(map(int, sys.stdin.readline().rstrip().split()))
    
    result = N
    for i in range(1, N + 1):
        a = find(parent, i)
        b = find(parent, num[i - 1])
        if a == b:
            now = i
            cy = i
            while True:
                result -= 1
                if now == num[cy - 1]:
                    break
                cy = num[cy - 1]
        else:
            union(parent, a, b)

    print(result)