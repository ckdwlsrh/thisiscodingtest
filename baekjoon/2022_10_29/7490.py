import sys
import itertools


N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    
    M = int(sys.stdin.readline().rstrip())
    for i in itertools.product([" ","+","-"], repeat = M - 1):
        s = ""
        for j, op in zip(range(1, M+1),list(i)+[" "]):
            s += str(j) + str(op)
        
        if eval(s.replace(" ","")) == 0:
            print(s.rstrip())
    print()