"""def check(n, f_cnt, dist, weak):
    friend = dist[0]
    if not weak:
        return min(f_cnt, f_cnt - len(dist))
    
    result = 9999
    for i in weak:
        weak.remove(i)
        if not weak:
            return min(f_cnt, f_cnt - len(dist[1:]))
        tmp = set()
        # 반시계 방향
        #i + friend or i - friend 내부에 존재할 경우 weak 삭제
        for j in weak:
            if i - friend < 0:
                if  (0 <= j and j <= i) or ( j < n and n + (i - friend) <= j):
                    tmp.add(j)
            else:
                if i - friend <= j and j <= i:
                    tmp.add(j)
                    
        
        left = check(n,f_cnt,dist[1:],weak.difference(tmp))
        tmp.clear()
        # 오른쪽
        for j in weak:
            if i + friend >= n:
                if  (0 <= j and j <= (i + friend) - n) or ( j < n and i <= j):
                    tmp.add(j)
            else:
                if i <= j and j <= i + friend:
                    tmp.add(j)
    
        right = check(n,f_cnt,dist[1:],weak.difference(tmp))
        tmp.clear()
        
        result = min(result, left,right)
        #삭제했던 녀석 추가
        weak.add(i)
    return result

def solution(n, weak, dist):
    dist.sort(reverse=True)
    m = len(dist)
    weak = set(weak)
    
    answer = check(n, m, dist, weak)
    
    return answer


print(solution(12,[1, 5, 6, 10],[1, 2, 3, 4]))"""

import itertools
def solution(n, weak, dist):
    length = len(weak)
    for i in range(length):
        weak.append(weak[i]+n)
    answer = len(dist)+1
    for start in range(length):
        for friends in list(itertools.permutations(dist,len(dist))):
            count = 1
            position = weak[start]+friends[count-1]
            for i in range(start, start+length):
                if position < weak[i] :
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[i]+friends[count-1]

            answer = min(count,answer)

    if answer > len(dist):
        return -1
    return answer