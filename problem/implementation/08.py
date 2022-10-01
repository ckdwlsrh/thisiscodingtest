import sys
S = sys.stdin.readline().rstrip()
S = sorted(S)
s = 0
for i in range(len(S)):
    if S[i] > '9':
        break
    else:
        s += int(S[i])

print(''.join(map(str,S[i:])) + str(s))