def change(u,v):
    if not v:
        return ''
    op, cl = 0, 0
    for i in range(len(v)):
        if v[i] == '(':
            u += v[i]
            op += 1
        elif p[i] == ')':
            u += v[i]
            cl += 1
        if op == cl:
            v = v[i+1:]
            break
    # 검증
    

def solution(p):
    answer = change('',p)
    
    return answer