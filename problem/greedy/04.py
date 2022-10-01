import sys

n = int(sys.stdin.readline().rstrip())
coin = list(map(int,sys.stdin.readline().rstrip().split()))

coin.sort()
max = 1
for x in coin:
    if max < x:
        break
    max += x
    
print(max)