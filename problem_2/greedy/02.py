import sys

number = sys.stdin.readline().rstrip()

max = int(number[0])
for i in number[1:]:
    if int(i) <= 1 or max <= 1:
        max += int(i)
    else:
        max *= int(i)

print(max)