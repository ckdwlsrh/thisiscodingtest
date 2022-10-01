def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    answer = 0
    n = len(food_times)
    l = n
    c = {}
    for x in food_times:
        try : c[x] += 1
        except: c[x] = 1

    copy = sorted(c.keys())
    
    front = 0
    for i in copy:
        now = i - front
        if k < n * now:
            break
        else:
            k -= n * now
            n -= c[i]
            front = i
    
    cnt = 0
    k %= n
    for x in range(l):
        if food_times[x] >= i:
            if k > 0:
                k -= 1
            elif k == 0:
                break
        else:
            cnt += 1
    answer = x + 1
    return answer