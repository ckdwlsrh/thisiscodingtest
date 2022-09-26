import sys


n = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
t = list(map(int, sys.stdin.readline().rstrip().split()))

def bs(x):
    front = 0
    end = n - 1
    
    while front <= end:
        mid = (front + end) // 2
        if x == data[mid] :
            return "yes"
        elif x > data[mid] :
            front = mid + 1
        elif x < data[mid] :
            end = mid - 1
            
    return "no"



data.sort()

for i in range(m):
    print(bs(t[i]), end = " ")
    