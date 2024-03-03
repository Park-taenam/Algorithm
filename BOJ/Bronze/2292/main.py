import sys

N = int(sys.stdin.readline().strip())

temp = 1
cnt = 1
while True:
    if N <= temp:
        print(cnt)
        break
    
    temp += 6*cnt
    cnt += 1
    