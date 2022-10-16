import sys

n = int(sys.stdin.readline().rstrip())

h = list(map(int,sys.stdin.readline().rstrip().split()))

check = {}
for i in h:
    try : check[i] += 1
    except: check[i] = 1

p = 0
result = 0
for i in sorted(check.keys()):
    result += (check[i] + p)// i
    p = (check[i] + p) % i
    
print(result)
