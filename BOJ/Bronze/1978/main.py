import sys

N = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().strip().split(" ")))

cnt = N
for number in numbers:
    if number == 1:
        cnt -= 1
        continue
    for i in range(2, number):
        if number%i == 0:
            cnt -= 1
            break

print(cnt)