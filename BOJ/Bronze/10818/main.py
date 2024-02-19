import sys

N = int(sys.stdin.readline().strip())

temp = list(map(int, sys.stdin.readline().strip().split(" ")))
print(min(temp), max(temp))