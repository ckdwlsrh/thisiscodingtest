
def check(building):
    for x, y, a in building:
        if a == 0: # 기둥
            if y != 0 and (x - 1, y, 1) not in building and (x, y, 1) not in building and (x,y - 1,0) not in building:
                return True
        elif a == 1: # 보
            if (x + 1, y - 1, 0) not in building and (x, y - 1, 0) not in building and ((x - 1,y, 1) not in building or (x + 1,y,1) not in building):
                return True
    return False
            

def solution(n, build_frame):
    
    answer = set()
    
    for x, y, a, b in build_frame:
        if b:
            answer.add((x,y,a))
            if check(answer):
                answer.remove((x,y,a))
        else:
            answer.remove((x,y,a))
            if check(answer):
                answer.add((x,y,a))

    answer = list(answer)
    answer.sort(key=lambda k:(k[0],k[1],k[2]))
    return answer

print(solution(5,[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))