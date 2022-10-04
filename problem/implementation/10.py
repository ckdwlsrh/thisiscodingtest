import copy

def turn(key, m):
    key_turned =[[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            key_turned[j][m - i - 1] = key[i][j]
    return key_turned

def check(key, lock, x, y, n, m):
    lock_copy = copy.deepcopy(lock)
    
    for i in range(x, x + m):
        for j in range(y, y + m):
            if lock_copy[i][j] == 1 and key[i - x][j - y] == 1:
                return False
            else:
                lock_copy[i][j] += key[i - x][j - y]
                
    cnt = 0
    for i in range(m - 1, n + m - 1):
        for j in range(m - 1, n + m - 1):
            if lock_copy[i][j] == 1:
                cnt += 1
    if cnt == n * n:
        return True
    return False

def solution(key, lock):
    
    n = len(lock)
    m = len(key)
    n_wide = n + 2 * (m - 1)
    lock_wide = [[0] * (n_wide) for _ in range(n_wide)]
    
    for i in range(m - 1, n + m - 1):
        for j in range(m - 1, n + m - 1):
            lock_wide[i][j] = lock[i - (m - 1)][j - (m - 1)]
    
    for q in range(4):
        for i in range(n + m - 1):
            for j in range(n + m - 1):
                if check(key, lock_wide, i, j, n, m):
                    return True
        key = turn(key, m)
    
    return False

t = solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]])
if t:
    print("true")
else:
    print("false")