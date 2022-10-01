where = input()
i = int(where[1])
j = int(ord(where[0])) - 96

steps = [(-2, -1),(-2,1),(2,-1),(2,1),(-1,-2),(-1,2),(1,-2),(1,2)]
cnt = 0;
for k in steps :
    x = i + k[0]
    y = j + k[1]
    if x >= 1 and x <= 8 and y <= 8 and y >= 1 :
        cnt +=1

print(cnt)
