import sys

n = 0
trees = {}

while True:
    tree = sys.stdin.readline().rstrip()
    if not tree:
        break
    n += 1
    if tree in trees:
        trees[tree] += 1
    else:
        trees[tree] = 1

for i in sorted(trees.keys()):
    print(i, "%0.4f" % (trees[i] / n * 100))