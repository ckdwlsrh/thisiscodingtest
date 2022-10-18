import itertools

N = int(input())

A = list(map(int, input().split()))

result = 0
for Arr in itertools.permutations(A,N):
    total = 0
    last = Arr[0]
    for i in Arr[1:]:
        total += abs(i - last)
        last = i
    
    result = max(result, total)
    
print(result)