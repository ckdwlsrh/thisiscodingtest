import sys

m = int(sys.stdin.readline().rstrip())

def count_zero(num):
    five = 5
    cnt = 0
    while five <= num:
        cnt += num // five
        five *= 5
    
    return cnt
    
first = 1
end = m * 5
result = 0

while first <= end:
    mid = (first + end) // 2
    
    cnt = count_zero(mid)
    
    if cnt < m:
        first = mid + 1
    else:
        end = mid - 1
        result = mid

if m == count_zero(result):
    print(result)
else:
    print(-1)