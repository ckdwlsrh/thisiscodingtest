import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
h = list(map(int, sys.stdin.readline().rstrip().split()))

def bs():
    front = 0
    end = max(h)
    result = 0
    
    while front <= end:
        mid = (front + end) // 2
        s = 0
        for i in range(n):
            if mid < h[i]:
                s += h[i] - mid
        
        result = mid
        if s > m:
            front = mid + 1
        elif s < m:
            end = mid - 1
        else:
            break
    
    return result

print(bs())
