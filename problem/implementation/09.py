def solution(s):
    n = len(s)
    answer = n
    for i in range(1, n//2 + 1):
        pattern = s[0:i]
        check = 0
        comp = ""
        for j in range(i,n,i):            
            if pattern == s[j:j + i]:
                check = 1
            else:
                pattern = s[j:j + i]
                comp += pattern + '1' if check == 1 else pattern
                check = 0
        comp += pattern + '1' if check == 1 else pattern
        answer = min(answer, len(comp))
    return answer

solution('aabbaccc')