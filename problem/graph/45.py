import sys
from collections import deque

test_case = int(sys.stdin.readline().rstrip())

for _ in range(test_case):
    n = int(sys.stdin.readline().rstrip())
    team = list(map(int, sys.stdin.readline().rstrip().split()))
    
    topology = [0] * (n+1)
    nodes = set()
    for i in range(n):
        topology[team[i]] = i
        for j in range(i+1, n):
            nodes.add((team[i],team[j]))
    
    check = 0
    m = int(sys.stdin.readline().rstrip())
    for i in range(m):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        if (b, a) in nodes:
            nodes.remove( (b, a) )
            topology[a] -= 1
            topology[b] += 1
            nodes.add( (a, b) )
        elif (a, b) in nodes:
            nodes.remove( (a, b) )
            topology[b] -= 1
            topology[a] += 1
            nodes.add( (b, a) )
    
    #topology sort
    queue = deque([])
    for i in range(1, n + 1):
        if topology[i] == 0:
            queue.append(i)
            break
        
    
    result = ""
    for i in range(n):
        if not queue:
            check = 1
            break
        elif len(queue) >= 2:
            check = 2
            break
        
        now = queue.popleft()
        result += str(now) + " "
        for j in range(1, n + 1):
            if (now, j) in nodes:
                topology[j] -= 1
                if topology[j] == 0:
                    queue.append(j)
    
    if check == 1:
        print("IMPOSSIBLE")
    elif check == 2:
        print("?")
    else :
        print(result)
    