def solution(N, stages):
    answer = {}
    cleared = [0 for _ in range(N + 2)]
    not_cleared = [0 for _ in range(N + 2)]
    
    for i in stages:
        not_cleared[i] += 1
        for j in range(1, i):
            cleared[j] += 1
    
    for i in range(1, N+1):
        if (not_cleared[i] + cleared[i]) == 0:
            answer[i] = 0
        else:
            answer[i] = not_cleared[i] / (not_cleared[i] + cleared[i])
    
    return sorted(answer, key = lambda k: answer[k], reverse=True)

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))