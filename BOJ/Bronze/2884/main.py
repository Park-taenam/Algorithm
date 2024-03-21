import sys

h, m = map(int, sys.stdin.readline().strip().split())

if m>=45:
    print(h, m-45)
else:
    if h>=1:
        print(h-1, m+60-45)
    else:
        print(h+24-1, m+60-45)