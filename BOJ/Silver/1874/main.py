'''https://data-flower.tistory.com/98'''

import sys
from collections import deque

n = int(sys.stdin.readline().strip())
stack, results, find = [], [], True

now = 1
for _ in range(n):
    num = int(sys.stdin.readline().strip())

    while now <= num:
        stack.append(now)
        results.append("+")
        now += 1

    if stack[-1] == num:
        stack.pop()
        results.append("-")
    else:
        find = False

if find:
    for i in results:
        print(i)
else:
    print("NO")