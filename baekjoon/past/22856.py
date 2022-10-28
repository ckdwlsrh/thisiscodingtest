import sys

n = int(sys.stdin.readline().rstrip())

tree = {}
for i in range(n):
    root, l, r = map(int, sys.stdin.readline().rstrip().split())
    tree[root] = [l , r]

cnt = 0
right = 0
now = 1

while True:
    if tree[now][1] == -1:
        break
    else:
        now = tree[now][1]
        right += 1

stack = [1]

while stack:
    now = stack[-1]
    #print(now)
    l, r = tree[now]
    
    if l != -1:
        tree[now][0] = -1
        cnt += 2
        stack.append(l)
        continue
    
    stack.pop()
    #print(stack.pop())
    if r != -1:
        tree[now][1] = -1
        cnt += 2
        stack.append(r)
        
print(cnt - right)