import sys

s = sys.stdin.readline().rstrip()
t = sys.stdin.readline().rstrip()

for i in range(15):
    s += s
    t += t
    
for i in range(1000):
    if s[i] != t[i]:
        print(0)
        exit(0)

print(1)
    
