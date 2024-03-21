import sys

x = list(map(int, sys.stdin.readline().strip().split()))

result = 0
for num in x:
    result += num**2
print(result%10)