n = int(input())
array = [int(input()) for _ in range(n)]

array = sorted(array, reverse=True)

for i in array:
    print(i, end = " ")

