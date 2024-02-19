import sys

N = int(sys.stdin.readline().strip())

for _ in range(N):
    a,b = map(int, sys.stdin.readline().strip().split(" "))
    print(a+b)