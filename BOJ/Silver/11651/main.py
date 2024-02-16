import sys

N = int(sys.stdin.readline().strip())

points = []
for _ in range(N):
    [x,y] = map(int, sys.stdin.readline().strip().split(" "))
    points.append([x,y])

points.sort(key = lambda x: (x[1], x[0]))

for point in points:
    print(f"{point[0]} {point[1]}")