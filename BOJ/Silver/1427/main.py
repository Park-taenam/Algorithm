import sys

x  = sys.stdin.readline().strip()
x = [v for v in x]
x = sorted(x)
for i in range(len(x)):
    print(x[-(i+1)], end='')