'''https://hongcoding.tistory.com/42'''
import sys
from collections import deque

t = int(sys.stdin.readline().strip())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().strip().split())

    queue = deque(map(int, sys.stdin.readline().strip().split()))
    cnt = 0
    while queue:
        best = max(queue)
        front = queue.popleft()
        m -= 1

        if best == front:
            cnt += 1
            if m < 0:
                print(cnt)
                break
        else:
            queue.append(front)
            if m<0:
                m = len(queue) -1