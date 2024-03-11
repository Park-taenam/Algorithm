'''https://claude-u.tistory.com/443'''
'''이분탐색'''
import sys

k, n = map(int, sys.stdin.readline().strip().split())
lan = [int(sys.stdin.readline().strip()) for _ in range(k)]
start, end = 1, max(lan)

while start <= end:
    mid = (start+end) // 2
    lines = 0
    for i in lan:
        lines += i // mid
    
    if lines >= n:
        start = mid+1
    else:
        end = mid-1
print(end)