import sys

n = int(sys.stdin.readline().strip())
size_lst = list(map(int, sys.stdin.readline().strip().split()))
t,p = map(int, sys.stdin.readline().strip().split())

res1  = 0
for i in range(6):
    cnt = size_lst[i]//t if size_lst[i]%t == 0 else size_lst[i]//t+1
    res1 += cnt
print(res1)

print(n//p, n%p, sep=" ")