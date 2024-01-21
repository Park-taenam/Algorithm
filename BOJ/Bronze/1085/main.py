import sys

read = sys.stdin.readline

x,y,w,h = [int(v) for v in read().split('\n')[0].split()]

min = 9999

for i,p in enumerate([0,0,w,h]):
    if i%2==0:
        if min>abs(p-x):
            min = abs(p-x)
    else:
        if min>abs(p-y):
            min = abs(p-y)

print(min)