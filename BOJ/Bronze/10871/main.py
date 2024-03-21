import sys

n,x = map(int,sys.stdin.readline().strip().split())

nums = list(map(int,sys.stdin.readline().strip().split()))

for num in nums:
    if num < x:
        print(num, end=" ")