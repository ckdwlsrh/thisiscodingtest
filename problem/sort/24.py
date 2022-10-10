import sys

N = int(sys.stdin.readline().rstrip())
antena = list(map(int, sys.stdin.readline().rstrip().split()))

antena.sort()

print(antena[(N - 1) // 2])






