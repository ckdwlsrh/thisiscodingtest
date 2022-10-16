import sys

n = int(sys.stdin.readline().rstrip())
coin = list(map(int, sys.stdin.readline().rstrip().split()))
coin.sort()
result = 1

for i in coin:
    if result < i:
        break
    result += i

print(result)