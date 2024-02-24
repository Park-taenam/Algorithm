import sys
from math import prod

a, b = map(int, sys.stdin.readline().strip().split(" "))

results = []
while True:
    temp_bool = True
    temp = min(a,b)
    if temp < 2:
        break
    for i in range(2, temp+1):
        if (a % i)==0 and (b % i)==0:
            results.append(i)
            a = a//i
            b = b//i
            temp_bool = False
            continue
    if temp_bool:
        break
print(prod(results))
print(a*b*prod(results))