import sys

while True:
    a,b,c = sorted(map(int, sys.stdin.readline().strip().split(" ")))
    
    if (a==0) and (b==0) and (c==0):
        break
    
    if c**2 == (a**2 + b**2):
        print('right')
    else:
        print('wrong')