def change(u,v):
    if not v:
        return ''
    op, cl = 0, 0
    for i in range(len(v)):
        if v[i] == '(':
            u += v[i]
            op += 1
        elif v[i] == ')':
            u += v[i]
            cl += 1
        if op == cl:
            v = v[i+1:]
            break
    # u검증
    check = 0
    op = 0
    for i in u:
        if i == '(':
            op += 1
        else:
            if op == 0:
                check = 1
                break
            op -= 1
    
    if check == 1 or op > 0 or op < 0:
        tmp = '('
        tmp += change('',v) + ')'
        u = u[1:-1]
        for i in u:
            if i == '(':
                tmp += ')'
            elif i == ')':
                tmp += '('
        
        u = tmp
    else:
        u += change('',v)
    
    return u
        
def solution(p):
    answer = change('',p)
    
    return answer

print(solution('()))((()'))