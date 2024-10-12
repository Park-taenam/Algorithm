import sys

lst = [sys.stdin.readline().strip() for _ in range(3)]

print(int(lst[0])+int(lst[1])-int(lst[2]))
print(int(str(lst[0])+str(lst[1]))-int(lst[2]))