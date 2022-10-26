import sys

N = int(sys.stdin.readline().rstrip())

hoban = list(map(int, sys.stdin.readline().rstrip().split()))
hoban.sort()

h = len(hoban)
if h%2 == 0:
    print(sum(hoban[h//2:])*2)

else:
    print(sum(hoban[h//2 + 1:]) * 2 + hoban[h//2])
