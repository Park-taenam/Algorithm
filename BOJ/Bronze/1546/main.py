import sys

N = int(sys.stdin.readline().strip())

scores = list(map(int, sys.stdin.readline().strip().split(" ")))
scores = [float(x/max(scores))*100 for x in scores]
print(sum(scores)/N)