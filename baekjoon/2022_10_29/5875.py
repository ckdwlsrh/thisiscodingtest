import sys
a = list(sys.stdin.readline().rstrip())
result = 0
open, close, total = 0, 0, 0
for i in range(len(a)):
    if a[i] == "(":
        open += 1
        total += 1
    else:
        close += 1
        total -= 1
    if total == -1:
        result = close
        break
    if total == 1:
        open = 0
if total == 2:
    result = open
print(result)