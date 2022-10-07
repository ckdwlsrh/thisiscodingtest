import sys

INF = int(1e9)

N = int(sys.stdin.readline().rstrip())

A = list(map(int, sys.stdin.readline().rstrip().split()))
sign = list(map(int, sys.stdin.readline().rstrip().split()))

result_max = -1 * INF
result_min = INF
        
        
def dfs(sign, result, i):
    global result_max, result_min
    if N == i:
        result_max = max(result_max,result)
        result_min = min(result_min,result)
    if sign[0] > 0:
        sign[0] -= 1
        dfs(sign,result + A[i], i + 1)
        sign[0] += 1
    if sign[1] > 0:
        sign[1] -= 1
        dfs(sign,result - A[i], i + 1)
        sign[1] += 1
    if sign[2] > 0:
        sign[2] -= 1
        dfs(sign,result * A[i], i + 1)
        sign[2] += 1
    if sign[3] > 0:
        sign[3] -= 1
        if result < 0 and A[i] > 0:
            dfs(sign, result * (-1) // A[i] * (-1),i + 1)
        else:
            dfs(sign,result // A[i], i + 1)
        sign[3] += 1
        
dfs(sign,A[0],1)

print(result_max)
print(result_min)